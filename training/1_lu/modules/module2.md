# Module 2 - Introduction to LUCIS-OPEN Tools for QGIS

**What will you learn from this module?**

- Get to know the function of each LUCIS-OPEN Tools for QGIS,
- Be familiar with the parameters of Tools,
- Process data with appropriate Tools.

## 1. GIS Datasets

- The table below lists the GIS datasets used for this module.
- They can be found within the downloaded _zip_ folder from the previous
  section at `GALUP-master -> training -> 1_lu -> datasets`.

| ID | File Name   | Data Format | Type    | Description  |
|----|------------|-------------|---------|-----------------------------|
| 1  | Gh_260_MMDA.shp                  | vector      | polygon | Districts of Ghana              |
| 2  | population_gha_2018-10-01.tif    | raster      | tiff    | Population of Ghana in 2018     |
| 3  | THLD_poly.shp                 | vector      | polygon | Integrated Decision Units in THLD District     |
| 4  | osm2020_allrds_THLD.shp       | vector      | line    | Primary and secondary roads in THLD District                                             |
| 5  | RailwayLine.shp             | vector      | line    | Railway line in Ghana                                             |
| 6  | Hydro.shp             | vector      | line    | Underground water veins in THLD District                                            |
| 7  | Health_Facilities.shp       | vector      | point    | Health facilities in THLD District                                           |
| 8  | Education_Facilities.shp       | vector      | point    | Education facilities in THLD District                                         |
| 9  | PointOfInterest.shp               | vector      | point    | Point of interest in Ghana                                           |
| 10  | SD5_15.tif                    | raster      | tiff    | [Soil PH 0-5](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/a3364e47-9229-4a6d-aed2-487fd7e4dccc)                  |

## 2. Get to Know LUCIS-OPEN Tools for QGIS

### 2.1 Density of Line Features

This tool calculates a magnitude-per-unit area from polyline features that fall within each input vector feature _or_ within a radius around each input vector
feature.

1. **Tool Parameters:**<br>
   For details about parameters settings of this tool, please check
   [here](https://github.com/SERVIR-WA/GALUP/wiki/Tools#density-of-line-features).
2. **Application Scenario:**<br>
   _Density of Line Features_ is used to calculate the line density in
   a polygon (i.e., calculating the total length of lines in a polygon feature
   divided by its area).
   Only the portion of a line within the neighborhood (a polygon feature or a
   radius around a polygon feature) is considered when calculating the density.
   If no lines fall within the neighborhood at a particular polygon, that
   polygon is assigned "[Null](https://www.cadlinecommunity.co.uk/hc/en-us/articles/360013744338-QGIS-NULL-Values#:~:text=By%20default%2C%20when%20you%20browse,will%20show%20a%20NULL%20value.)".

   This tool is often used to calculate the density of linear features, such as
   roads and rivers.
   In the following example, we use this tool to calculate the density of
   underground water veins in the THLD area.

   The figures below show the parameter setting of the tool and the output.<br>
   > :pushpin: Check the details of an image:<br>
   > If you can't see the image clearly, click on the image to view it in a
   > new page, which will show the image in its original size.

|          Parameter Setting         |    Output    |
|:------------------------------------------:|:------------------------------------------:|
| ![PS1](../../../images/PrameterSetting/LineDensity.png) | ![am1](../../../images/ApplicationMaps/LineDen2.png) |

### 2.2 Distance to Point Features

Calculates the distance between the input vector features and their nearest point feature.

1. **Tool Parameters:**<br>
    For details about parameters settings of this tool, please check [here](https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-point-features).
2. **Application Scenario:**<br>
    _Distance to Point Features_ is often used to find the nearest location (point feature) around a polygon feature. For example, this tool can be used to find the nearest school or the nearest hospital around each residential area.

    In the following example, we use the Distance to Point Features tool to calculate the distance between each polygon in THLD area and the nearest education facility.

    The figures below shows the parameter setting of the tool and the output.

|          Parameter Setting         |    Output    |
|:------------------------------------------:|:------------------------------------------:|
| ![PS2](../../../images/PrameterSetting/DistoPoint.png) | ![am2](../../../images/ApplicationMaps/DistoP2.png) |

### 2.3 Reclassify Field

Reclassify a field in the input table based on predefined rules and store the translated values in a new field.

1. **Tool Parameters:**<br>
    For details about parameters settings of this tool, please check [here](https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field).
2. **Application Scenario:**<br>
    _Reclassify Field_ reclassifies or changes the values of the feature to alternative values. For example, a vector of soil type may be assigned values of 1 to 10 to represent erosion potential. This tool is useful when you are trying to do a suitability model, it allows you to assign new values to different evaluation indicators under a same scoring system on which the final weighting step will be based.

    Recall that, in Exercise 2 of Module 1, we calculated the population density of Ghana by district in 2018. In the following example, in order to know the population density level of the Ghana by district in 2018, we use the Reclassify Field tool to reclassify the population density of the Ghana by district in 2018 according to the criteria that old values: 7-60, 60-100, 100-186, 186-490, and 490-18804 will be assigned new values: 1, 2, 3, 4, 5, respectively.

    The figures below shows the parameter setting of the tool and the output.

|          Parameter Setting         |    Output   |
|:------------------------------------------:|:------------------------------------------:|
| ![PS3](../../../images/PrameterSetting/Reclassify.png) | ![am3](../../../images/ApplicationMaps/Reclassify2.png) |
### 2.4 Spatial Join

1. **Summary:**<br>
  This tool join attributes from the join features to the target
  features based on specified spatial relationship.

2. **Parameters:**<br>
  For the parameters setting for Spatial Join tool, please click [here](https://github.com/SERVIR-WA/GALUP/wiki/Tools#spatial-join).

3. **Application Scenario:**<br>
  _Spatial Join_ evaluates spatial relationships (i.e., _**Intersect**_,
  _**Contains**_, _**Within**_) between features in the **Target Layer** and
  the **Join Layer**.
  The tool joins the columns from the **Join Layer** to the **Target Layer** if
  any two features, one from each layer (we call them "matched" for each
  other), satisfy the specified spatial relationship.<br>
  When there are multiple "matched" features in the **Join Layer**, you can
  choose either _**Join one to many**_ or _**Join one to one**_.
  If _**Join one to many**_ is selected, features in the **Target Layer**
  will be duplicated multiple times (as many as the number of "matched"
  features) to combine with each "matched" feature in the **Join Layer**.
  On the contrary, if  _**Join one to one**_ is selected, all "matched"
  features in the **Join Layer** will be aggregated, and then combined with
  a target feature.<br>
  In the following example, we choose the _**Join one to one**_ option to find
  out the _**count**_ (number of records) of points of interest (tourism)
  within each District Assembly of Ghana.

|         Parameters setting     |       Output        |
|:---------------------------------------:|:---------------------------------------------:|
| <img src="../../../images/m2_SpatialJoin/ParametersSetting.png" alt= "Add data to Map Canvas" width="600">   |  <img src="../../../images/m2_SpatialJoin/Output2.png" alt= "Add data to Map Canvas" width="580">   |

### 2.5 Zonal Statistics

1. **Summary:**<br>
  This tool calculate statistics on values of raster within the
  zones of another dataset.

2. **Parameters:**<br>
  For the parameters setting for Zonal Statistics tool, please click [here](https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics).

3. **Applications:**<br>
  _Zonal Statistics_ calculates statistics for specified zones based on values from another dataset (rasater dataset). 
  This tool calculates the **mean**, **median**, **sum**, **minimum**,
  **maximum**, **standard deviation**, **majority**, **minority**, **unique**, or **range** in each zone.
  In the following example, we use this tool to show the population size
  in each district of Ghana.

|         Parameters setting     |       Output        |
|:---------------------------------------:|:---------------------------------------------:|
| <img src="../../../images/m2_ZonalStatistics/ParametersSetting.png" alt= "Add data to Map Canvas" width="565">   |  <img src="../../../images/m2_ZonalStatistics/Output2.png" alt= "Add data to Map Canvas" width="530">   |

### 2.6 Select by Location

1. **Summary:**<br>
This tool can select part of the input Layer based on its spatial
relationship with the selecting layer.

2. **Parameters:**<br>
For the parameters setting for Select by Location tool, please click [here](https://github.com/SERVIR-WA/GALUP/wiki/Tools#select-by-location).

3. **Applications:**<br>
_Select By Location_ allows you to select features from **Input layer** based on their location relative to features in **Selection layer**.
In the following example, we use this tool to select all the districts attached with the 100-kilometer buffer of the railway line in Ghana.

|         Parameters setting     |       Output        |
|:---------------------------------------:|:---------------------------------------------:|
| <img src="../../../images/m2_SelectbyLocation/ParametersSetting.png" alt= "Add data to Map Canvas" width="570">   |  <img src="../../../images/m2_SelectbyLocation/Output2.png" alt= "Add data to Map Canvas" width="521">   |


## 3. Exercises and Post

- Please complete the [Exercise 1](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise1.md). # Density of Line (road density)
- Please complete the [Exercise 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise2.md). # Distance to Point Features (distance to health facility)
- Please complete the [Exercise 3](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise3.md). # Select by location  (within the 5 miles buffer of the education facility)
- Please complete the [Exercise 4](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise4.md). # Reclassify Field & Zonal Statistics (a kind of crops, reclassify soil PH)