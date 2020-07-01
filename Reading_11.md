Reading 11: 

# What is Data Science?

Data science is the study of data. It involves developing methods of recording, storing, and analyzing data to effectively extract useful information. The goal of data science is to gain insights and knowledge from any type of data — both structured and unstructured.

# Jupyter Installation

## Installation  
JupyterLab can be installed using conda, pip, pipenv or docker.  

conda  

If you use conda, you can install it with:

conda install -c conda-forge jupyterlab
pip  

If you use pip, you can install it with:

pip install jupyterlab 

If installing using pip install --user, you must add the user-level bin directory to your PATH environment variable in order to launch jupyter lab.

pipenv  

If you use pipenv, you can install it as:

pipenv install jupyterlab 

pipenv shell  

or from a git checkout:  

pipenv install git+git://github.com/jupyterlab/jupyterlab.git#egg=jupyterlab

pipenv shell

When using pipenv, in order to launch jupyter lab, you must activate the project’s virtualenv. For example, in the directory where pipenv’s Pipfile and Pipfile.lock live (i.e., where you ran the above commands):

pipenv shell

jupyter lab  

Docker  

If you have Docker installed, you can install and use JupyterLab by selecting one of the many ready-to-run Docker images maintained by the Jupyter Team. Follow the instructions in the Quick Start Guide to deploy the chosen Docker image. NOTE: Ensure your docker command includes the -e JUPYTER_ENABLE_LAB=yes flag to ensure JupyterLab is enabled in your container.



# What is NumPy?

NumPy is a commonly used Python data analysis package. By using NumPy, you can speed up your workflow, and interface with other packages in the Python ecosystem, like scikit-learn, that use NumPy under the hood. NumPy was originally developed in the mid 2000s, and arose from an even older package called Numeric. This longevity means that almost every data analysis or machine learning package for Python leverages NumPy in some way.