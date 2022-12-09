# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='koslang',
    version='1.0',
    description='Can detect slang in Korean.',
    author='koSlang',
    author_email='diadiahun0902@gmail.com',
    long_description=long_description,
    python_requires='>=3.10',
    long_description_content_type="text/markdown",
    packages= find_packages(exclude = ['docs', 'tests*','__pycache__/']),
    )