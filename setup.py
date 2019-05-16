#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

install_requirements = [
    "sceptre>=2.1.2"
]

setup(
    name='sceptre-stack-termination-protection-hook',
    version="1.0.1",
    description="A Sceptre hook to enable and disable cloudformation"
                "stack termination protection",
    py_modules=['stack_termination_protection'],
    long_description=readme,
    long_description_content_type="text/markdown",
    author="zaro0508",
    author_email="zaro0508@gmail.com",
    license='Apache2',
    url="https://github.com/cloudreach/sceptre",
    entry_points={
        'sceptre.hooks': [
            'stack_termination_protection = '
            'stack_termination_protection:StackTerminationProtection',
        ],
    },
    keywords="sceptre",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    install_requires=install_requirements,
    include_package_data=True,
    zip_safe=False,
)
