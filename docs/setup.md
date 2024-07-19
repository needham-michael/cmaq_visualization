Setup
=====

Getting the code
----------------

The most up-to-date version of this repository including all tutorial data can be downloaded locally with

```shell
git clone https://github.com/needham-michael/cmaq_visualization.git
```

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
You can install the source code from this repository into the `cmaq_pyenv` conda environment by running `pip install .` (make sure that the correct conda environment is selected). If you plan to make changes to the source code, change that command to `pip install . -e` so that it is *editible*. You may also want to add the following __[cell magic comamands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)__ to the notebooks: `%load_ext autoreload`, and `%autoreload 2`.

These can just be placed in a cell at the top of the notebook and run once. This will allow you to make changes to the source code and have those changes immediately become available within the Jupyter notebook without the need to restart the kernel.