# Module 4 - Exercise 3

## 1. Skills Practiced

This exercise will practice:

- **Rank Sum Method**
- **Rank Reciprocal Method**

## 2. Nonpairwise Weighting Methods for Row Crops Farming

The row crops model evaluates the suitability of lands to grow row crops
from two objectives, physical and economic suitability.
These two could be further divided into sub-objectives, including landscape
and soil conditions, market, and transportation accessibility.
Module 4 shows how to equally weigh objectives and sub-objectives when it is possible to compare importance between them.

This exercise aims to illustrate how to organize sub-objectives by using different nonpairwise weighting methods if we can directly compare those sub-objectives.

The rank sum method firstly assesses weight values of all sub-objectives by arranging them in rank order from the value 1 signifies most important to the nth important. Then, this method divides the inverse rank value of each sub-objective by the sum of the inverse rank value of all sub-objectives.

The rank reciprocal method also needs to first assess the weight values of all sub-objectives in rank order. Then, this method divides the reciprocal values of each sub-objective by the sum of the reciprocal values of all sub-objectives.

### 2.2 Required Datasets

The following datasets are requested in the practice of weighting methods
for Row Crops:

- The outcome from
  [Landscape Condition](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/LandConditionMap.pdf)
  model
- The outcome from
  [Soil Condition](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/SoilIndex.pdf)
  model
- The outcome from
  [Market]((https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/rcrp_Market.pdf)
  model
- The outcome from
  [Transportation Accessibility](https://github.com/SERVIR-WA/GALUP/blob/master/img/map/m3_transportation_accessibility.png)
  model

## 3. Instruction

### 3.1 Rank Sum Method
1. This exercise rank Landscape Condition, Soil Condition, Market, and
   Transportation Accessibility in order: 3, 2, 4, 1.
2. Calculate the weight value of each sub-objective by using rank sum method.
3. Use **<ins>Join attributes by field value</ins>** tool
   under **_Vector general_** to join outcome fields into one vector layer.
4. Use
   **<ins>Weighted Sum of Fields</ins>** tool under **_Scripts_**
   <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">.
   to calculate the weighted sum of sub-objectives by using the weight values
   from rank sum method.
5. Name **Output field name** as _ranksum_ and **Output layer** as _Ranksum.shp_
5. Now, let's set up the **Symbology** of the output layer _Ranksum.shp_.
   Open the
   <img src="../../../img/gui/icon/symbology.svg" alt= "AttrTbl" width="20">
   **Symbology** tab from the **Layer Properties** window.
   Select the ![graduated](../../../img/gui/icon/rendererGraduatedSymbol.svg)
   *Graduated style*.
   Specify the _ranksum_ field as **Value**, and then choose the _RdYlGn_ color
   ramp with **5** classes.
   Click **Apply**.
6. Create a _Layout_ for the map, and then add _Legend_, _Scale bar_, and
    _North Arrow_ to it. 
7. Export the map as a PDF file.

### 3.2 Rank Reciprocal Method
1. This exercise rank Landscape Condition, Soil Condition, Market, and
   Transportation Accessibility in order: 3, 2, 4, 1.
2. Calculate the weight value of each sub-objective by using
   rank reciprocal method.
3. Use **<ins>Join attributes by field value</ins>** tool
   under **_Vector general_** to join outcome fields into one vector layer.
4. Use
   **<ins>Weighted Sum of Fields</ins>** tool under **_Scripts_**
   <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">.
   to calculate the weighted sum of sub-objectives by using the weight values
   from rank reciprocal method.
5. Name **Output field name** as _rankrcp_ and **Output layer** as _Rankrcp.shp_
5. Now, let's set up the **Symbology** of the output layer _Rankrcp.shp_.
   Open the
   <img src="../../../img/gui/icon/symbology.svg" alt= "AttrTbl" width="20">
   **Symbology** tab from the **Layer Properties** window.
   Select the ![graduated](../../../img/gui/icon/rendererGraduatedSymbol.svg)
   *Graduated style*.
   Specify the _rankrcp_ field as **Value**, and then choose the _RdYlGn_ color
   ramp with **5** classes.
   Click **Apply**.
6. Create a _Layout_ for the map, and then add _Legend_, _Scale bar_, and
    _North Arrow_ to it. 
7. Export the map as a PDF file.

## 4.Result

- Upon completion, the map by using rank sum method you got should look similar
  to this pdf [here](),
  and the map by using rank reciprocal method should look similar to this pdf
  [here]()
- Now you have completed all exercises. Please go back to
  [Module 4](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module4.md)
  to turn in them.
