from setuptools import setup

setup(
    name="graphnet",
    version="0.1.0",
    description="A simple graph network comprising of nodes & edges for network analysis",
    url="https://github.com/shuds13/pyexample",
    author="Matthew Davidson",
    author_email="matthew.davidson@generalfusion.com",
    license="",
    packages=["graphnet"],
    install_requires=[
        "pandas",
        "openpyxl",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.9",
    ],
    scripts=[
        "tests/test_build_graphnetwork_from_file.py",
    ],
)
