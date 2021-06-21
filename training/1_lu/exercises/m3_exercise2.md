# Module 3 - Exercise 2

## 1. Skills Practiced

This exercise will practice:

- **QGIS Graphical Modeler**
- **Market Model**

## 2. Description

Market is a sub-objective of the economic objective. The reason that we set this as a sub-objective is that the distance to market can affect the row crops selling and transportation fee.

**Market model** aims to evaluate the suitability of IDUs for planting row crops by measuring the distance between the IDU and the market places (i.e., the distance to large city, middle city, and small city).

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

1. Locate _LargeCity\_pt.shp_, _MiddleCity\_pt.shp_, _SmallCity\_pt.shp_ and _THLD\_poly.shp_ in the _Browser Panel_ and add them to _Map Canvas_.
2. In the _Menu Toolbar_, click _Processing_ and open _Graphical Modeler..._ ![gm](../../../images/processingModel.svg).
3. In the _Model Properties_ panel, name the _Name_ as **Market**, and the _Group_ as **Economic**.
4. In the _Inputs_ panel, click _Inputs_ tab, add:

- One _Vector Features_ parameter, and name the _Parameter name_ as **InputPolygon** and leave others as default, then click **OK**.
- Three _Point_ parameters, and name their the _Parameter name_ as **Large cities**, **Medium cities**, and **Small cities** respectively, and leave others as default, then click **OK** for each one.
- One _String_ parameter, and name the _Description_ as **Weights by City Level** and type `0.6, 0.3, 0.1` for _Default value_, and leave others as default, then then click **OK**.

4. In the _Algorithm_ tab, add and set the parameters of the following tools **in sequence**.

|_Distance to Point Features_|_Rescale Field Field Linearly_|_Distance to Point Features_|_Rescale Field Field Linearly_|
|------------------------|---------------------|------------------------------------|------------------------|
| 1 | 2 | 3 | 4|
|**Description**: Distance to Large City <br> **Input layer**: select _InputPolygon_ <br> **Point layer**: select _Large cities_ <br> **Distance method**: select _Euclidean_ <br> **Output data type**: select _Float_ <br> **Output column name**: Dis_to_BC <br> **Output shapefile**: _leave this as default_ |**Description**: Res Dist to Large City <br> **Input layer**: select _'Output shapefile' from algorithm 'Distance to Large City'_ <br> **Field to rescale**: Dis_to_BC <br> **Start value for rescaling**: 30000 <br> **End value for scaling**: 0 <br> **New minimum**: 1 <br> **New maximum**: 9 <br> **Output field name**: Res_D_BC <br> **Output layer**: _leave this as default_|**Description**: Distance to Medium City <br> **Input layer**: select _'Output layer' from algorithm 'Res Dist to Large City'_ <br> **Point layer**: select _Medium cities_ <br> **Distance method**: select _Euclidean_ <br> **Output data type**: select _Float_ <br> **Output column name**: Dis_to_MC <br> **Output shapefile**: _leave this as default_ |**Description**: Res Dist to Medium City <br> **Input layer**: select _'Output shapefile' from algorithm 'Distance to Medium City'_ <br> **Field to rescale**: Dis_to_MC <br> **Start value for rescaling**: 30000 <br> **End value for scaling**: 0 <br> **New minimum**: 1 <br> **New maximum**: 9 <br> **Output field name**: Res_D_MC <br> **Output layer**: _leave this as default_|

|_Distance to Point Features_|_Rescale Field Field Linearly_ |_Weighted Sum of Fields_|
|-----------------------|------------------|------------------|
| 5 | 6 | 7 |
|**Description**: Distance to Small City <br> **Input layer**: select _'Output layer' from algorithm 'Res Dist to Medium City'_ <br> **Point layer**: select _Small cities_ <br> **Distance method**: select _Euclidean_ <br> **Output data type**: select _Float_ <br> **Output column name**: Dis_to_SC <br> **Output shapefile**: _leave this as default_  |**Description**: Res Dist to Small City <br> **Input layer**: select _'Output shapefile' from algorithm 'Distance to Small City'_ <br> **Field to rescale**: Dis_to_SC <br> **Start value for rescaling**: 30000 <br> **End value for scaling**: 0 <br> **New minimum**: 1 <br> **New maximum**: 9 <br> **Output field name**: Res_D_SC <br> **Output layer**: _leave this as default_|**Description**: Weighted Sum of Fields <br> **Input layer**: select _'Output layer' from algorithm 'Res Dist to Small City'_ <br> **Fields**: Res_D_BC;Res_D_MC;Res_D_SC <br> **Weights** click the _Value_ icon, select _Model Input_, and select _Weights by City Level_ <br> **Output column name**: Market <br> **Output layer**: rcrp_Market |

1. Now you have finished the model, click **Run model** ![st](../../../images/mActionStart.svg) on the main menu of the _Processing Modeler_ window to open the _Market_ model.
2. Set the model as follows:

- **Inputpolygon**: select _THLD\_poly_
- **Large cities**: _LargeCity\_pt_
- **Medium cities**: _MediumCity\_pt_
- **Small cities**: _SmallCity\_pt_
- Leave other prameters as default
- Click **Run**.

7.  Choose _Categorized_ symbology and choose the _Bupu_ color ramp to
render the the Output column from _Reclassify Field_ tool.
8. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
9. Export as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_maps/rcrp_Market.pdf).
- Now you have completed all exercises. Please go back to
  [Module 3](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module3.md#4-exercises-and-post-training-survey) to turn in them.

