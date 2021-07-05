# Module 2 - Exercise 3

## 1. Skills Practiced

This exercise will practice:

- [Select by Location](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#26-select-by-location)

## 2. Description

Normally, the residential areas will be built near the education facilities so that it will be convenient for the education of children. In this exercise, we will help to find out the IDUs of THLD that are in proximity (within the 1 miles) to the education facility by using the [Select by Location](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#26-select-by-location) tool.

## 3. GIS Dataset

The following datasets are used in this exercises:
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`.
- _Education\_Facilities.shp_ at `GALUP-master -> training -> 1_lu -> datasets -> Education facilities in THLD District`.

## 4. Instruction

1. Locate _THLD\_poly.shp_ and _Education\_Facilities.shp_ in the
   **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   **<ins>Select by Location</ins>** tool under _Scripts_
   <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">
   and double click to open the tool.
3. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: THLD_poly,</li>
      <li><b>Selection layer</b>: Education_Facilities,</li>
      <li><b>Join option</b>: Within a distance,</li>
      <li><b>Within distance of selecting feature</b>: 1 mile,</li>
      <li><b>Output layer</b>: <i>EduProIDU.shp</i>,</li>
      <li>leave all other parameters as default.</li>
   </ol>
4. Click **Run**.
5. Set the symbology for the output polygons (match the color as the pdf file
   below).
6. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
7. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_maps/M2E3_EduProximity.pdf).
- Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#7-exercises-and-post-training-survey) to complete the fourth exercise.
