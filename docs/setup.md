Getting Started
===============

Getting the code
----------------

The most up-to-date version of this repository including all tutorial data can be downloaded locally using git. You can "get git" onto your local machine __[directly from the git website](https://git-scm.com/downloads)__, or it can be installed within a conda environment using `conda install -c conda-forge git`. Either way, once git is configured, you can download everything you need to run these examples with

```shell
git clone https://github.com/needham-michael/cmaq_visualization.git
```

This will create a directory called `/cmaq_visualization` on your local machine.

Preparing the python environment
--------------------------------

The `environment.yml` file includes instructions for recreating the same conda environment (named `cmaq_pyenv`) used to develop and run these notebooks. Assuming conda has been __[installed locally](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)__ and __[initialized](https://conda.io/projects/conda/en/latest/dev-guide/deep-dives/activation.html)__ for the user's shell, the environment can be recreated by running the following command from within the base directory

`conda env create -f environment.yml`

The environment can then be activated with

`conda activate cmaq_pyenv`

Adding the ipython kernel to Jupyter
------------------------------------

Once the environment has been created, Jupyter needs to be configured to execute the notebooks *using the environment.* This requires using the __[ipykernel](https://github.com/ipython/ipykernel)__ package, which was included in the `environment.yml` file. From the terminal window, run

`python3 -m ipykernel install --user --name=cmaq_pyenv --display-name="Python3 (cmaq_pyenv)"`

Installing the project package
------------------------------
You will need to install the python utility functions into the `cmaq_pyenv` conda environment by running `pip install .` from the `/cmaq_visualiztion` folder (make sure that the correct conda environment is selected). 

If you plan to make your own changes to those utility functions (or add new ones), change that command to `pip install . -e` so that it is *editible*. 

!!! note
    If you do make edits to the utility functions (or add your own), you may also want to add the following __[cell magic comamands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)__ to the notebooks: `%load_ext autoreload`, and `%autoreload 2`, which can just be placed in a cell at the top of the notebook and run once. 
    
    This will allow you to make changes to the source code and have those changes immediately become available within the Jupyter notebook without the need to restart the kernel.