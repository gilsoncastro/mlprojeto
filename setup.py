from setuptools import find_packages,setup
from typing import List

HYPE_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    Essa função vai retornar a lista de requisitos
    '''
    requirements=[]
    with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n","") for req in requirements]

         if HYPE_E_DOT in requirements:
              requirements.remove(HYPE_E_DOT)

    return requirements


setup(
 name='mlprojeto',
 version='0.0.1',
 author='Gilson Castro',
 author_email='gilson_castro@yahoo.com',
 packages=find_packages(),
 install_requires=get_requirements('requirements.txt')

)