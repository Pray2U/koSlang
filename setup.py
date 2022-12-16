# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

setup(
    name='koslang',#module 이름
    version='1.0.6',
    description='Can detect slang in Korean.',
    author='koSlang',
    author_email='diadiahun0902@gmail.com',
    long_description="",
    python_requires='>=3.8',
    license='MIT',
    py_modules=['koslang'], #업로드할 module
    install_requires=["eunjeon","pandas"], #module 필요한 다른 module
    packages=['koslang'], #업로드할 module이 있는 폴더
    include_package_data=True,
)