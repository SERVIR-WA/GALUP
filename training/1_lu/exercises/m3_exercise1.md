# Module 3 - Exercise 1

## 1. Skills Practiced

This exercise will practice:

- **QGIS Graphical Modeler**
- **Land Condition Model**

The Land Condition model will use following tools:

1. [Reclassify Field](https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field)
2. [Reclassify by table](https://docs.qgis.org/3.4/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html#reclassify-by-table)
3. [Weight Sum of Fields](https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields)
4. [Zonal Statistics](https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics)

## 2. Description

Yam is an important staple food crop in Ghana and is produced throughout the
country.
In Twifo-Heman-Lower-Denkyira (THLD) district, the local government wants to
plan and develop new cropland to grow Yam.
Therefore, as a planner, we need to evaluate the suitability of land for
growing Yam.

The first step of our analysis aims to select out the area with a suitable
soil pH range.
Soil pH affects plant nutrient availability by controlling the chemical forms
of the different nutrients and influencing the chemical reactions they undergo.
Yam prefers the rich fertile soil with a pH ranged from 5.5 to 6.5<sup>[1]</sup>,
and the horizontal growth of its roots has been observed to occur within the
top 10 cm of soil<sup>[2]</sup>.
So, we will evaluate the land in THLD district by analyzing the Soil pH dataset in root depth ranged from 5 to 15 cm.

In this exercise, we will create a Soil pH index to evaluate the suitability
to grow Yam in THLD district by using the [Reclassify Field](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#23-reclassify-field) tool and [Zonal Statistics](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#25-zonal-statistics) tool.

## 3. GIS Dataset

You should use the following data to finish this exercise:
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`
- _Slope\_Percent.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Slope_Percent`
- _SD5\_15.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Soil pH 5_15 in THLD District`

## 4. Instruction

|          Model         |
|------------------------------------------|
| ![LCM](../../../images/Model%20Map/Land_Condition.svg) |

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

## 6.Reference

1. Ernest, D. (n.d.). How to Grow Yams. https://www.diynetwork.com/how-to/outdoors/gardening/how-to-grow-yams
2. O'SULLIVAN, J. N. (2008). Root distribution of yam (Dioscorea alata) determined by strontium tracer. Experimental Agriculture, 44(2), 223.
