from setuptools import setup,find_packages
from typing import List

def get_requirements(file_name):
    requirement = []
    with open(file_name) as file:
        raw_requirement = file.readlines()
        for i in raw_requirement:
            word = i.replace("\n","")
            requirement.append(word)
        if "-e ." in requirement:
            requirement.remove("-e .")
    return requirement


setup(
name = "finance_complaint",
version = '0.0.1',
author = "Aakash Pal",
author_email='aakashpal1198@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
