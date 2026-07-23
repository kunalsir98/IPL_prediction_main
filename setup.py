<<<<<<< HEAD
from setuptools import find_packages,setup 
from typing import List 
=======
from setuptools import find_packages, setup 
from typing import List
>>>>>>> 4a4f3ce82f76aec236d6408a73373dc94d2d60f4

HYPHEN_DOT = '-e .'

<<<<<<< HEAD
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","")for i in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
=======
def get_requirements(file_path : str)->List[str] :
    requirements = []
    with open(file_path) as file_obj :
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_DOT in requirements :
            requirements.remove(HYPHEN_DOT)
>>>>>>> 4a4f3ce82f76aec236d6408a73373dc94d2d60f4

    return requirements

setup(
<<<<<<< HEAD
    name="ipl",
    version="0.0.1",
    author="kunal",
    author_email="kunalchopde98@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)



=======
    name = "IPLPRED",
    version = "0.0.1",
    author = "anand",
    author_email= "itsanandshrivastava@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()

)
>>>>>>> 4a4f3ce82f76aec236d6408a73373dc94d2d60f4
