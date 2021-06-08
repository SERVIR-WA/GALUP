# Module 2 - Exercise 2

## 1. Description

The distance to health facilities in a district is one common measure of that area's accessibility to medical resources.
Twifo-Heman-Lower-Denkyira (THLD) district, we want to build a healthcare center to improve all Integrated Decision Units' (IDUs) accessibility to the medical resource.
In the first step of the healthcare center location selection, we need to find out those areas with relatively less access to health facilities by measuring the distances to those facilities.
In this exercise, we will visualize the distance to Health Facilities in the THLD district by using the [Distance to Point Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#22-distance-to-point-features) tool.

## 2. GIS Dataset

You should use the following data to finish this exercise: 
- _Health\_Facilities.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Health facilities in THLD District`
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Integrated Decision Units in THLD District`

## 3. Skills Practices

This exercise will practice:

- [Distance to Point Features](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#22-distance-to-point-features)

## 4. Instruction

1. Locate _Health\_Facilities.shp_ and _THLD\_poly.shp_ in the _Browser Panel_ and add it to
   _Map Canvas_.
2. Open _Distance to Point Features_ tool.
3. Set _THLD\_poly_ as **Input layer** and _Health\_Facilities.shp_ as **Point layer**.
4. Choose _Euclidean_ as Distance method and _Float_ as **Output data type**, and then
   give an appropriate **Output column name**.
5. Choose drop down list in **Output shapefile** and select `Save to Files...`, so
   you can save the output shapefile to the files you frequently use.
6. **Run** _Distance to Points_ tool.
7. Choose _Graduated_ symbology and choose the _Natural Breaks (Jenks)_ and the _Reds_
   color ramp with 5 classes to render the Output column.
8. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
9. Export as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_download/DistanceToHF.pdf).
- Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#3-exercises) to complete the third exercise.