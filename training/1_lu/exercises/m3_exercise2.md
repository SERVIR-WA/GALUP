# Module 3 - Exercise 2

## 1. Skills Practiced

This exercise will practice:

- **QGIS Graphical Modeler**
- **Market Model**

## 2. Description

Market is a significant aspect for planting row crops because the distance to
market can affect the row crops selling and transportation fee.

**Market model** aims to evaluate the suitability of IDUs for planting row
crops by measuring the distance between the IDU and the market places (i.e.,
the distance to large city, middle city, and small city).

## 3. GIS Dataset

You should use the following data to finish this exercise:
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs in the THLD District`
- _LargeCity\_pt.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Large_City_Point`
- _MediumCity\_pt.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Medium_City_Point`
- _SmallCity\_pt.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Small_City_Point`

## 4. Instruction

![marketmodelmap](../../../images/Model%20Map/Market.svg)

1. Locate _LargeCity\_pt.shp_, _MiddleCity\_pt.shp_, _SmallCity\_pt.shp_ and
_THLD\_poly.shp_ in the **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the _Menu Toolbar_, click _Processing_ and open ![gm](../../../images/processingModel.svg) `Graphical Modeler...` .
3. In the **_Model Properties_** panel, name the _Name_ as **Market**, and
the _Group_ as **Economic**.
4. In the **_Inputs_** panel, click **_Inputs_** tab, add:
   - One _Vector Features_ parameter, and name the _Parameter name_ as
**1_Input Polygon** and leave others as default, then click **OK**.
   - Three _Point_ parameters, and name their the _Parameter name_ as
**2_Large cities**, **3_Medium cities**, and **4_Small cities** respectively, and
leave others as default, then click **OK** for each one.
   - One _String_ parameter, and name the _Description_ as
**5_Weights by City Level** and type `0.6, 0.3, 0.1` for _Default value_
market weights for **Large cities**, **Medium cities**, and **Small cities**),
and leave others as default, then then click **OK**.
5. Parameter setting:

   ![m1](../../../images/PrameterSetting/m1.svg)
<br><sup>*</sup>
Note: Parameters were left as default if not mentioned in the table above.

6. Edit the names of inputs, delete all the number and underscore in front of their names (e.g., edit **1_Input Polygon** to **Input Polygon**).

7. Now you have finished the model, click ![st](../../../images/mActionStart.svg)
`Run model`  on the main menu of the _Processing Modeler_ window to open the
_Market_ model.
8. Set the model as follows:
   - **Inputpolygon**: select _THLD\_poly_
   - **Large cities**: _LargeCity\_pt_
   - **Medium cities**: _MediumCity\_pt_
   - **Small cities**: _SmallCity\_pt_
   - Leave other prameters as default.
   - Click **Run**.
9. Now let's setup the **Symbology** of the output layer _rcrp\_Market_.
Open the <img src="../../../images/M2E1/symbology.svg" alt= "AttrTbl" width="20">
Symbology tab from the **Layer Properties** window. Select the ![graduated](../../../images/M2E1/rendererGraduatedSymbol.svg) Graduated style. Specify the _Market_
field as **Value**, then choose the _BuPu_ color ramp with 5 classes. Click **Apply**.
10. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
11. Export as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_maps/rcrp_Market.pdf).
- Now you have completed all exercises. Please go back to
  [Module 3](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module3.md#4-exercises-and-post-training-survey) to turn in them.