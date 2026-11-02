#importing the required modules
from pathlib import Path # works with paths
from typing import List # function is expected to return a list.
from setuptools import find_packages,setup # to find the packages and setup the package

# assign a root of the project
PROJECT_ROOT = Path(__file__).parent # setupfile path to its parents (Network_Security)

# defining a function
def get_requirements(file_path:str) -> List[str]:                                       # requirements.txt to list of str
    requirements=[]                                                                     # creating a empty list to store the requirements
    for requirement in (PROJECT_ROOT/file_path).read_text().splitlines():               # read the texts and split by lines through the project root and file path
        requirement=requirement.strip()                                                 # remove teh front and back spaces
        if requirement and requirement !="-e ." and not requirement.startswith("#"):    # it add requirements except -e . and comments 
            requirements.append(requirement)                                            # add to list (selected requirements only)
    return requirements                                                                 # returns the final list

setup(
    name="Network_Security",
    author="Jenison J",
    author_email="jenison717@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)