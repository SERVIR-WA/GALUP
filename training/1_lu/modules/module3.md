# Module 3 - Create Suitability Models with QGIS Graphical Modeler

**What will you learn from this module?**

- Get to know the Graphical Modeler,
- Learn about the Row Crops model,
- Solve planning-related questions by modeling in the Graphical Modeler.

## 1. Graphical Modeler

## 2. Suitability Modeling

Suitability modeling is the most common application for the LUCIS-OPEN Tools in QGIS and can solve a variety of problems, for examples, you can use Tools to find the best place for a new housing development.

In this model, we will use Tools to do land suitability modeling. There are four types of land uses we need to determine for the IDUs in the THLD area: Row Crops, Livestock, Timberland, and Urban. In each of the land use, we have different decisive factors that help us . And, for each decisive factor, models will be used to evaluate multiple facets consisting of the decisive factor and give a land suitability score to each IDU, representing the suitability of one facet.

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

## 4. Exercises and Post-training Survey

- Please complete the [Exercise 1](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise1.md).
- Please complete the [Exercise 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise2.md).
- Please take this post-training
  [survey](https://ufl.qualtrics.com/jfe/form/SV_9nLiduVDMRRE4t0) (required).
- Please submit your exercises [here](https://github.com/SERVIR-WA/GALUP/issues/new?assignees=muribasterra&labels=exercise+w1m2&milestone=Module+2+Exercises&template=w1m2-exercise-submission.md&title=Module+2+exercises+%5Breplace+with+your+name%5D).

## 5. What's Next?

Module 4 - Aggregate Results to Make Land-Use Decisions.
