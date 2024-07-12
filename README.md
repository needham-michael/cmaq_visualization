# Python Visualizations of CMAQ Output

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/astral-sh/ruff"><img alt="Code style: black" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
</p>

**Last Updated: 12 July 2024**

A series of short examples of generating visualizations of output from the US EPA __[Commmunity Multiscale Air Quality Model (CMAQ)](https://github.com/USEPA/CMAQ/tree/main)__ using tools from the python ecosystem. 

## Examples
All tutorials are included in the __[examples](./examples)__ folder. Prior to running the jupyter notebooks, ensure the python environment is correctly configured by following the steps below under __Setup__.


* __[1) Minimal CMAQ Plotting Example](./examples/01_minimal_cmaq_plotting_example.ipynb)__:  Generate simple coordinate-aware maps of hourly Ozone and PM2.5 concentrations from a CMAQ simulation on the 36US3 grid.

* __[2) Basic Analysis of hr2day output](./examples/02_hr2day_output_analysis_example.ipynb)__: Generate maps and timeseries plots of the daily maximum of 8-hour average ozone (MDA8O3) with additional colorbar customizations to highlight the value of 0.070 ppm, which is important for the __[primary 8-hour NAAQS](https://www.epa.gov/criteria-air-pollutants/naaqs-table)__ for ozone. This notebook utilizes output files that were generated using the __[CMAQ hr2day](https://github.com/USEPA/CMAQ/tree/main/POST/hr2day)__ postprocessing tool.

### Auxiliary Examples

Auxiliary examples included for informational purposes but cannot be downloaded and run because they rely on data files which are too large / too numerous to include in the __[tutorial data](./examples/tutorial_data)__ folder.

* __[A1) Concat files](./examples/A1_concat_files.ipynb)__: Auxiliary example showing basic concatenation of files.
* __[A2) Download AQS data](./examples/A2_aqs_download_pyrsig.ipynb)__: Auxiliary example showing how to download AQS data that coincides with CMAQ output using __[pyRSIG](https://github.com/barronh/pyrsig)__. Also includes an example of plotting AQS monitor data on an interactive web map with __[folium](https://python-visualization.github.io/folium/latest/#)__.

## Setup
### Preparing the python environment
The `environment.yml` file includes instructions for recreating the same conda environment (named `cmaq_pyenv`) used to develop and run these notebooks. Assuming conda has been __[installed locally](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)__ and __[initialized](https://conda.io/projects/conda/en/latest/dev-guide/deep-dives/activation.html)__ for the user's shell, the environment can be recreated by running the following command from within the base directory

`conda env create -f environment.yml`

The environment can then be activated with

`conda activate cmaq_pyenv`

### Adding the ipython kernel to Jupyter

Once the environment has been created, Jupyter needs to be configured to execute the notebooks *using the environment.* This requires using the __[ipykernel](https://github.com/ipython/ipykernel)__ package, which was included in the `environment.yml` file. From the terminal window, run

`python3 -m ipykernel install --user --name=cmaq_pyenv --display-name="Python3 (cmaq_pyenv)"`

### Installing the project package

You can install the source code from this repository into the `cmaq_pyenv` conda environment by running `pip install .` (make sure that the correct conda environment is selected). If you plan to make changes to the source code, change that command to `pip install . -e` so that it is *editible*. You may also want to add the following __[cell magic comamands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)__ to the notebooks: `%load_ext autoreload`, and `%autoreload 2`.

These can just be placed in a cell at the top of the notebook and run once. This will allow you to make changes to the source code and have those changes immediately become available within the Jupyter notebook without the need to restart the kernel.





