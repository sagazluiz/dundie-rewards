# setuptools

# pyproject

# external build tools (poetry, flit)

from setuptools import find_packages, setup

setup(
    name = "dundie",
            # x.y.z
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    author="Bruno Rocha / Fabio Araujo",
    packages=find_packages(),
    
)

