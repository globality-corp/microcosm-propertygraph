#!/usr/bin/env python
from setuptools import find_packages, setup

project = "microcosm-propertygraph"
version = "1.1.0"

setup(
    name=project,
    version=version,
    description="Microcosm Property graph - Conventions for exposing data as a property graph",
    author="Globality Engineering",
    author_email="engineering@globality.com",
    url="https://github.com/globality-corp/microcosm",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    keywords="microcosm",
    install_requires=[
        "microcosm>=2.12.0",
        "microcosm-flask>=2.6.0",
    ],
    setup_requires=[
        "nose>=1.3.7",
    ],
    dependency_links=[
    ],
    entry_points={
        "console_scripts": [
            "neo4-nodes = micrcosm_propertygraph.neo4j:export_nodes_main",
            "neo4-relationships = micrcosm_propertygraph.neo4j:export_relationships_main",
        ],
        "microcosm.factories": [
        ],
    },
    tests_require=[
        "coverage>=3.7.1",
        "PyHamcrest>=1.9.0",
    ],
)
