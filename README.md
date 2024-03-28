# SoftEngProj
This is the git repository where we will work on our software engineering project. I will include some information that will be helpful for getting everything set up as well as some other helpful info and resources. 
## Git
Obviously, we will using [Git](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git#using-git). You will need to [install](https://git-scm.com/downloads) it and become familiar with the general workflow

You will need to [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository
### Git Workflow
It is important to understand the basics of how git works. These are some of the most important things: 
* Branches
* Fetch
* Merge
* Pull - This is a combination of Fetch and Merge. Either use this or Fetch and Merge every time you start doing any work so the code you have stays up to date with what is in the Git
* Push - understand what is upstream (what you are pushing to). Only push when your changes are complete and won't break other people's code
## Conda
To ensure that we are all using the same packages, we will use [Conda](https://docs.anaconda.com/free/miniconda/index.html). This is a pretty intuitive environment management tool
### Conda Environment Setup
You will need to install [miniconda](https://docs.anaconda.com/free/miniconda/index.html). Install with the default options. To use it, you'll need to open the Anaconda Prompt - just type Anaconda Prompt in the search bar and it'll show up.
The environment can be set up by running `conda env create -f env.yml`
### Other Conda Info
* To activate the environment: `conda activate seproject`
* The name is what the environment will be called after running the command above
* The channels are where conda searches for the packages 
* The dependencies are the packages we are using. If you have to add a package, follow the format of the other dependences `package=version`
## Django
[Django](https://docs.djangoproject.com/en/5.0/) is a Python package that will allow us to create websites using their modified version of HTML
### Important manage.py Commands
* runserver to start up the server
* collectstatic to allow the use of files in the edu_app/static directory. This will create a static directory in the root directory of the project to allow references to existing static files in the html
* makemigrations is used to create models
* migrate is used to apply created models to the database
### Resources
[Conda](https://docs.anaconda.com/free/miniconda/index.html)  

[Git](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git#using-git)

[Django](https://docs.djangoproject.com/en/5.0/)

This is a [decently descriptive article](https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8) that I used to set up the project infrastructure

Read these [docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction) to better understand how Django works