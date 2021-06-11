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

## 4. Exercises and Post-training Survey

- Please complete the [Exercise 1](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise1.md).
- Please complete the [Exercise 2](https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise2.md).
- Please take this post-training
  [survey](https://ufl.qualtrics.com/jfe/form/SV_9nLiduVDMRRE4t0) (required).
- Please submit your exercises [here](https://github.com/SERVIR-WA/GALUP/issues/new?assignees=muribasterra&labels=exercise+w1m2&milestone=Module+2+Exercises&template=w1m2-exercise-submission.md&title=Module+2+exercises+%5Breplace+with+your+name%5D).

## 5. What's Next?

Module 4 - Aggregate Results to Make Land-Use Decisions.
