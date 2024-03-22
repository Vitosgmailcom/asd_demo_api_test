from setuptools import setup, find_packages

setup(version="1.1",
      packages=find_packages(),
      install_requires = [
            "pytest==8.1.1",
            "pytest-html==4.1.1",
            "requests==2.31.0",
            "PyMySql==1.1.0"
            ]
      )