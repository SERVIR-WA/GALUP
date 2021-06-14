# Module 3 - Create Suitability Models with QGIS Graphical Modeler

**What will you learn from this module?**

- Get to know the Graphical Modeler,
- Learn about the Row Crops model,
- Solve planning-related questions by modeling in the Graphical Modeler.

## 1. Introduction to QGIS Graphical Modeler

## 2. Suitability Modeling

Suitability modeling is the most common application for the LUCIS-OPEN Tools in QGIS and can solve a variety of problems, for examples, you can use Tools to find the best place for a new housing development.

### 2.1 LUCIS Philosophy

The following figure shows the LUCIS Framework.
![lucis_workflow](../../../images/lucis_workflow.svg)
The first step is to ascertain the goals of the LUCIS. We need to inquire the opinions of stakeholders and separate these values into three categories: 1) agricultural productions, 2) socioeconomic activities, and 3) ecological functions. To be more specific, these three categories can be turned into three land uses correspondingly: 1) agricultural land uses, 2) urban land uses, and 3) conservational land. Therefore, the goals are to identify land use for agricultural land uses, urban land uses, and conservational land.

The second step is to ascertain the objectives for each goal. For agricultural land uses and urban land uses, we always consider the suitability, in which two perspectives are commonly used to derive objectives: 1) physical suitability, and 2) economic suitability. In terms of conservational land, we should consider the significance of conservational land and two perspectives are commonly: 1) existing ecological value, and 2) potential ecological value.

### 2.2 The General Workflow of Suitability Modeling

#### 2.2.1 Define Criteria

#### 2.2.2 Transform to a Common Suitability Scale

#### 2.2.3 Weight the Criteria and Create a Suitability Map

In this module, we will use Tools to do land suitability modeling. Each IDU in the THLD area will be assigned to one of the four land uses by comparing land use scores: Row Crops, Livestock, Timberland, and Urban.

In terms of the scoring process, firstly, we have different decisive factors in each of the land use, and, under each decisive factor, multiple models will be applied and generate a weighted score for that decisive factor (with 9 represents the highest, and 1 represents the lowest) to each IDU. Finally, after we having a score for each land use on each IDU, the land use with the highest score will be the final land use for that IDU.

## 3. Row Crops Model

_Row Crops Model_ aims to evaluate the suitability of IDUs' land in THLD district
to grow Row crops. This model evaluate the land based on economic and physical
perspectives.
In terms of the economic aspect, the model measures [_Transport Accessibility_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#transport-accessibility-economic)
and the distance to [_Market_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#market-economic).
In terms of the physical aspect, the model considers about
[_Land Condition_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#land-condition-physical)
to respond to rain and produce useful pasture, and
[_Soil Condition_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#soil-condition-physical).

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

#### 3.1.1 Usage

_Transportation Accessibility model_ can be used to evaluate the nearness of
polygons to the two different types of line features. By adjusting the weighted
value, the model can give different outcomes.

#### 3.1.2 Example

In the following example, we use _Transportation Accessibility model_ to measure
the accessibility of IDUs in THLD district to the primary and secondary roads.

The datasets used are listed below:

| ID | File Name     | Data Format | Type    | Description                     |
|----|---------------|-------------|---------|---------------------------------|
| 1  | THLD_poly.shp | vector | polygon | IDUs in the THLD District Assembly |
| 2  | primary_road.shp | vector | point | Primary road in THLD District |
| 3  | secondary_road.shp | vector | point | Secondary road in THLD District |

The two figures below display the specific parameter settings and the output of the model.

|          Parameter Setting         |    Output    |
|------------------------------------------|------------------------------------------|
| <img src="../../../images/m3_TransportationAcces/ParametersSetting.png" alt= "Add data to Map Canvas" width="540">   |  <img src="../../../images/m3_TransportationAcces/Output.png" alt= "Add data to Map Canvas" width="600">   |

In the output map, we used Reds to indicate transportation accessibility of IDUs
in THLD district.
Specifically, the darker the red the higher the traffic accessbility.

### 3.2 Physical - Soil Condition

When evaluate the Soil Condition of the Row Crops land use, three influential indicators on the growth of crops are included in this model: Root Zone Depth, Soil Drainage, and Soil PH at Different Soil Depth. The logic of this model is that, firstly, the model uses Zonal Statistics tool to assign the raster data (three indicators) to the vector polygon, and then uses the Reclassify Field tool to reclassify the assigned value on each the vector data (the reclassification rule should be based on the official documents and agriculture literatures). Finally, the Weight Sum of Fields tool is used to calculate the final score for the Soil Condition. For more information about this model, please click [here](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#soil-condition-physical).

The suitability modeling workflow
To identify the best bobcat patches to conserve you will use a suitability model. A suitability model is comprised of six steps:

Define the problem
Identify and derive the criteria
Transform values to a common scale
Weight the criteria relative to one another and combine
Locate the phenomenon
Analyze the results

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
