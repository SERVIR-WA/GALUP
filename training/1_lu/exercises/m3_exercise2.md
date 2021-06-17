# Module 2 - Exercise 4

## 1. Skills Practices

This exercise will practice:

- [Land Condition Model](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#land-condition-physical)

## 2. Description

_Land Condition Model_ aims to evaluate the capacity of land to respond to rain
and produce useful pasture.
The assessment of land condition includes the evaluation of slope percent and
land cover condition.
In the first step, this model 




## 3. GIS Dataset

You should use the following data to finish this exercise:
- _SD5\_15.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Soil pH 5_15 in THLD District`
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`

## 4. Instruction

1. Locate _SD5\_15.tif_ and _THLD\_poly.shp_ in the _Browser Panel_ and add them to _Map Canvas_.
2. Open _Zonal Statistics_ tool.
3. Set _THLD\_poly.shp_ as **Input layer** and _SD5\_15.tif_ as **Raster layer**.
4. Type _mean_ in **Types of statistics** and then give an appropriate
name for **Output column prefix**.
5. Choose drop down list in **Output layer** and select `Save to Files...`, so you can save the output shapefile to the files you frequently use.
6. **Run** _Zonal statistics_ tool.
7. Open _Reclassify Field_ tool.
8. Set the output shapefile from the Zonal Statistics tool as **Input layer** and the output column as **Field to reclassify**.
9. Type _40-50, 50-55, 55-65_ in **Old values**.
10. Type _1, 2, 3_ in **New values**.
11. Set _0_ for No data value and then give an appropriate name for
   **Output column prefix**.
12. Choose drop down list in **Output layer** and select `Save to Files...`, so you can save the output shapefile to the files you frequently use.
13. **Run** _Reclassify Field_ tool.
14. Choose _Categorized_ symbology and choose the _Greens_ color ramp to
render the the Output column from _Reclassify Field_ tool.
15. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
16. Export as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/SoilIndex.pdf).
- Now you have completed all exercises. Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#4-exercises) to turn in them.


















#### **Tools used in the model**
1. [Reclassify Field](https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field)
2. [Reclassify by table](https://docs.qgis.org/3.4/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html#reclassify-by-table)
3. [Weight Sum of Fields](https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields)
4. [Zonal Statistics](https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics)
#### **_Input parameters_**
  1. Input layer: Input vector layer.
  2. Land cover: Input raster layer. Land cover is usually comprised of lands with different woodland conditions and built up area.
  3. Add value for land cover: Add new value for different land cover types in table.Table is fixed as 3 row table. Row 1 represents the number of land cover types. Row 2 is the number of land cover types plus 1. Row 3 represents the value the land cover types will be given. Different columns represent different types of land cover.
  4. Slope: Input slope raster data.
  5. Parameters for LCC: Land Capability Classification is defined as a system of grouping land into various classes based on inherent limitations imposed on sustained use by soil attributes, topography, drainage and climate. Slope percent could be attributed into 5 classes in following range<a href="#ref1"><sup>[1]</sup></a>:
        | Slope (percent rise) | Suitability |
        |----------------------|-------------|
        | 0-2                  | 9           |
        | 2-8                  | 7           |
        | 8-15                 | 5           |
        | 15-25                | 3           |
        | 25-45                | 1           |
  6. LCC Classes: Defined Classes respond to the range of Slope percent.
  7. Weight by LC Slope: Weight the suitability of land cover condition for agriculture activities and slope percent. Weight should be separated by comma.
#### **Output**
`rcrp_LandCondition` (output vector layer for land condition).





## 6.Reference

1. Ernest, D. (n.d.). How to Grow Yams. https://www.diynetwork.com/how-to/outdoors/gardening/how-to-grow-yams
2. O'SULLIVAN, J. N. (2008). Root distribution of yam (Dioscorea alata) determined by strontium tracer. Experimental Agriculture, 44(2), 223.
