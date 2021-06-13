# Module 2 - Exercise 4

## 1. Skills Practices

This exercise will practice:

- [Reclassify Field](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#23-reclassify-field)
- [Zonal Statistics](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#25-zonal-statistics)

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
- _SD5\_15.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Soil pH 5_15 in THLD District`
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`

## 4. Instruction

1. Locate _SD5\_15.tif_ and _THLD\_poly.shp_ in the **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   **<ins>Zonal Statistics</ins>** tool under **_Scripts_**
   <img src="../../../images/M2E1/processingScript.svg" alt= "scripts" width="20">.
3. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: THLD_poly,</li>
      <li><b>Raster layer</b>: SD5_15,</li>
      <li><b>Types of statistics</b>: mean,</li>
      <li><b>Output column prefix</b>: SpH,</li>
      <li><b>Output layer</b>: SpH.shp,</li>
      <li>leave all other parameters as default.</li>
   </ol>
4. Click **Run**.
5. Open **<ins>Reclassify Field</ins>** tool under **_Scripts_**
   <img src="../../../images/M2E1/processingScript.svg" alt= "scripts" width="20">.
6. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: SpH,</li>
      <li><b>Field to reclassify</b>: SpH_mean,</li>
      <li><b>Old values</b>: 40-50, 50-55, 55-65,</li>
      <li><b>New values</b>: 1, 2, 3,</li>
      <li><b>Output column name</b>: SpH_re,</li>
      <li><b>Output layer</b>: SpH_re.shp,</li>
      <li>leave all other parameters as default.</li>
   </ol>
7. Click **Run**.
8. Now let's setup the **Symbology** of the output layer (_SpH\_re.shp_).
   Open the
   <img src="../../../images/M2E1/symbology.svg" alt= "AttrTbl" width="20">
   Symbology tab from the **_Layer Properties_** window.
   Select the ![categorized](../../../images/M2E1/rendererCategorizedSymbol.svg)
   Categorized style.
   Specify the _SpH\_re_ field as **Value**, then choose the _Greens_ color ramp
   with 3 classes. Click **Apply**.
9. Click **OK** on the **Symbology** tab.
10. Create a _Layout_, then add _Legend_, _Scale bar_, and _North Arrow_ to the
   layout.
11. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/SoilIndex.pdf).
- Now you have completed all exercises. Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#7-exercises-and-post-training-survey) to turn in them.

## 6.Reference

1. Ernest, D. (n.d.). How to Grow Yams. https://www.diynetwork.com/how-to/outdoors/gardening/how-to-grow-yams
2. O'SULLIVAN, J. N. (2008). Root distribution of yam (Dioscorea alata) determined by strontium tracer. Experimental Agriculture, 44(2), 223.
