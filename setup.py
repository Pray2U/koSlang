# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    setup(
        name='koslang',#module 이름
        version='1.0.0',
        description='Can detect slang in Korean.',
        author='koSlang',
        author_email='diadiahun0902@gmail.com',
        long_description=long_description,
        python_requires='>=3.10',
        long_description_content_type="text/markdown",
        license='MIT',
        py_modules=['modules'], #업로드할 module
        install_requires=["eunjeon"], #module 필요한 다른 module
        packages=['koslang'] #업로드할 module이 있는 폴더
    )