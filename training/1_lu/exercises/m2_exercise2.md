# Module 2 - Exercise 2

## 1. Skills Practices

This exercise will practice:

- [Distance to Point Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#22-distance-to-point-features)

## 2. Description

The distance to health facilities in a district is one common measure of that area's accessibility to medical resources.
Twifo-Heman-Lower-Denkyira (THLD) district, we want to build a healthcare center to improve all Integrated Decision Units' (IDUs) accessibility to the medical resource.
In the first step of the healthcare center location selection, we need to find out those areas with relatively less access to health facilities by measuring the distances to those facilities.
In this exercise, we will visualize the distance to Health Facilities in the THLD district by using the [Distance to Point Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#22-distance-to-point-features) tool.

## 3. GIS Dataset

The following datasets are used in this exercises:

- _Health\_Facilities.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Health facilities in THLD District`
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`

## 4. Instruction

1. Locate _Health\_Facilities.shp_ and _THLD\_poly.shp_ in the **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   **<ins>Distance to Point Features</ins>** tool under **_Scripts_**
   <img src="../../../images/M2E1/processingScript.svg" alt= "scripts" width="20">.
3. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: THLD_poly,</li>
      <li><b>Point layer</b>: Health_Facilities,</li>
      <li><b>Distance method</b>: Euclidean,</li>
      <li><b>Output data type</b>: Float,</li>
      <li><b>Output column name</b>: HF_Dis,</li>
      <li><b>Output shapefile</b>: HFDisMap.shp,</li>
      <li>leave all other parameters as default.</li>
   </ol>
4. Click **Run**.
5. Now let's setup the **Symbology** of the output layer.
   Open the
   <img src="../../../images/M2E1/symbology.svg" alt= "AttrTbl" width="20">
   Symbology tab from the **_Layer Properties_** window.
   Select the ![graduated](../../../images/M2E1/rendererGraduatedSymbol.svg)
   Graduated style.
   Choose the [_Natural Breaks (Jenks)_](http://wiki.gis.com/wiki/index.php?title=Jenks_Natural_Breaks_Classification&oldid=763049).
   Specify the _HF\_Dis_ field as **Value**, then choose the _Reds_ color ramp
   with 5 classes. Click **Apply**.
6. Click **OK** on the **Symbology** tab.
7. Create a _Layout_, then add _Legend_, _Scale bar_, and _North Arrow_ to the
   layout.
8. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/DistanceToHF.pdf).
- Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#7-exercises-and-post-training-survey) to complete the third exercise.
