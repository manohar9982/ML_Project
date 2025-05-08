# status.py package banayenge hum ise pypi me dalenge to koi bhi ise install bhi kr skta hai
# pura application ka basic information hota h ve hum satup krte hai 

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' # muje ise bhi ignore krna hai
def get_requirements(file_path:str)-> List[str]:  # get requirement ek esa function banya jaha pe humne apna file path de diya vo hai string type uska return type hai list from of string  
    '''
    this function will return the list of requirements
    
    '''
    requirements=[]
    
    with open(file_path) as file_obj: # means file ko open krke read krega line by line
        requirements=file_obj.readlines()
        [req.replace('\n',"") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements




setup(
name = 'mlproject',
version = '0.0.1',
author = 'manohar',
author_email = 'manoharp99826@gamil.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt') # requirements.txt me jo jo library du vo autometicaly isme aa jana chahiye to

    
)