# setup.py
from setuptools import setup, find_packages

setup(
    name="RushAPI",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="LizardRush",
    description="A library to communicate with Lizard Rush services",
    url="https://github.com/LizardRush/RushAPI",
)
