# -*- coding: future_fstrings -*-

import boto3
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = "Run a one-off management command on an ECS cluster."

    def add_arguments(self, parser):
        parser.add_argument(
            "-e",
            "--env",
            type=str,
            default="default",
            help=(
                "Environment to run the task in, as defined in"
                "ECSMANAGE_ENVIRONMENTS."
            ),
        )

        parser.add_argument(
            "cmd",
            type=str,
            nargs="+",
            help="Command override for the ECS container (e.g. 'migrate')",
        )

    def handle(self, *args, **options):
        """
        Run the given command on the latest app CLI task definition and print
        out a URL to view the status.
        """
        self.env = options["env"]
        cmd = options["cmd"]

        config = self.parse_config()

        aws_region = config["AWS_REGION"]

        self.ecs_client = boto3.client("ecs", region_name=aws_region)
        self.ec2_client = boto3.client("ec2", region_name=aws_region)

        task_def_arn = self.get_task_def(config["TASK_DEFINITION_NAME"])
        security_group_id = self.get_security_group(config["SECURITY_GROUP_TAGS"])
        subnet_id = self.get_subnet(config["SUBNET_TAGS"])

        task_id = self.run_task(config, task_def_arn, security_group_id, subnet_id, cmd)

        cluster_name = config["CLUSTER_NAME"]

        url = (
            f"https://console.aws.amazon.com/ecs/home?region={aws_region}#"
            f"/clusters/{cluster_name}/tasks/{task_id}/details"  # NOQA
        )

        self.stdout.write(self.style.SUCCESS(f"Task started! View here:\n{url}"))  # NOQA

    def parse_config(self):
        """
        Parse configuration settings for the app, checking to make sure that
        they're valid.
        """
        if getattr(settings, "ECSMANAGE_ENVIRONMENTS") is None:
            raise CommandError(
                "ECSMANAGE_ENVIRONMENTS was not found in the Django settings."
            )

        ecs_configs = settings.ECSMANAGE_ENVIRONMENTS.get(self.env, None)
        if ecs_configs is None:
            raise CommandError(
                f'Environment "{self.env}" is not a recognized environment in '
                "ECSMANAGE_ENVIRONMENTS (environments include: "
                f"{settings.ECSMANAGE_ENVIRONMENTS.keys()})"
            )

        config = {
            "TASK_DEFINITION_NAME": "",
            "CLUSTER_NAME": "",
            "SECURITY_GROUP_TAGS": "",
            "SUBNET_TAGS": "",
            "LAUNCH_TYPE": "FARGATE",
            "AWS_REGION": "us-east-1",
        }

        for config_name, config_default in config.items():
            if ecs_configs.get(config_name) is None:
                if config_default == "":
                    raise CommandError(
                        f'Environment "{self.env}" is missing required config '
                        f"attribute {config_name}"
                    )
                else:
                    config[config_name] = config_default
            else:
                config[config_name] = ecs_configs[config_name]

        return config

    def parse_response(self, response, key, idx=None):
        """
        Perform a key-value lookup on a response from the AWS API, wrapping it
        in error handling such that if the lookup fails the response body
        will get propagated to the end user.
        """
        if not response.get(key):
            msg = f"Unexpected response from ECS API: {response}"
            raise KeyError(msg)
        else:
            if idx is not None:
                try:
                    return response[key][0]
                except (IndexError, TypeError):
                    msg = f"Unexpected value for '{key}' in response: " f"{response}"  # NOQA
                    raise IndexError(msg)
            else:
                return response[key]

    def get_task_def(self, task_def_name):
        """
        Get the ARN of the latest ECS task definition with the name
        task_def_name.
        """
        task_def_response = self.ecs_client.list_task_definitions(
            familyPrefix=task_def_name, sort="DESC", maxResults=1
        )

        return self.parse_response(task_def_response, "taskDefinitionArns", 0)

    def get_security_group(self, security_group_tags):
        """
        Get the ID of the first security group with tags corresponding to
        security_group_tags.
        """
        filters = []
        for tagname, tagvalue in security_group_tags.items():
            filters.append({"Name": f"tag:{tagname}", "Values": [tagvalue]})

        sg_response = self.ec2_client.describe_security_groups(Filters=filters)

        security_group = self.parse_response(sg_response, "SecurityGroups", 0)
        return security_group["GroupId"]

    def get_subnet(self, subnet_tags):
        """
        Get the ID of the first subnet with tags corresponding to subnet_tags.
        """
        filters = []
        for tagname, tagvalue in subnet_tags.items():
            filters.append({"Name": f"tag:{tagname}", "Values": [tagvalue]})

        subnet_response = self.ec2_client.describe_subnets(Filters=filters)

        subnet = self.parse_response(subnet_response, "Subnets", 0)
        return subnet["SubnetId"]

    def run_task(self, config, task_def_arn, security_group_id, subnet_id, cmd):
        """
        Run a task for a given task definition ARN using the given security
        group and subnets, and return the task ID.
        """
        overrides = {"containerOverrides": [{"name": "django", "command": cmd}]}

        task_def = self.ecs_client.describe_task_definition(
            taskDefinition=task_def_arn
        )["taskDefinition"]

        # Only the awsvpc network mode supports the networkConfiguration
        # input value.
        if task_def["networkMode"] == "awsvpc":
            network_configuration = {
                "awsvpcConfiguration": {
                    "subnets": [subnet_id],
                    "securityGroups": [security_group_id],
                }
            }

            task_response = self.ecs_client.run_task(
                cluster=config["CLUSTER_NAME"],
                taskDefinition=task_def_arn,
                overrides=overrides,
                networkConfiguration=network_configuration,
                count=1,
                launchType=config["LAUNCH_TYPE"],
            )
        else:
            task_response = self.ecs_client.run_task(
                cluster=config["CLUSTER_NAME"],
                taskDefinition=task_def_arn,
                overrides=overrides,
                count=1,
                launchType=config["LAUNCH_TYPE"],
            )

        task = self.parse_response(task_response, "tasks", 0)

        # Parse the ask ARN, since ECS doesn't return the task ID.
        # Task ARNS look like: arn:aws:ecs:<region>:<aws_account_id>:task/<id>
        task_id = task["taskArn"].split("/")[1]
        return task_id
