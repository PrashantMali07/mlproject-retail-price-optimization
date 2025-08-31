from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of required modules, which
    is important for this overall project which is written inside 
    a file named "requirements.txt"
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='retail-price-optimization',
version='1.0.0',
author='PrashantMali07',
author_email='er.prashantkmrmali@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)