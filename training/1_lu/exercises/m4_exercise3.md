# Module 4 - Exercise 3

## 1. Skills Practiced

This exercise will practice:

- **Rank Sum Method**
- **Rank Reciprocal Method**

## 2. Nonpairwise Weighting Methods for Row Crops Farming

This exercise aims to illustrate how to organize sub-objectives
by using different nonpairwise weighting methods if we can
directly compare landscape condition, soil condition, market,
and transportation accessibility.

The rank sum method firstly assesses weight values of all sub-objectives by
arranging them in rank order from the value 1 signifies most important
to the nth important.
Then, this method divides the inverse rank value of each sub-objective
by the sum of the inverse rank value of all sub-objectives.

The rank reciprocal method also needs to first assess the weight values of
all sub-objectives in rank order.
Then, this method divides the reciprocal values of each sub-objective
by the sum of the reciprocal values of all sub-objectives.

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
  [Market](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/rcrp_Market.pdf)
  model
- The outcome from
  [Transportation Accessibility](https://github.com/SERVIR-WA/GALUP/blob/master/img/map/m3_transportation_accessibility.png)
  model

## 3. Instruction

1. This exercise rank Landscape Condition, Soil Condition, Market, and
   Transportation Accessibility in order: 2, 1, 4, 3.
2. Calculate the weight value of each sub-objective by using rank sum method
   and rank reciprocal method.
3. Use **<ins>Join attributes by field value</ins>** tool
   under **_Vector general_** to join outcome fields into one vector layer.
4. Use
   **<ins>Weighted Sum of Fields</ins>** tool under **_Scripts_**
   <img src="../../../img/gui/icon/processingScript.svg" alt= "scripts" width="20">
   to calculate the weighted sum of sub-objectives by using the weight values
   from rank sum method and rank reciprocal method.
5. Now, let's set up the **Symbology** of the output layers.
   Open the
   <img src="../../../img/gui/icon/symbology.svg" alt= "AttrTbl" width="20">
   **Symbology** tab from the **Layer Properties** window.
   Select the ![graduated](../../../img/gui/icon/rendererGraduatedSymbol.svg)
   *Graduated style*.
   Specify the rank sum and rank reciprocal weighted field
   as **Value**, and then choose the _RdYlGn_ color ramp with **5** classes.
   Click **Apply**.
6. Create two _Layout_ for two maps, and then add _Legend_, _Scale bar_, and
    _North Arrow_ to them. 
7. Export these two maps as a PDF file.

## 4.Result

- Upon completion, the map by using rank sum method you got should look similar
  to this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/RankSum.pdf),
  and the map by using rank reciprocal method should look similar to this pdf
  [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/pdf_maps/RankReciprocal.pdf).
- Now you have completed all exercises. Please go back to
  [Module 4](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module4.md)
  to turn in them.
