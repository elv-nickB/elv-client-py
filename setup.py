from setuptools import setup, find_packages

setup(
    name = "elv_client_py",
    packages=find_packages(),
    install_requires=['requests==2.31.0', 'base58==2.1.1'],
)