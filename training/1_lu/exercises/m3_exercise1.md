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

_Land Condition_ is a sub-objective of the physical objective.

_Land Conditiony_ model aims to evaluate the capacity of land to respond to
rain and produce useful pasture by measuring the slope percent and land cover
condition.
In term of land cover, we wish to select out the suitable land while protect
existing forest.
We list following table to indicate which land cover is more suitable to grow
row crops.
|      |  Land Cover Types                     | Suitability  |
|------|---------------------------------------|--------------|        
|  1   |  Open forest, unknown                 |      5       |
|  2   |  Closed forest, unknown               |      1       |
|  3   |  Closed forest, evergreen broad leaf  |      1       |
|  4   |  Open forest, evergreen broad leaf    |      5       |
|  5   |  Shrubs                               |      7       |
|  6   |  Urban / built up                     |      1       |
|  7   |  Herbaceous vegetation                |      9       |
|  8   |  Closed forest, deciduous broad leaf  |      1       |
|  9   |  Herbaceous wetland                   |      3       |

note: lands with higher suitability score are more suitable to grow
row crops. 

According to research<sup>[1]()</sup>, slope percent could be attributed into 5
classes in following range:

| Slope (percent rise) | Suitability |
|----------------------|-------------|
| 0-2                  | 9           |
| 2-8                  | 7           |
| 8-15                 | 5           |
| 15-25                | 3           |
| 25-45                | 1           |

note: lands with higher suitability score are more suitable to grow
row crops. 

## 3. GIS Dataset

You should use the following data to finish this exercise:
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`
- _Slope\_Percent.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Slope_Percent`
- _iSDA\_MGRS.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Ghana Land Cover 2019`

In THLD district, different land cover types are represented by numbers in
Dataset. The table below lists all land cover types collected in 2019:

| Value|  Land Cover Types                     |
|------|---------------------------------------|
|  1   |  Open forest, unknown                 |
|  2   |  Closed forest, unknown               |
|  3   |  Closed forest, evergreen broad leaf  |
|  4   |  Open forest, evergreen broad leaf    |
|  5   |  Shrubs                               |
|  6   |  Urban / built up                     |
|  7   |  Herbaceous vegetation                |
|  8   |  Closed forest, deciduous broad leaf  |
|  9   |  Herbaceous wetland                   |

## 4. Instruction

|          Model         |
|------------------------------------------|
| ![LCM](../../../images/Model%20Map/Land_Condition.svg) |

1. Click [image] in **_Processing Toolbox_** and choose `Create New Model...`.
2. Click **_Model Properties_** and type _Land Condition_ in **Name** and
_Physical_ in **Group**.
3. Add _Vector Layer_, name it **AInput layer**, and choose _Polygon_ in **Geometry type**.
4. Add Raster Layer and name it **BLand Cover**.
4. Add _Matrix_, name it **CAdd Value for Land Cover**, and then set table as
   following:

   |     |   1  |   2  |   3     |
   |-----|------|------|---------|
   |  1  |   1  |   2  |   5     |
   |  2  |   2  |   3  |   1     |
   |  3  |   3  |   4  |   1     |
   |  4  |   4  |   5  |   5     |
   |  5  |   5  |   6  |   7     |
   |  6  |   6  |   7  |   1     |
   |  7  |   7  |   8  |   9     |
   |  8  |   8  |   9  |   1     |
   |  9  |   9  |  10  |   3     |
5. Remove all prefix **A**, **B**, **C** in name.
6. Click **_Algorithms_**, locate the
   **<ins>Reclassify by table</ins>** tool under **_Raster analysis_**.
7. Add the tool and rename it **Add Value for Land Cover**, then set
   parameters as follows (click advanced parameters):
   <ol type="a">
      <li><b>Raster layer</b>: Land Cover,</li>
      <li><b>Band number</b>: 1,</li>
      <li><b>Reclassification table</b>: Add Value for Land Cover,</li>
      <li><b>Output no data value</b>: -9999,</li>
      <li><b>Range boundaries</b>: min <= value < max,</li>
      <li><b>Use no data when no range matches value</b>: Yes,</li>
      <li><b>Output data type</b>: Float32,</li>
      <li>leave all other parameters as default.</li>
   </ol>
8. Click **_Algorithms_**, locate the
   **<ins>Zonal Statistics</ins>** tool under **_Scripts_**
   <img src="../../../images/M2E1/processingScript.svg" alt= "scripts" width="20">.
9. Add the tool and rename it **Add LC to Polygon**, then set
   parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: Input layer,</li>
      <li><b>Raster layer</b>: 'Reclassified raster' from algorithm 'Add Value for Land Cover',</li>
      <li><b>Types of statistics</b>: mean,</li>
      <li><b>Output column prefix</b>: LC,</li>
      <li><b>No data value</b>: -9999,</li>
      <li>leave all other parameters as default.</li>
   </ol>
10. Add _Raster Layer_ and name it **DSlope**.
11. Add two _String_, name one as **EParameters for LCC**, and then set **Default value**
   as: 0-2,2-8,8-15,15-25,25-45;
   and name another one as **FLCC Classes**, and then set **Default value**
   as: 9,7,5,3,1.
12. Remove  **D**, **E**, **F** in name.
13. Click **_Algorithms_**, locate the
   **<ins>Zonal Statistics</ins>** tool under **_Scripts_**
   <img src="../../../images/M2E1/processingScript.svg" alt= "scripts" width="20">.
14. Add the tool and rename it **Add Slope to Polygon**, then set
   parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: 'Output layer' from algorithm 'Add LC to Polygon',</li>
      <li><b>Raster layer</b>: Slope,</li>
      <li><b>Types of statistics</b>: mean,</li>
      <li><b>Output column prefix</b>: Slp,</li>
      <li><b>No data value</b>: Not set,</li>
      <li>leave all other parameters as default.</li>
   </ol>
15. Click **_Algorithms_**, locate the
   **<ins>Reclassify Field</ins>** tool under **_Scripts_**
   <img src="../../../images/M2E1/processingScript.svg" alt= "scripts" width="20">.
16. Add the tool and rename it **Rec Slope Percent**, then set
   parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: 'Output layer' from algorithm 'Add Slope to Polygon',</li>
      <li><b>Field to reclassify</b>: Health_Facilities,</li>
      <li><b>Old values</b>: Parameters for LCC,</li>
      <li><b>New values</b>: LCC Classes,</li>
      <li><b>No data value</b>: 255,</li>
      <li><b>Output column name</b>: Slp_r,</li>
      <li>leave all other parameters as default.</li>
   </ol>
17. Add _String_, name it as **GWeight by LC Slope**, and then set **Default value**
   as: 0.5,0.5;
18. Remove  **G** in name.
19. Click **_Algorithms_**, locate the
   **<ins>Weighted Sum of Fields</ins>** tool under **_Scripts_**
   <img src="../../../images/M2E1/processingScript.svg" alt= "scripts" width="20">.
20. Add the tool and rename it **Weighted Sum LC & Slp**, then set
   parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: 'Output layer' from algorithm 'Rec Slope Percent',</li>
      <li><b>Fields</b>: LC_mean;Slp_r,</li>
      <li><b>Weights</b>: Weight by LC Slop,</li>
      <li><b>Output field name</b>: LandCondit,</li>
      <li><b>Output layer</b>: rcrp_LandCondition,</li>
      <li>leave all other parameters as default.</li>
   </ol>
21. Sava the model in a folder you can find.
22. Locate _Slope\_Percent.tif_, _iSDA\_MGRS.tif_, and _THLD\_poly.shp_ in the **_Browser Panel_** and add them to **_Map Canvas_**.
23. In the **_Processing Toolbox_** panel, locate the
   **<ins>Land Condition</ins>** model under **_Models_** -> **_Physical_**.
24. **Double Click** to open the model and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: THLD_poly,</li>
      <li><b>Land Cover</b>: iSDA_MGRS,</li>
      <li><b>Slope</b>: Slope_Percent,</li>
      <li>leave all other parameters as default.</li>
25. Click **Run**.
26. Now let's setup the **Symbology** of the output layer.
   Open the
   <img src="../../../images/M2E1/symbology.svg" alt= "AttrTbl" width="20">
   Symbology tab from the **_Layer Properties_** window.
   Select the ![graduated](../../../images/M2E1/rendererGraduatedSymbol.svg)
   Graduated style.
   Specify the _LandCondit_ field as **Value**, then choose the _Reds_ color ramp
   with 5 classes. Click **Apply**.
27. Click **OK** on the **Symbology** tab.
28. Create a _Layout_, then add _Legend_, _Scale bar_, and _North Arrow_ to the
   layout.
29. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here]().
- Now you have completed all exercises. Please go back to
  [Module 3]() to turn in them.

## 6.Reference

1. Scopesi, C., Olivari, S., Firpo, M., Scarpellini, P., Pini, S., & Rellini, I. (2020). Land capability classification of Vernazza catchment, Cinque Terre National Park, Italy. Journal of Maps, 16(2), 357-362.
