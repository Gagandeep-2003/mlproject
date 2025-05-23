# It is responsible for creating my Machine Learning Application as a package.
# it will help us to distribute the package and install it in any system.
# it will help us to install the dependencies.
# it will help us to run the application from any system.
# it will help us to create the build of the application.
# it will help us to create the distribution of the application.
# it will help us to create the wheel of the application.
# it will help us to create the source distribution of the application.

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    ''''this function will return the list of requirements
    written in requirements.txt file'''
    requirements = []
    
    with open (file_path) as file_obj:
        requirements_file = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

# It is meta data information for our project.
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'gagan',
    author_email = 'gagan@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)