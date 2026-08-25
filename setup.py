from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
'''

Ye setup.py file basically tumhare ML project ko Python package ke form mein install/configure karne ke liye hai; setuptools se project ki packaging hoti hai, get_requirements() function requirements.txt ko read karke saari required libraries ki list banata hai, req.strip() extra spaces/newlines hataata hai, -e . ko requirements list se remove karta hai kyunki ye current project ko editable mode mein install karne ka command hai, aur last mein setup() project ka name (mlproject), version, author, packages (find_packages() se project ke Python packages automatically find) aur required libraries (install_requires) define karta hai. Simple mein: setup.py 
Python ko batata hai ki tumhara project kya hai, uske packages kaunse hain aur project chalane ke liye kaunsi libraries install karni hain.

'''


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Vishvesh',
    author_email='walunjvishvesh21@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)