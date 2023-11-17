# Module 2 - Exercise 2

## 1. Skills Practices

This exercise will practice:

- [Distance to Point Features](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#22-distance-to-point-features)

## 2. Description

The distance to a point of interest in a district is one common measure of that area's accessibility to tourism resources.
In the Pandamatenga Landscape, we want to explore busisness opportunuties and build a tourism facicility to improve all Integrated Decision Units' (IDUs) accessibility to points of interest.
In the first step of the tourism facility location selection, we need to find out those areas with relatively less access to points of interst by measuring the distances to those points.
In this exercise, we will visualize the distance to Points of Interest in the Panadamatenga landscape by using the [Distance to Point Features](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#22-distance-to-point-features) tool.

## 3. GIS Dataset

The following datasets are used in this exercises:

- _PND_POI.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Points of Interest in Pandamatenga Landscape`
- _PND_IDUs.shp_ at
`GALUP-master -> training -> 1_lu -> datasets -> Pandamatenga Landscape IDUs`
	
## 4. Instruction

1. Locate _PND_POI.shp_ and _PND_IDUs.shp_ in the **_Browser Panel_** and add them to **_Map Canvas_**.
2. In the **_Processing Toolbox_** panel, locate the
   **<ins>Distance to Point Features</ins>** tool under **_PyLUSATQ_**
<img src="https://github.com/mogaetkpp/GALUP/blob/master/img/gui/icon/PyLUSATQ.svg" alt= "scripts" width="20">.
3. **Double Click** to open the tool and set parameters as follows:
   <ol type="a">
      <li><b>Input layer</b>: PND_IDUs,</li>
      <li><b>Point layer</b>: PND_POI,</li>
      <li><b>Distance method</b>: Euclidean,</li>
      <li><b>Output data type</b>: Float,</li>
      <li><b>Output column name</b>: POI_Dis,</li>
      <li><b>Output shapefile</b>: POIDisMap.shp,</li>
      <li>leave all other parameters as default.</li>
   </ol>
4. Click **Run**.
5. Now let's setup the **Symbology** of the output layer.
   Open the
   <img src="../../../img/gui/icon/symbology.svg" alt= "AttrTbl" width="20">
   Symbology tab from the **_Layer Properties_** window.
   Select the ![graduated](../../../img/gui/icon/rendererGraduatedSymbol.svg)
   Graduated style.
   Choose the [_Natural Breaks (Jenks)_](http://wiki.gis.com/wiki/index.php?title=Jenks_Natural_Breaks_Classification&oldid=763049).
   Specify the _POI_Dis_ field as **Value**, then choose the _Reds_ color ramp
   with 5 classes. Click **Apply**.
6. Click **OK** on the **Symbology** tab.
7. Create a _Layout_, then add _Legend_, _Scale bar_, and _North Arrow_ to the
   layout.
8. Export the map as a PDF file.

## 5.Result

- Upon completion, the map you got should look similar to this pdf
  [here](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/pdf_maps/DistanceToHF.pdf).
- Please go back to
  [Module 2](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/modules/module2.md#7-exercises-and-post-training-survey) to complete the third exercise.
