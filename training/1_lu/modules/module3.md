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

#### 2.1.1 Goals

In the LUCIS Framework, the first step is to ascertain the goals of the LUCIS. We need to inquire the opinions of stakeholders and separate these values into three categories: 1) agricultural productions, 2) socioeconomic activities, and 3) ecological functions. To be more specific, these three categories can be turned into three land uses correspondingly: 1) agricultural land uses, 2) urban land uses, and 3) conservational land. Therefore, the goals are to identify land use for agricultural land uses, urban land uses, and conservational land.

#### 2.1.2 Objectives

The second step is to ascertain the objectives for each goal. For agricultural land uses and urban land uses, we always consider the suitability, in which two perspectives are commonly used to derive objectives: 1) physical suitability, and 2) economic suitability. In terms of conservational land, we consider the significance of conservational land and two perspectives are commonly used: 1) existing ecological value, and 2) potential ecological value.

#### 2.1.3 Sub-objectives

In this last step, sub-objectives is the specified objectives. For example, if the the objective is to consider the physical suitability perspective (objective) of the residential land use (a goal in urban land uses), one of the sub-objectives can be that to evaluate the proximity of research areas to educational facilities.

### 2.2 The General Workflow of Suitability Modeling

There are three main steps for creating a suitability model:

1. Define Criteria
2. Transform to a Common Suitability Scale
3. Weight the Criteria and Create a Suitability Map

#### **Step 1: Define Criteria**

The first step to create a suitability model is to identify the criteria for the subject of the model. Each criterion identified should be instrumental in reaching the overall goal of the model. For example, if we want to identify the suitable site for an orchard. The following criteria will be considered:

1. Slope;
2. Distance to markets;
3. Land price;
4. Land use types.

#### **Step 2: Transform to a Common Suitability Scale**

Slope, distance to markets, land price and land use type are the criteria that will be used for the suitability model. To proceed, these will be combined. However, mathematically adding the slope, distance to markets, land price and land use type together will result in meaningless values. For example, a location may have a slope value of 5 percent, be 600 meters from a fruit market, and have a land use of 4, representing single family residential. The resulting sum of these values for the location is 609, an irrelevant number. Before the criteria can be added together, the values within each criterion must be transformed to a common suitability scale.

In this example, a 1 to 9 suitability scale will be used. For each value in a criterion, locations with attributes that are most preferred will receive higher suitability values, while locations with the least preferred features will receive lower suitability values. For example, slopes greater than 25 percent will receive a suitability value of 1, slopes that are between 4 percent and 6 percent will be assigned a suitability value of 7, and slopes that are less than 3 percent will have a suitability value of 9.

This transformation process is applied to each value within each criterion identified in the model. The standard for assigning 1 to 9 to values in each criterion should be according to relevant literature or official documents. The values in each criterion are transformed relative to one another to a common suitability scale. The transformed criteria can now be combined.

#### **Step 3: Weight the Criteria and Create a Suitability Map**

Before combination of the transformed values, it may be that one criterion is more important than the others. If that is the case, that criterion will be weighted more than the others. To emphasize the distinction, the transformation process described in step 2 converts the values within a criterion relative to one another. The weighting in this step defines the relative importance of each criterion to one another.

In our example, the weight of each criteria can be:

1. Slope: 10%
2. Distance to markets: 30%
3. Land price: 25%
4. Land use types: 35%

Then, the suitability map can be created by doing symbology on the weighted combination of transformed values. The place with the higher value will be a more suitable site for the orchard.

## 3. Row Crops Model

In this module, we will use Tools to do land suitability modeling.
Each IDU in the THLD area will be assigned to one of the four land uses by
comparing land use scores: Row Crops, Livestock, Timberland, and Urban.

In terms of the scoring process, firstly, we have different decisive factors
in each of the land use, and, under each decisive factor, multiple models will
be applied and generate a weighted score for that decisive factor (with 9 represents
the highest, and 1 represents the lowest) to each IDU. Finally, after we having
a score for each land use on each IDU, the land use with the highest score will
be the final land use for that IDU.

In Row Crops model, we evaluate the suitability of IDUs to grow Row Crops based
on two perspectives: physical and economic. The following figure shows the Row Crops model.

![RowCrops_model](../../../images/RowCrops_model.svg)

In terms of physical suitability, we look for conditions in which land
growing Row Crops can have the optimized production.
In this model, we consider [_Land Condition_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#land-condition-physical)
and [_Soil Condition_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#soil-condition-physical)
as important criteria to determine how many IDUs in THLD district are physically
suitable to grow Row Crops.
In terms of economic suitability, we evaluate the economic efficiency of each IDU
in THLD district.
We expect the land owners who grow Row Crops spend the lowest cost on transportation.
Therefore, we need to ensure lands growing Row Crops have shorter distance to
primary/secondary roads and small/middle/large cities than those without growing
Row Crops.
To achieve that, we choose
[_Transport Accessibility_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#transport-accessibility-economic)
and [_Market_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#market-economic)
as criteria to evaluate how many IDUs in THLD district are economically suitable.

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