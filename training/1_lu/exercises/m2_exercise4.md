# Module 2 - Exercise 4

## 1. Description

Yam is an important staple food crop in Ghana and is produced throughout the country. In Twifo/Heman/Lower Denkyira (THLD) district, the local government want to plan and develop a new crop land to grow Yam. Therefore, as a planner, we need to provide suggestions for the local governemnt to choose the most suitable land. 

The first step of our analysis aims to select out the area with a suitable soil pH range. Soil pH affects plant nutrient availability by controlling the chemical forms of the different nutrients and influencing the chemical reactions they undergo. Yam prefers the rich fertile soil that has a pH of 5.5 to 6.5<sup>[1]</sup>, and the horizontal growth of its roots has been observed to occur within the top 10 cm of soil<sup>[2]</sup>. So, we will evaluate the land in THLD district by analyzing the Soil pH dataset in root depth ranged from 5 to 15 cm.

In this exercise, we will create a Soil pH index to evaluate the suitability to grow Yam in the land of each Integrated Decision Units' (IDUs) in THLD district.

You should use _SD5/_15.tif_ at
`GALUP-master -> training -> 1_lu -> datasets -> Soil pH 5_15 in THLD District`
and _THLD\_poly_ at
`GALUP-master -> training -> 1_lu -> datasets -> Integrated Decision Units in THLD District`
to finish this exercise.

## 2. Skills Practices

This exercise covers:

- Use the Reclassify Field tool
- Use the Zonal Statistics tool

## 3. Instruction

1. Locate _SD5\_15.tif_ and _THLD\_poly_ in the _Browser Panel_ and add it to
   _Map Canvas_.
2. Open _Zonal Statistics_ tool.
3. Set _THLD\_poly_ as Input layer and _SD5\_15.tif_ as Raster layer.
4. Type _mean_ in Types of statistics and then give an appropriate name for
   Output column prefix.
5. Choose drop down list in Output layer and select _Save to Files..._, so
   you can save the output shapefile to the files you frequently use.
6. Run _Zonal statistics_ tool.
7. Open _Reclassify Field_ tool.
8. Set the output shapefile from the Zonal Statistics tool as Input layer and
   the output column as Field to reclassify.
9. Type _40-50, 50-55, 55-65_ in Old values.
10. Type _1, 2, 3_ in New values.
11. Set _0_ for No data value and then give an appropriate name for
   Output column prefix.
12. Choose drop down list in Output layer and select _Save to Files..._, so
   you can save the output shapefile to the files you frequently use.
13. Run _Reclassify Field_ tool.
14. Choose _Categorized_ symbology and choose the _Greens_ color ramp to render
   the the Output column from _Reclassify Field_ tool.
4. Add _ESRI Gray (light)_ as the basemap.
5. Create a _Layout_ and then add _Legend_, _Scale bar_, and _North Arrow_.
6. Export as a PDF file.

## 4.Result

Now, you can select out the area with Soil pH Suitaility Index 3 as the suitable
cropland to grow Yam.

- See the example map, Population of Ghana in 2018, in this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_download/SoilIndex.pdf)

## 5.Reference

1. Ernest, D. (n.d.). How to Grow Yams. https://www.diynetwork.com/how-to/outdoors/gardening/how-to-grow-yams
2. O'SULLIVAN, J. N. (2008). Root distribution of yam (Dioscorea alata) determined by strontium tracer. Experimental Agriculture, 44(2), 223.
