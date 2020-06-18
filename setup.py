import os
from setuptools import setup, find_packages


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name="cdqa",
    version="1.3.9",
    author="Félix MIKAELIAN, André FARIAS, Matyas AMROUCHE, Olivier SANS, Théo NAZON",
    description="An End-To-End Closed Domain Question Answering System",
    url="https://github.com/cdqa-suite/cdQA",
    packages=find_packages(),
    install_requires=read("requirements.txt").split(),
)
