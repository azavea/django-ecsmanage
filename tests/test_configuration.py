from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import SimpleTestCase


class ConfigurationTestCase(SimpleTestCase):
    """
    Test the configuration of settings for the management command.
    """

    def test_failure_when_no_settings(self):
        """
        Test that the command throws an error when the ECSMANAGE_ENVIRONMENTS
        setting does not exist.
        """
        with self.assertRaises(CommandError):
            call_command("ecsmanage", "help")

    def test_failure_when_missing_environment(self):
        """
        Test that the command throws an error when the environment passed to
        the CLI does not exist in ECSMANAGE_ENVIRONMENTS.
        """
        ECSMANAGE_ENVIRONMENTS = {"staging": {}, "production": {}}
        with self.assertRaises(CommandError):
            with self.settings(ECSMANAGE_ENVIRONMENTS=ECSMANAGE_ENVIRONMENTS):
                call_command("ecsmanage", "help", env="foobar")

    def test_failure_when_no_task_def_name(self):
        """
        Test that the command throws an error when the configuration is missing
        a task definition name.
        """
        ECSMANAGE_ENVIRONMENTS = {
            "staging": {
                "CLUSTER_NAME": "foo",
                "SECURITY_GROUP_TAGS": {},
                "SUBNET_TAGS": {},
            }
        }
        with self.assertRaises(CommandError):
            with self.settings(ECSMANAGE_ENVIRONMENTS=ECSMANAGE_ENVIRONMENTS):
                call_command("ecsmanage", "help", env="staging")

    def test_failure_when_no_cluster_name(self):
        """
        Test that the command throws an error when the configuration is missing
        a cluster name.
        """
        ECSMANAGE_ENVIRONMENTS = {
            "staging": {
                "TASK_DEFINITION_NAME": "foo",
                "SECURITY_GROUP_TAGS": {},
                "SUBNET_TAGS": {},
            }
        }
        with self.assertRaises(CommandError):
            with self.settings(ECSMANAGE_ENVIRONMENTS=ECSMANAGE_ENVIRONMENTS):
                call_command("ecsmanage", "help", env="staging")

    def test_failure_when_no_security_group_tags(self):
        """
        Test that the command throws an error when the configuration is missing
        security group tags.
        """
        ECSMANAGE_ENVIRONMENTS = {
            "staging": {
                "TASK_DEFINITION_NAME": "foo",
                "CLUSTER_NAME": "bar",
                "SUBNET_TAGS": {},
            }
        }
        with self.assertRaises(CommandError):
            with self.settings(ECSMANAGE_ENVIRONMENTS=ECSMANAGE_ENVIRONMENTS):
                call_command("ecsmanage", "help", env="staging")

    def test_failure_when_no_subnet_tags(self):
        """
        Test that the command throws an error when the configuration is missing
        subnet tags.
        """
        ECSMANAGE_ENVIRONMENTS = {
            "staging": {
                "TASK_DEFINITION_NAME": "foo",
                "CLUSTER_NAME": "bar",
                "SECURITY_GROUP_TAGS": {},
            }
        }
        with self.assertRaises(CommandError):
            with self.settings(ECSMANAGE_ENVIRONMENTS=ECSMANAGE_ENVIRONMENTS):
                call_command("ecsmanage", "help", env="staging")
