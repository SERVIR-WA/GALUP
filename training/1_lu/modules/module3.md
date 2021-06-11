# Module 3 - Create Suitability Models with QGIS Graphical Modeler

**What will you learn from this module?**

- Get to know the Graphical Modeler,
- Learn about the Row Crops model,
- Solve planning-related questions by modeling in the Graphical Modeler.

## 1. Graphical Modeler

## 2. Suitability Modeling

Suitability modeling is the most common application for the LUCIS-OPEN Tools in QGIS and can solve a variety of problems, for examples, you can use Tools to find the best place for a new housing development.

In this module, we will use Tools to do land suitability modeling. Each IDU in the THLD area will be assigned to one of the four land uses by comparing land use scores: Row Crops, Livestock, Timberland, and Urban.

In terms of the scoring process, firstly, we have different decisive factors in each of the land use, and, under each decisive factor, multiple models will be applied and generate a weighted score for that decisive factor (with 9 represents the highest, and 1 represents the lowest) to each IDU. Then, the final score of a certain land use of each IDU will be calculated by using the [Compute AHP Weights](https://github.com/SERVIR-WA/GALUP/wiki/Tools#compute-ahp-weights) to weightedly sum up each decisive factor's score under that land use (with 9 represents the highest, and 1 represents the lowest). Finally, after we having a score for each land use on each IDU, the land use with the highest score will be the final land use for that IDU.

## 3. Row Crops Model

_Row Crops Model_

### 3.1 Economic - Transportation Accessibility

_Transportation Accessibility model_ aims to evaluate the accessibility of IDUs
to traffic roads.
By using [_Distance to Line Features_](https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-line-features),
this model calculate the shorest distance from each IDU to the primary and
secondary roads and store the values in two different fields.
Then the model use [_Rescale Field Linearly_](https://github.com/SERVIR-WA/GALUP/wiki/Tools#rescale-field-linearly)
to transform values in fields to specified continuous scales (i.e., 1 to 9 scale).
Finally, by using [_Weight Sum of Fields_](https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields)
to multiply the rescaled fields with weighted value and sum them up,
the model can create a index for each IDU to measure their accessibility to
the primary and secondary roads.
You can check the _Input parameters_ of this model
[here](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#transport-accessibility-economic).

## 3.1.1 Usage
_Transportation Accessibility model_ can be used to evaluate the nearness of
polygons to the two different types of line features. By adjusting the weighted
value, the model can give different outcomes.

## 3.1.2 Example

In the following example, we choose the **Join one to one** option to find out
the **count** (number of records) of points of interest (tourism) within each
District Assembly of Ghana.

The datasets used are listed below:


The two figures below display the specific parameter settings and the output of the model.



In the output map


### 3.2 Physical - Soil Condition

When evaluate the Soil Condition of the Row Crops land use, three influential indicators on the growth of crops are included in this model: Root Zone Depth, Soil Drainage, and Soil PH at Different Soil Depth. The logic of this model is that, firstly, the model uses Zonal Statistics tool to assign the raster data (three indicators) to the vector polygon, and then uses the Reclassify Field tool to reclassify the assigned value on each the vector data (the reclassification rule should be based on the official documents and agriculture literatures). Finally, the Weight Sum of Fields tool is used to calculate the final score for the Soil Condition. For more information about this model, please click [here](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#soil-condition-physical).

#### 3.2.1 Usage

This model is often used to evaluate the soil condition for crops. Specific parameters (reclassification rule, weights of each indicator) in the model can be set according to the growing condition of different crops. The number of intervals of soil depth for the soil PH can also be changed based on the soil PH data you find.

#### 3.2.2 Example

In the following example, we set the parameters of the model according to the growing conditions of 6 main crops (Maize, Rice, Cassava, Yam, Cocoyam, Plantain) in THLD area.

The datasets used are listed below:

| ID | File Name     | Data Format | Type    | Description                                                 |
|--- |---------------|-------------|---------|-------------------------------------------------------------|
| 1  | THLD_poly.shp | vector      | polygon | IDUs in the THLD District Assembly |
| 2  | RZD_THLD100   | raster      | tiff    | [Root Zone Depth](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/c77d1209-56e9-4cac-b76e-bbf6c7e3a617) |
| 3  | Drain_THLD100 | raster      | tiff    | [Soil Drainage](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/953d0964-6746-489a-a8d1-f188595516a9)     |
| 4  | SD0_5          | raster      | tiff    | [Soil PH 0-5](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/a3364e47-9229-4a6d-aed2-487fd7e4dccc)     |
| 5  | SD5_15         | raster      | tiff    | [Soil PH 5-15](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/a3364e47-9229-4a6d-aed2-487fd7e4dccc)     |
| 6  | SD15_30        | raster      | tiff    | [Soil PH 15-30](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/a3364e47-9229-4a6d-aed2-487fd7e4dccc)     |
| 7  | SD30_60        | raster      | tiff    | [Soil PH 30-60](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/a3364e47-9229-4a6d-aed2-487fd7e4dccc)     |
| 8  | SD60_100       | raster      | tiff    | [Soil PH 60-100](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/a3364e47-9229-4a6d-aed2-487fd7e4dccc)     |
| 9  | SD100_200      | raster      | tiff    | [Soil PH 100-200](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/a3364e47-9229-4a6d-aed2-487fd7e4dccc) |

|          Parameter Setting         |    Output Map   |
|------------------------------------------|------------------------------------------|
| ![PS1](../../../images/SoilCondition/pa_set.png) | ![am1](../../../images/SoilCondition/symbology_sc.png) |

## 4. Exercises and Post-training Survey

- Please complete the [Exercise 1](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise1.md).
- Please complete the [Exercise 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise2.md).
- Please take this post-training
  [survey](https://ufl.qualtrics.com/jfe/form/SV_9nLiduVDMRRE4t0) (required).
- Please submit your exercises [here](https://github.com/SERVIR-WA/GALUP/issues/new?assignees=muribasterra&labels=exercise+w1m2&milestone=Module+2+Exercises&template=w1m2-exercise-submission.md&title=Module+2+exercises+%5Breplace+with+your+name%5D).

## 5. What's Next?

Module 4 - Aggregate Results to Make Land-Use Decisions.
