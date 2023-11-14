# Module 3 - Exercise 1

## 1. Skills Practiced

This exercise will practice:

- **QGIS Graphical Modeler**
- **Land Condition Model**

The Landscape Condition model consists of the following tools:

1. [Reclassify Field](https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field)
2. [Reclassify by table](https://tinyurl.com/4axm4775)
3. [Weight Sum of Fields](https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields)
4. [Zonal Statistics](https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics)

## 2. Modeling Landscape Condition for Row Crops Farming

### 2.1 Model methodology

The _Landscape Condition_ model evaluates land capacity in terms of
(1) **slope** and (2) **land cover**.
An agriculture parcel's slope affects its capacity of retaining rainwater as
well as the level of difficulty for planting and harvesting.
According to Scopesi et al. (2020)<sup><a href="#ref1">1</a></sup>,
**slope percent** can be classified into **5** categories:

| Slope (percent rise) | Suitability |
|----------------------|-------------|
| 0-2                  | 9           |
| 2-4                  | 7           |
| 4-6                  | 5           |
| 6-9                  | 3           |


From the land cover's perspective, it is important that agricultural
activities are not in conflict with existing built-up areas and conserved
forests.
Given the above considerations and how difficult it can be converted for row
crops farming, the suitability scores for each land cover are listed as
follows.

<a id="modis"></a>
| value |  Land Cover Types                     | Suitability |
|-------|---------------------------------------|-------------|
|  1    |  Open Herbaceous Vegetation           |      9      |
|  2    |  Cropland                             |      9      |
|  3    |  Built-up                             |      1      |
|  4    |  Water Bodies Seasonal                |      1      |
|  5    |  Open Herbaceous Wetland              |      1      |
|  6    |  Closed Woodland                      |      5      |
|  7    |  Closed Bushland                      |      5      |
|  8    |  Sparse Forest/Woodland               |      9      |
|  9    |  Sparse/Open Bushland/Shrubs          |      9      |
|  10   |  Open Woodland/Bushland               |      9      |
|  11   |  Open Bushland/Shrubs                 |      7      |

### 2.2 Model Datasets

The following datasets are used in the landscape condition model:

- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`
- _Slope\_Percent.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Slope_Percent`
- _iSDA\_MGRS.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Ghana Land Cover 2019`

<sup>*</sup> Note:
The land cover data used in this exercise is the Collection 6 of Moderate
Resolution Imaging Spectroradiometer (MODIS)<sup><a href="#ref2">2</a></sup>.
For details of the classification please check the above
<a href="#modis">tabel</a>.

## 3. Instruction

![LCM](../../../img/qgm/model/Land_Condition.svg)

### 3.1 Build the model

1. Click
   <img src="../../../img/gui/icon/processingModel.svg" alt= "Model" width="20">
   in **_Processing Toolbox_** and choose `Create New Model...`.
2. Click **_Model Properties_** and type _Landscape Condition_ in **Name** and
   _Physical_ in **Group**.
3. Add a *Vector Layer* [input](https://tinyurl.com/qgis-gm-input), and name
   it **1_Input layer**, and choose _Polygon_ in **Geometry type**.
   > :bulb: **Why adding a prefix to the input element**<br>
   > In  QGIS 3.10.8, Model Dialogs display *input* elements in a sequence that
   > is based on their first character's order in the
   > [ASCII table](http://www.asciitable.com/).
   > So, to display inputs in the desired order, we need to add a number as a
   > prefix, e.g., "1_", in front of the input element's name.
4. Add a *Raster Layer* input, and name it **2_Land Cover**.
5. Add a _Matrix_ input, and name it **3_Add Value for Land Cover**, and then
   set table as following:
   <img src="../../../img/gui/window/m3_e1_Matrix.png" alt= "Matrix" width="400">
6. Remove all prefix **1_**, **2_**, **3_** in name.
   <img src="../../../img/qgm/algtbl/m3_e1_landscapecondition.svg" alt= "Toolsettings" width="1000">
7. Click **_Algorithms_**, Add the **<ins>Reclassify by table</ins>** tool
   under **_Raster analysis_**, and rename it **Add Value for Land Cover**,
   then set parameters as it shows in table (click advanced parameters).
8. Add the **<ins>Zonal Statistics</ins>** tool under **_Scripts_**
   <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">,
   and rename it **Add LC to Polygon**, then set parameters.
9.  Add _Raster Layer_ and name it **4_Slope**.
10. Add two _String_, name one as **5_Parameters for LCC**, and then set
    **Default value** as: 0-2,2-8,8-15,15-25,25-45; and name another one as
    **6_LCC Classes**, and then set **Default value** as: 9,7,5,3,1.
11. Remove all prefix **4_**, **5_**, **6_** in name.
12. Add the **<ins>Zonal Statistics</ins>** tool under **_Scripts_**
    <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">,
    and rename it **Add Slope to Polygon**, then set parameters.
13. Add the **<ins>Reclassify Field</ins>** tool under **_Scripts_**
    <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">,
    and rename it **Rec Slope Percent**, then set parameters.
14. Add _String_, name it as **7_Weight by LC Slope**, and then set
    **Default value** as 0.5,0.5 which suggests **land cover** and **slope**
    are equally important.
15. Remove prefix **7_** in name.
16. Add the **<ins>Weighted Sum of Fields</ins>** tool under **_Scripts_**
    <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">,
    and rename it **Weighted Sum LC & Slp**, then set parameters.
17. **Save** the model in a desired location.

### 3.2 Run the model and visualize the result

1. Locate _Slope\_Percent.tif_, _iSDA\_MGRS.tif_, and _THLD\_poly.shp_ in
   the **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   <ins>**Landscape Condition**</ins> model.
3. **Double Click** to open the model and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: THLD_poly,</li>
      <li><b>Land Cover</b>: iSDA_MGRS,</li>
      <li><b>Slope</b>: Slope_Percent,</li>
      <li>leave all other parameters as default.</li>
   </ol>
4. Click **Run**.
5. Now let's setup the **Symbology** of the output layer.
   Open the
   <img src="../../../img/gui/icon/symbology.svg" alt= "AttrTbl" width="20">
   Symbology tab from the **_Layer Properties_** window.
   Select the ![graduated](../../../img/gui/icon/rendererGraduatedSymbol.svg)
   Graduated style.
   Specify the _LandCondit_ field as **Value**, then choose the _Reds_ color
   ramp with 5 classes. Click **Apply**.
6. Click **OK** on the **Symbology** tab.
7. Create a _Layout_, then add _Legend_, _Scale bar_, and _North Arrow_ to the
   layout.
8. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/LandConditionMap.pdf).
- Please go back to [Module 3](https://tinyurl.com/yn9hy6ca) to complete the
  second exercise.

## 6.Reference

1. <a id="ref1"></a>Scopesi, C., Olivari, S., Firpo, M., Scarpellini,
   P., Pini, S., & Rellini, I. (2020). Land capability classification of
   Vernazza catchment, Cinque Terre National Park, Italy. Journal of Maps,
   16(2), 357-362.
2. <a id="ref2"></a>Sulla-Menashe, D., & Friedl, M. A. (2018). User guide to
   collection 6 MODIS land cover (MCD12Q1 and MCD12C1) product.
   USGS: Reston, VA, USA, 1-18.
