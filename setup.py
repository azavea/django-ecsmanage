import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

description = (
    'Run any Django management command on an AWS Elastic Container Service (ECS)'
    'cluster.'
)

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ecsmanage',
    version='0.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',
    description=description,
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/azavea/django-ecsmanage/',
    author='Azavea',
    author_email='yourname@example.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        'Django >=1.11, <=2.1',
        'boto3 >=1.9.0'
    ]
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)