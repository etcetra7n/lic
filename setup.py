from setuptools import setup
from setuptools.command.install import install
from os import path, listdir, makedirs
from shutil import copy

class CustomInstall(install):
    def run(self):
        if not(path.exists("C:/licenses/")):
            makedirs("C:/licenses/")
        lic_files = listdir("./licenses")
        for file in lic_files:
            copy(f"./licenses/{file}", "C:/licenses/")

setup(
    packages= ['src'],
    cmdclass={'install': CustomInstall},
)
# attr: __init__.__version__
