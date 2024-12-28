from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Teja kukatla',
    author_email ='kukatlateja1@gmail.com',
    install_requirements =["openai","langchain","streamlit","python-dotenv","pyPDF2"],
    packages=find_packages()
)