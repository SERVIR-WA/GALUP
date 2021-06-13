# Module 2 - Exercise 1

## 1. Skills Practiced

This exercise will practice:

- [Density of Line Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#21-density-of-line-features).
- How to deal with "Null" values in symbology settings.

## 2. Description

In this exercise, we will calculate and visualize the density of road networks
in the THLD District Assembly by using the
[Density of Line Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#21-density-of-line-features)
tool.

## 3. GIS Dataset

The following datasets are used in this exercises:

- _THLD\_poly.shp_ at
  `GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`.
- _osm2020\_allrds\_THLD.shp_  at
  `GALUP-master -> training -> 1_lu -> datasets -> Primary and secondary roads in THLD District`.

## 4. Instruction

1. Locate _THLD\_poly.shp_ and _osm2020\_allrds\_THLD.shp_ in the
   **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   **<ins>Density of Line Features</ins>** tool under **_Scripts_**
   <img src="../../../images/M2E1/processingScript.svg" alt= "scripts" width="20">.
3. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: THLD_poly,</li>
      <li><b>Line later</b>: osm2020_allrds_THLD,</li>
      <li><b>Output column name</b>: Rds_Den,</li>
      <li><b>Output layer</b>: RdsDenMap.shp,</li>
      <li>leave all other parameters as default.</li>
   </ol>
4. Click **Run**.
5. Open the **_Attribute Table_**
   <img src="../../../images/M2E1/attributes.svg" alt= "AttrTbl" width="20">
   of the output layer, i.e., _RdsDenMap_, to review the calculated output
   field, _Rds\_Den_, each record of which represents the road density of each
   IDU in the THLD District Assembly.
6. Now let's setup the **Symbology** of the output layer.
   Open the
   <img src="../../../images/M2E1/symbology.svg" alt= "AttrTbl" width="20">
   Symbology tab from the **_Layer Properties_** window.
   Select the ![graduated](../../../images/M2E1/rendererGraduatedSymbol.svg)
   Graduated style.
   Specify the _Rds\_Den_ field as **Value**, then choose the _RdPu_ color ramp
   with 5 classes. Click **Apply**.
7. However, if we leave the symbology like this, many IDUs would not appear in
   the output layer because of "Null" values.
   So, let's fix this (still in the **Symbology** tab).

   Select the ![rule](../../../images/M2E1/rendererRuleBasedSymbol.svg)
   Rule\_based style.
   Click **Add rule** ![addrule](../../../images/M2E1/symbologyAdd.svg) on the
   lower left portion of the window to open **_Edit Rule_**.
   Type `0` for **Label**.
   Click <img src="../../../images/M2E1/mIconExpression.svg" alt= "exp" width="20">
   **Expression** to open the **_Expression String Builder_** window, in which
   type `"Rds_den" is NULL` in the **Expression** field.
   Click **OK** to close the **_Expression String Builder_** window.

   Scroll down the **_Edit Rule_** window to the **Symbol** section.
   Change the color to _White_ from the drop-down menu of **Color**.
   Click **OK** to close the **_Edit Rule_** window.
8. Click **OK** on the **Symbology** tab.
9. Create a _Layout_, then add _Legend_, _Scale bar_, and _North Arrow_ to the
   layout.
10. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_maps/M2E1_RdsDenMap.pdf).
- Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#3-exercises) to complete the second exercise.
