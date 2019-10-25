from setuptools import setup

setup(
    name="integrity",
    version="0.1.0",
    author="Aleksandr Donskoi",
    author_email="donskoy.alexander@gmail.com",
    packages=["integrity"],
    entry_points={"console_scripts": ["integrity = integrity.__main__:main"]},
)
