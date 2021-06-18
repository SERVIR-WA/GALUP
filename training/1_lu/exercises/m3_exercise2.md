# Module 3 - Exercise 2

## 1. Skills Practiced

This exercise will practice:

- **QGIS Graphical Modeler**
- **Market Model**

## 2. Description

Market is a sub-objective of the economic condition objective. The reason that we set this as a sub-objective is that the distance to market can affect the row crops selling and transportation fee.

**Market model** aims to evaluate the suitability of IDUs for planting row crops by measuring the distance between the IDU and the market places (i.e., the distance to large city, middle city, and small city).

## 3. GIS Dataset

You should use the following data to finish this exercise:
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`
- _LargeCity\_pt.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Large_City_Point`
- _MiddleCity\_pt.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Middle_City_Point`
- _SmallCity\_pt.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Small_City_Point`

## 4. Instruction

![marketmodelmap](../../../images/Model%20Map/Market.svg)

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

