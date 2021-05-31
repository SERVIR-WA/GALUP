# Exercise 2

## 1. Description

The distance to health facilities in a district is one common measure of that area's accessibility to medical resource. In Twifo/Heman/Lower Denkyira (THLD) district, we want to build a healthcare center to improve all Integrated Decision Units' (IDUs) accessibility to medical resource. Therefore, we need to find out those area far from health facilities in the first step of the healthcare center location selection. In this exercise, we will visualize the distance to Health Facilities in THLD district by calculating the distance to the health facilities in each IDU.

You should use _Health\_Facilities.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Health facilities in THLD`
and _THLD\_poly_ at
`GALUP-master -> training -> 1_lu -> datasets -> IDUs of THLD District`
to finish this exercise.

## 2. Skills Practices

This exercise covers:

- Use the Distance to Points tool

## 3. Instruction

1. Locate _Health\_Facilities.shp_ and _THLD\_poly_ in the _Browser Panel_ and add it to
   _Map Canvas_.
2. Open _Distance to Point Features_ tool.
3. Set _THLD\_poly_ as Input layer and _Health\_Facilities.shp_ as Point layer.
4. Choose _Euclidean_ as Distance method and _Float_ as Output data type, and then
   give an appropriate Output column name.
5. Choose drop down list in Output shapefile and select _Save to Files..._, so
   you can save the output shapefile to the files you frequently use.
6. Run _Distance to Points_ tool.
7. Choose _Graduated_ symbology and choose the _Natural Breaks (Jenks)_ and the _Reds_
   color ramp with 5 classes to render the Output column.
8. Add _ESRI Gray (light)_ as the basemap.
9. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
10. Export as a PDF file.

## 4.Result

Now, you can easily find out the area with the lowest accessibility to medical resource
by reviewing the map.

- See the example map, Distance to Health Facility in THLD District, in this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_download/DistanceToHF.pdf)
