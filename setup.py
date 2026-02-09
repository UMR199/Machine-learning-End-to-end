from setuptools import find_packages,setup

def get_req(file_path):
    requirments =[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]
        if "-e ." in requirments:
            requirments.remove("-e .")
    return requirments

setup(
    name="ML_Project",
    version='0.0.1',
    author="MUHAMMAD UMAR",
    author_email="mhunterkhan@gmail.com",
    packages = find_packages(),
    install_requires = get_req("requirements.txt")
)