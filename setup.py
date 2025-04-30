from setuptools import setup, find_packages

setup(
    name="sample_python_script",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyspark"
    ],
    entry_points={
        "console_scripts": [
            "main=src.sample_script:main"
        ]
    }
)
