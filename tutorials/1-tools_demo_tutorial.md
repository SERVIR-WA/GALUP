# Tools Demo Tutorial

## Zonal Statistics:

Zonal statistics is a tool used to calculate statistics on values of raster within the zones of vector layer.

***Step 1 -Choose Input layer and Raster layer***

This tool can help us to calculate statistics on raster data within a vector zone. Here, we assume we want to know the average of slope percent in each polygon zone. Here are vector (THLD_poly) and raster layers (Slop_PreWM) we need:
![demo1_raster_data](https://github.com/chjch/lucis_qgis/blob/master/images/demo1_raster_data.png)
![demo1_vector_data](https://github.com/chjch/lucis_qgis/blob/master/images/demo1_vector_data.png)

|          Vector layers (THLD_poly)         |    Raster layers (Slop_PreWM)    |
|:------------------------------------------:|:------------------------------------------:|
| ![grayscale](images/demo1_raster_data.png) | ![rgb_composite](images/demo1_vector_data.png) |


***Step 2 -Open the Zonal Statistics Tool Interface***

After we input the vector layer and raster layer, we need to choose an appropriate function. In this case, we need to calculate the average of slope percent, therefore, we choose 'mean' function to calculates the average of all cells in the value raster that belong to each vector zone. Then we name the output column prefix (Slp).

|               Choose function              |             Output name                   |
|:------------------------------------------:|:------------------------------------------:|
| ![demo1_function_choose](images/demo1_function_choose.png) | ![demo1_name_output](images/demo1_name_output.png) |


***Step 3 -Check the result***

After we processing the tools, we have a new column in output vector layer (Slp_mean). We demonstrate graduated change of slope percent in each polygon.

|               Output table              |             Change of slope                   |
|:------------------------------------------:|:------------------------------------------:|
| ![demo1_result](images/demo1_function_choose.png) | ![demo1_result_present](images/demo1_name_output.png) |
