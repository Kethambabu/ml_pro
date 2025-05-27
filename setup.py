from setuptools import find_packages,setup
from typing import List
e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    get_requirements=[]
    with open(file_path) as file_obj:
        get_requirements=file_obj.readlines()
        get_requirements=[req.replace("\n","") for req in get_requirements]
        if e_dot in get_requirements:
            get_requirements.remove(e_dot)
    return get_requirements
setup(

name='mlprojrct',
version='0.0.1',
auther='ketham',
auther_email='kethambau@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
