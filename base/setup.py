from setuptools import setup


setup(
    name='common-tests',
    version='4.1.2-rr2-SNAPSHOT',

    author="Confluent, Inc.",

    description='Docker image tests',

    url="https://github.com/confluentinc/common",

    dependency_links=open('requirements.txt').read().split("\n"),

    packages=['test'],

    include_package_data=True,

    python_requires='>=2.7',
    setup_requires=['setuptools-git'],

)
