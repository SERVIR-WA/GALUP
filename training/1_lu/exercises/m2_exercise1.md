# Module 2 - Exercise 1

## 1. Description

In this exercise, we will visualize the road network density in the THLD area by using the [Density of Line Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#21-density-of-line-features) tool.

## 2. GIS Dataset

You should use the following data to finish this exercise:
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Integrated Decision Units in THLD District`.
- _osm2020\_allrds\_THLD.shp_  at `GALUP-master -> training -> 1_lu -> datasets -> Primary and secondary roads in THLD District`.

## 3. Skills Practiced

This exercise covers:

- The parameter setting and the usage of the Density of Line Features tool.

## 4. Instruction

1. Locate _THLD\_poly.shp_ and _osm2020\_allrds\_THLD.shp_ in the _Browser Panel_ and add them to
   _Map Canvas_.
2. In the _Processing Toolbox_ panel, find the Density of Line Features tool under the _Scripts_.
3. Open the Density of Line Features tool, set the _THLD\_poly.shp_ as the **input layer**, and _osm2020\_allrds\_THLD.shp_ as the **Line layer**. Name the **Output column name** as _Rds\_Den_, and the **Output layer** as _RdsDenMap_ and click **Run**.
4. Open _Attribute Table_ of the output layer (_RdsDenMap_) to review the output field, _Rds\_Den_, which represents THLD roads network density
   by district.
5. Open the symbology window, choose the target field: _Rds\_Den_ and _Graduated_ symbology, then choose the _RdPu_ color ramp with 5 classes. Click **Apply**, and then choose _Rule\_based symbology_, click **Add rule** ![addrule](../../../images/M2E1/symbologyAdd.svg) to open the _Edit Rule_ window.
6. Type _0_ for the _Label_, and click the **Expression** ![expre](../../../images/M2E1/mIconExpression.svg) to open the _Expression String Builder_ window, and type _"Rds\_den" is NULL_ into the _Expression_ field, and click **OK** to close the _Expression String Builder_ window.
7. Scroll down the _Edit Rule_ window and select the white color in the drop-down menu of the _Color_. Click **OK** to close the _Edit Rule_ window.
8. Click **OK** on the symbology window to finish the symbology part.
9.  Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
10. Export as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_download/M2E1_RdsDenMap.pdf).
- Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#3-exercises) to complete the second exercise.
