# Module 2 - Exercise 3

## 1. Description

Normally, the residential areas will be built near the education facilities so that it will be convenient for the education of children. In this exercise, we will help to find out the IDUs of THLD that are in proximity (within the 1 miles) to the education facility by using the [Select by Location](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#26-select-by-location) tool.

## 2. GIS Dataset
You should use the following data to finish this exercise:
- _THLD\_poly.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Integrated Decision Units in THLD District`.
- _Education\_Facilities.shp_ at `GALUP-master -> training -> 1_lu -> datasets -> Education facilities in THLD District`.

## 3. Skills Practiced

This exercise covers:

- The parameter setting and the usage of the Select by Location tool.

## 4. Instruction

1. Locate _THLD\_poly.shp_ and _Education\_Facilities.shp_ in the _Browser Panel_ and add them to
   _Map Canvas_.
2. In the _Processing Toolbox_ panel, find the [Select by Location tool under the _Scripts_.
3. Open the Select by Location tool, set the _THLD\_poly.shp_ as the **Input layer**, and _Education\_Facilities.shp_ as the **Selection layer**. Set the **Join option** as _Within a distance_, and the **Within distance of selecting feature** as _1 mile_. Name the **Output layer** as _EduProIDU_ and click **Run**.
4. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
5. Export as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](../pdf_download/M2E3_EduProximity2.pdf).
- Please go back to
  [Module 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module2.md#3-exercises) to complete the fourth exercise.
