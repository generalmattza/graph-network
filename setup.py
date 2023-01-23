from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="graphnet",
    version="0.1.0",
    description="A simple graph network comprising of nodes & edges for network analysis",
    long_description=readme,
    url="https://github.com/generalmattza/graph-network.git",
    author="Matthew Davidson",
    author_email="matthew.davidson@generalfusion.com",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=[
        "pandas",
        "openpyxl",
        "pytest",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.9",
    ],
)
