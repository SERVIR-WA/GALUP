# Module 2 - Exercise 1

## 1. Skills Practiced

This exercise will practice:

- [Density of Line Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#21-density-of-line-features).
- How to deal with "Null" values in symbology settings.

## 2. Description

In this exercise, we will calculate and visualize the
**density of road networks**
in the THLD District Assembly by using the
[Density of Line Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#21-density-of-line-features)
tool.
This is an important measurement to help understand transportation
accessibility of a given region, which is a crucial factor to consider when
making land-use plans.

## 3. GIS Dataset

The following datasets are used in this exercises:

- _THLD\_poly.shp_ at
  `GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`.
- _osm2020\_allrds\_THLD.shp_ at
  `GALUP-master -> training -> 1_lu -> datasets -> Primary and secondary roads in THLD District`.

## 4. Instruction

1. Locate _THLD\_poly.shp_ and _osm2020\_allrds\_THLD.shp_ in the
   **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   **<ins>Density of Line Features</ins>** tool under **_Scripts_**
   <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">.
3. **Double Click** to open the tool and set parameters as follows:
   - **Input layer**: THLD_poly,
   - **Line later**: osm2020_allrds_THLD,
   - **Output column name**: Rds_Den,
   - **Output layer**: RdsDenMap.shp,
   - leave all other parameters as default.
4. Click **Run**.
5. Open the **_Attribute Table_**
   <img src="../../../img/gui/icon/attributes.svg" alt= "AttrTbl" width="20">
   of the output layer, i.e., _RdsDenMap_, to review the calculated output
   field, _Rds\_Den_, each record of which represents the road density of each
   IDU in the THLD District Assembly.
6. Now let's setup the **Symbology** of the output layer.
   Open the
   <img src="../../../img/gui/icon/symbology.svg" alt= "AttrTbl" width="20">
   Symbology tab from the **_Layer Properties_** window.
   Select the ![graduated](../../../img/gui/icon/rendererGraduatedSymbol.svg)
   Graduated style.
   Specify the _Rds\_Den_ field as **Value**, then choose the _RdPu_ color ramp
   with 5 classes. Click **Apply**.
7. However, if we leave the symbology like this, many IDUs would not appear in
   the output layer because of "Null" values.
   So, we need to add a specific "rule" on how "Null" values should be
   rendered.
   <ol type="1">
      <li>
      Now, select the
      <img src="../../../img/gui/icon/rendererRuleBasedSymbol.svg" alt="rule">
      Rule_based style in the Symbology tab.
      </li>
      <li>
      Then, click <b>Add rule</b>
      <img src="../../../img/gui/icon/symbologyAdd.svg" alt="addrule"> on the
      lower left portion of the window to open <b><i>Edit Rule</i></b>.
      </li>
      <li>
      Type <code>0</code> for <b>Label</b>.
      </li>
      <li>
      Click
      <img src="../../../img/gui/icon/mIconExpression.svg" alt= "exp" width="20">
      <b>Expression</b> to open the <b><i>Expression String Builder</i></b>
      window.
      </li>
      <li>
      Type <code>"Rds_den" is NULL</code> in the <b>Expression</b> field.
      </li>
      <li>
      Click <b>OK</b> to close the <b><i>Expression String Builder</i></b>
      window.
      </li>
      <li>
      Scroll down the <b><i>Edit Rule</i></b> window to the <b>Symbol</b>
      section.
      Change the color to <ins><i>white</i></ins> from the drop-down menu of
      <b>Color</b>.
      </li>
      <li>
      Click <b>OK</b> to close the <b><i>Edit Rule</i></b> window.
      </li>
      <li>
      Click <b>OK</b> on the <b>Symbology</b> tab.
      </li>
   </ol>
8. Create a _Layout_, then add _Legend_, _Scale bar_, and _North Arrow_ to the
   layout.
9. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_maps/M2E1_RdsDenMap.pdf).
- Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#7-exercises-and-post-training-survey) to complete the second exercise.
