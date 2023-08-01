from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        this function will return list of requirements/libraries
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements =  file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='statanomaly',
    version='0.0.1',
    author='Kiran R Krishnan',
    author_email='kiranrkrishnan07@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)