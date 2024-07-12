CMAQ Visualization Examples
==============

A series of short examples of generating visualizations of output from the US EPA __[Commmunity Multiscale Air Quality Model (CMAQ)](https://github.com/USEPA/CMAQ/tree/main)__ using tools from the python ecosystem. 

<div class="alert alert-block alert-warning">
For configuration / install instructions, see the primary <b><a href="../README.md">README</a></b> for this repository. Sample data files for these notebooks are included in the <b><a href="./tutorial_data">tutorial data</a></b> folder.
</div>

## Examples
1. __[Minimal CMAQ Plotting Example](./01_minimal_cmaq_plotting_example.ipynb)__:  Generate simple coordinate-aware maps of hourly Ozone and PM2.5 concentrations from a CMAQ simulation on the 36US3 grid.

2. __[Basic Analysis of hr2day output](02_hr2day_output_analysis_example.ipynb)__: Generate maps and timeseries plots of the daily maximum of 8-hour average ozone (MDA8O3) with additional colorbar customizations to highlight the value of 0.070 ppm, which is important for the __[primary 8-hour NAAQS](https://www.epa.gov/criteria-air-pollutants/naaqs-table)__ for ozone. This notebook utilizes output files that were generated using the __[CMAQ hr2day](https://github.com/USEPA/CMAQ/tree/main/POST/hr2day)__ postprocessing tool. 