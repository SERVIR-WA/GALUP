# Module 3 - Create Suitability Models with QGIS Graphical Modeler

**What will you learn from this module?**

- Get to know the Graphical Modeler,
- Learn about the Row Crops model,
- Solve planning-related questions by modeling in the Graphical Modeler.

## 1. Introduction to QGIS Graphical Modeler

Please see this video:<br>
<a href="https://www.youtube.com/watch?v=eZb5VLTc9-o">
  <img src="../../../images/video_frames/QGIS%20Model%20Builder.png" alt= "GMtutorial" width="800">
</a>

## 2. Suitability Modeling

Suitability is a measure of the relative degree to which a land unit is suitable for a specified purpose. The decision on suitability is based strictly on its current condition and the context in which it is found. It neither anticipates nor requires any change for the assignment of a suitability score. In many cases, suitability is measured on a scale of 1 to 9, with 1 representing low suitability and 9 representing high suitability.
Suitability modeling is a process consisting of a series of GIS tools to determine suitability. In this workshop, we present a method of modeling suitability in QGIS with the **LUCIS-OPEN Tools for QGIS**.

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

1. [Define criteria](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module3.md#step-1-define-criteria)
2. [Transform to a common suitability scale](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module3.md#step-2-transform-to-a-common-suitability-scale)
3. [Weight the criteria and create a suitability map](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module3.md#step-3-weight-the-criteria-and-create-a-suitability-map)

#### Step 1: Define Criteria

The first step to create a suitability model is to identify the criteria for the subject of the model. Each criterion identified should be instrumental in reaching the overall goal of the model. For example, if we want to identify a suitable site for an orchard. We can consider the following criteria:

- Slope
- Distance to markets
- Land price
- Land use types

#### Step 2: Transform to a Common Suitability Scale

The four criteria mentioned above are measured in their specific scales. The final suitability will combine them together. However, simply adding their values is meaningless. For example, a site is on a 5 percent slope, 600 meters from a fruit market, and with a land use of 34, representing single-family residential. The sum of these values is 639,  which makes no sense. Therefore, before combining the criteria, we must transform the values of each criterion from its original scale to a common suitability scale.

In this example, a 1 to 9 suitability scale will be used. For each value in a criterion, locations with attributes that are most preferred will receive higher suitability values, while locations with the least preferred features will receive lower suitability values. For example, slopes greater than 25 percent will receive a suitability value of 1, slopes that are between 4 percent and 6 percent will be assigned a suitability value of 7, and slopes that are less than 3 percent will have a suitability value of 9.

The original values in every criterion should be transformed into this common scale from 1 to 9. And such transformations should follow relevant literature or guidelines. The transformed criteria can now be combined.

#### Step 3: Weight the Criteria and Create a Suitability Map

Before combination of the transformed values, it may be that one criterion is more important than the others. If that is the case, that criterion will be weighted more than the others. To emphasize the distinction, the transformation process described in step 2 converts the values within a criterion relative to one another. The weighting in this step defines the relative importance of each criterion to one another.

In our example, the weight of each criteria can be:

- Slope: 10%
- Distance to markets: 30%
- Land price: 25%
- Land use types: 35%

Then, the suitability map can be created by doing symbology on the weighted combination of transformed values. The place with the higher value will be a more suitable site for the orchard.

## 3. Row Crops Model

In this module, we will use **LUCIS-Open Tools for QGIS** to create suitability models.

Each IDU in the THLD area will be assigned to one of the four land uses by
comparing land use scores: Row Crops, Livestock, Timberland, and Urban.
In Row Crops model, we evaluate the IDUs' suitability in growing Row Crops based
on two objectives: physical suitability and economic suitability.
The following figure shows the Row Crops model.

<img src="../../../images/RowCrops_model.svg" alt= "RowCrops_model" width="400">

In terms of physical suitability, we look for conditions in which land
growing Row Crops can have the optimized production.
In this objectives, we consider [_Land Condition_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#land-condition-physical)
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

In this module, we will introduce two models and two for exercise.

### 3.1 Transportation Accessibility

_Transportation Accessibility_ model is a sub-objective of the economic objectives. 
_Transportation Accessibility_ model is used to compare the potential
transportation costs in each IDUs by measuring its distance to traffic roads.
We assume the IDUs with higher accessibility require less transportation cost to
deliver goods to outside.

1. By using [_Distance to Line Features_](https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-line-features),
this model calculate the shorest distance from each IDU to the primary and
secondary roads and store the values in two different fields.
2. Then the model use [_Rescale Field Linearly_](https://github.com/SERVIR-WA/GALUP/wiki/Tools#rescale-field-linearly)
to transform values in fields to specified continuous scales (i.e., 1 to 9 scale).
3. Finally, using [_Weight Sum of Fields_](https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields)
to multiply the rescaled fields with weighted value and sum them up,
the model can create a index for each IDU to measure their accessibility to
the primary and secondary roads.
You can check the _Input parameters_ of this model
[here](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#transport-accessibility-economic).

#### 3.1.1 Dataset

In the following example, we use _Transportation Accessibility_ model to measure
the accessibility of IDUs in THLD district to the primary and secondary roads.

The datasets used are listed below:

| ID | File Name     | Data Format | Type    | Description                     |
|----|---------------|-------------|---------|---------------------------------|
| 1  | THLD_poly.shp | vector | polygon | IDUs in the THLD District Assembly |
| 2  | primary_road.shp | vector | point | Primary road in THLD District |
| 3  | secondary_road.shp | vector | point | Secondary road in THLD District |

#### 3.1.2 Tools used in the model

1. [Distance to Line Features](https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-line-features)
2. [Rescale Field Linearly](https://github.com/SERVIR-WA/GALUP/wiki/Tools#rescale-field-linearly)
3. [Weight Sum of Fields](https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields)

#### 3.1.3 Model and Model Results

|          Model         |
|------------------------------------------|
| ![TAM](../../../images/Model%20Map/Transportation_Accessibility.svg) |

| Distance to Major Roads                                                               | Res Major Roads                                                                                             | Distance to Sec Roads | Res Secondary Roads | Weighted Sum MR & SR                                                |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------|---------------------|---------------------------------------------------------------------|
| 1.Input layer: Input Polygon <br> 2.Line layer: Major Roads <br> 3.Output column name: Dis_toMR | 1.Input layer: 'Output layer' from algorithm 'Distance to Major Roads' <br> 2.Field to rescale: Dis_toMR <br> 3.Start value: 15000 <br> 4.End value: 0 <br> 6.New minimum: 1 <br> 7.New maximum: 9 <br> 8.Output field name: DisMR_R |    1.Input layer: 'Output layer' from algorithm 'Res Major Roads' <br> 2.Line layer: Secondary Roads <br> 3.Output column name: Dis_toR     |    1.Input layer: 'Output layer' from algorithm 'Distance to Sec Roads' <br> 2.Field to rescale: Dis_toR <br> 3.Start value: 5000 <br> 4.End value: 0 <br> 6.New minimum: 1 <br> 7.New maximum: 9 <br> 8.Output field name: DisR_R | 1.Input layer: 'Output layer' from algorithm 'Res Secondary Roads' <br> 2.Fields: DisMR_R;DisR_R <br> 3.Weights: Using model input: Weighted Value <br> 4.Output field name: rcrp_trans <br> 5.Output layer: rcrp_TransportAccessibility |

|          Parameter Setting         |    Output    |
|------------------------------------------|------------------------------------------|
| <img src="../../../images/m3_TransportationAcces/ParametersSetting.png" alt= "Add data to Map Canvas" width="540">   |  <img src="../../../images/m3_TransportationAcces/Output.png" alt= "Add data to Map Canvas" width="600">   |

In the output map, we used Reds to indicate transportation accessibility of IDUs
in THLD district.
Specifically, the darker the red the higher the traffic accessibility.

### 3.2 Soil Condition

Soil condition is a sub-objective of the physical condition objective. The reason that we set this as a sub-objective is that soil condition can affect the row crops plantation and production (e.g., drainage will affect the plantation of crops, and soil pH can affect the production of the crops).

After defining the soil condition as a sub-objective, we need to identify specific criteria. Here, in consideration of the possible criterion and the data availability of the THLD area, we identify 1) **Drainage**, 2) **Root Zone Depth**, and 3) **Soil pH** as three criteria in the model.

Then, we assign new values to the old values of the three criteria (the rule will be based on literature in relevant agricultural fields).

The last step is to proceed the value combination. Before combining values, different weights will be assigned to each criteria (weight value will be based on literature in relevant agricultural fields).

#### 3.2.1 Data

The datasets used are listed below:

| ID | File Name     | Data Format | Type    | Description                                                 |
|--- |---------------|-------------|---------|-------------------------------------------------------------|
| 1  | THLD_poly.shp | vector      | polygon | IDUs in the THLD District Assembly |
| 2  | RZD_THLD100   | raster      | tiff    | [Root Zone Depth](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/c77d1209-56e9-4cac-b76e-bbf6c7e3a617) |
| 3  | Drain_THLD100 | raster      | tiff    | [Soil Drainage](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/953d0964-6746-489a-a8d1-f188595516a9)     |
| 4  | SD0_5          | raster      | tiff    | Soil pH value at 0cm-5cm soil depth*      |
| 5  | SD5_15         | raster      | tiff    | Soil pH value at 5cm-15cm soil depth*     |
| 6  | SD15_30        | raster      | tiff    | Soil pH value at 15cm-30cm soil depth*    |
| 7  | SD30_60        | raster      | tiff    | Soil pH value at 30cm-60cm soil depth*    |
| 8  | SD60_100       | raster      | tiff    | Soil pH value at 60cm-100cm soil depth*   |
| 9  | SD100_200      | raster      | tiff    | Soil pH value at 100cm-200cm soil depth*  |

\*: [Soil pH data source](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/a3364e47-9229-4a6d-aed2-487fd7e4dccc): the soil pH value varies in different soil depth at the same location.

#### 3.2.2 Tools Used in the Model

1. [Reclassify Field](https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field)
2. [Weight Sum of Fields](https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields)
3. [Zonal Statistics](https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics)

 The logic of this model is:

  1. Use **Zonal Statistics** tool to calculate the mean value of raster data (three criteria consist of eight raster layers) to each IDU;
  2. Then, use the **Reclassify Field** tool to reclassify the assigned value on each the vector data (the reclassification rule should be based on the official documents and agriculture literatures);
  3. Finally, after iterating the two steps above for each criterion, we use the **Weight Sum of Fields** tool to calculate the final suitability. <br>
  Note: 
  
For more information about this model, please click [here](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#soil-condition-physical).

#### 3.2.3 Model and Model Results

|          Model         |
|------------------------------------------|
| ![SCM](../../../images/Model%20Map/Soil_Condition.svg) |

|          Parameter Setting         |    Output Map   |
|------------------------------------------|------------------------------------------|
| ![PS1](../../../images/SoilCondition/pa_set.png) | ![am1](../../../images/SoilCondition/symbology_sc.png) |

## 4. Exercises and Post-training Survey

- Please complete the [Exercise 1](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise1.md).
- Please complete the [Exercise 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m3_exercise2.md#module-3---exercise-2).
- Please take this post-training
  [survey](https://ufl.qualtrics.com/jfe/form/SV_9nLiduVDMRRE4t0) (required).
- Please submit your exercises [here](https://github.com/SERVIR-WA/GALUP/issues/new?assignees=muribasterra&labels=exercise+w1m2&milestone=Module+2+Exercises&template=w1m2-exercise-submission.md&title=Module+2+exercises+%5Breplace+with+your+name%5D).

## 5. What's Next?

Module 4 - Aggregate Results to Make Land-Use Decisions.
