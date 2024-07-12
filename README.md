# Analysis of CMAQ output

*Created 5/29/2024*

Jupyter notebooks contained within this directory were developed using `python 3.12.3` using [conda](https://conda.io/projects/conda/en/latest/index.html) to install packages.

## Contents

```
├── README.md
├── environment.yml
├── examples
    ├── 01_minimal_cmaq_plotting_example_MN_2024-05-23.ipynb
    ├── 02_hr2day_output_analysis_example_MN_2024-06-04.ipynb
```

## Setup
### Preparing the python environment
The `environment.yml` file includes instructions for recreating the same conda environment (named `cmaq_pyenv`) used to develop and run these notebooks. Assuming conda has been [installed locally](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and [initialized](https://conda.io/projects/conda/en/latest/dev-guide/deep-dives/activation.html) for the user's shell, the environment can be recreated by running the following command from within the base directory

`conda env create -f environment.yml`

The environment can then be activated with

`conda activate cmaq_pyenv`

### Adding the ipython kernel to Jupyter

Once the environment has been created, Jupyter needs to be configured to execute the notebooks *using the environment.* This requires using the [ipykernel](https://github.com/ipython/ipykernel) package, which was included in the `environment.yml` file. From the terminal window, run

`python3 -m ipykernel install --user --name=cmaq_pyenv --display-name="Python3 (cmaq_pyenv)"`

### Installing the project package





