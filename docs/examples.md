Examples
========

* __[1) Minimal CMAQ Plotting Example](./examples/01_minimal_cmaq_plotting_example.ipynb)__:  Generate simple coordinate-aware maps of hourly Ozone and PM2.5 concentrations from a CMAQ simulation on the 36US3 grid.

* __[2) Basic Analysis of hr2day output](./examples/02_hr2day_output_analysis_example.ipynb)__: Generate maps and timeseries plots of the daily maximum of 8-hour average ozone (MDA8O3) with additional colorbar customizations to highlight the value of 0.070 ppm, which is important for the __[primary 8-hour NAAQS](https://www.epa.gov/criteria-air-pollutants/naaqs-table)__ for ozone. This notebook utilizes output files that were generated using the __[CMAQ hr2day](https://github.com/USEPA/CMAQ/tree/main/POST/hr2day)__ postprocessing tool.

* __[3) Model-Data Comparison](./examples/03_model_monitor_comparison.ipynb)__: Download AQS in-situ air quality data using the __[pyRSIG](https://barronh.github.io/pyrsig/)__ package and compare to CMAQ hr2day output as in Example 2.

* __[4) Edits to Emission Files](./examples/04_cmaq_emission_inputs.ipynb)__: Demonstrate how to use __[xarray](https://docs.xarray.dev/en/stable/)__ to make changes to NO and NO2 fields from a 12US1 CMAQ emission files.

Auxiliary Examples
------------------

Auxiliary examples included for informational purposes but cannot be downloaded and run because they rely on data files which are too large / too numerous to include in the __[tutorial data](./examples/tutorial_data)__ folder.

* __[A1) Concat files](./examples/A1_concat_files.ipynb)__: Auxiliary example showing basic concatenation of files.

* __[A2) Download AQS data](./examples/A2_aqs_download_pyrsig.ipynb)__: Auxiliary example showing how to download AQS data that coincides with CMAQ output using __[pyRSIG](https://github.com/barronh/pyrsig)__. Also includes an example of plotting AQS monitor data on an interactive web map with __[folium](https://python-visualization.github.io/folium/latest/#)__.

* __[A3) Coordinate Transformations and Subsetting](./examples/A3_coordinate_transformation_subsetting.ipynb)__ : Auxiliary example showing how to manage data in different coordinate systems. Makes use of __[cartopy](https://scitools.org.uk/cartopy/docs/latest/)__ for coordinate reference systems, as well as __[geopandas](https://geopandas.org/en/stable/)__ and __[shapely](https://shapely.readthedocs.io/en/stable/manual.html)__ to manage points and polygons across coordinate systems.