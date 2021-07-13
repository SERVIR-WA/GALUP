# Module 4 - Making Land-Use Decisions using the LUCIS Framework

**What will you learn from this module?**

- Understand the framework of LUCIS,
- Get to know the AHP,
- Learn more weights assignment methods in land-use decisions.

## 1. The LUCIS Philosophy

In the planning process, when planners make land-use decisions, the common
problem is the **land-use conflicts** caused by the different values and
motivations of the stakeholder groups that represent the interests of the
three land-use categories.

To solve the **land-use conflict** problem, planners will refer to
the **Land-Use Conflict Identification Strategy** (LUCIS) which is a
***goal-driven*** GIS model that produces a <ins>spatial representation</ins>
of **probable patterns** of future land use. The following diagram shows
the general process of the LUCIS Framework.

![lucis_workflow](../../../img/dgrm/lucis_workflow.svg)

### The general workflow of LUCIS

1. [Define goals, objectives, and sub-objectives](https://tinyurl.com/wtm9ddj2)
2. Dataset Preparation
3. [Suitability Modeling](https://tinyurl.com/yxvmhy68)
4. [Analytic Hierarchy Process (AHP)]()

This module will introduce **Define Goals and Objectives and Sub-objectives**
and **Analytic Hierarchy Process (AHP)**. Dataset preparation will not be
elaborated in this module, and recall that the suitability modeling has been
introduced in Module 3.

### 1.1 Define Goals, Objectives and Sub-objectives

![hierarchy_workflow](../../../img/dgrm/lucis_hierarchy_workflow.svg)

As shown in the figure above, **Goals**, **Objectives** and **Sub-objectives**
are a hierarchical set of statements, they are defined in LUCIS as follows:

1. Goals: describe what is to be accomplished;
2. Objectives: describe how each accomplishment is to be achieved;
3. Sub-objectives: supporting statements for goals and objectives.

#### 1.1.1 Goal

In the LUCIS Framework, the first step is to define the **goals** of the
project. Three categories are employed to find the goal: 1) *agricultural
productions*, 2) *socioeconomic activities*, and 3) *ecological functions*.
To define a goal, we need to:

1. Inquire the intents of stakeholders;
2. Sort out the intents into agricultural productions, socioeconomic
   activities, and ecological functions.

Specifically, these three categories will be turned into three land uses
categories correspondingly: 1) **agricultural land uses**,
2) **urban land uses**, and 3) **conservational land use**. In other words,
we will make sure our goal fall into these three land-use categories (e.g.,
to develop commercial land use for emerging industries in a city).

In real world setting, a broad range of time and effort is normally devoted
to the development of goals, but it is well worth to spend time on defining
explicit goals.

#### 1.1.2 Objective

After we have goals, we need to develop the objectives for each goal. As
described by its definition, objectives are set to describe how each goal is
to be achieved. Since three land uses categories are used in LUCIS, we use
different objectives for each land use category.

For **agricultural** and **urban land uses**, we always consider two
objectives:

- Physical suitability
- Economic suitability

In terms of conservational land, we consider the significance of conservational
land and two objectives are commonly used:

- Existing ecological value
- Potential ecological value

#### 1.1.3 Sub-objective

Generally, sub-objectives are a group of statements that can help to
evaluate the objective. Note that **not** all objectives are required to
have sub-objectives if the objective is self-evident.

### 1.2 Example

In this section, we will use an example of THLD area to illustrate the
workflow of defining **Goals**, **Objectives** and **Sub-objectives** in LUCIS.

#### 1.1.1 Define Goals

As a planner, first we need to ask the intents of stakeholders. Let's say one
intent of the stakeholders is to <ins>***develop a land-use scenarios for THLD
area to accommodate the population projected for the year 2050***</ins>.

We can distill some goals from this intent according to the three
categories: 1) *agricultural productions*, 2) *socioeconomic activities*,
and 3) *ecological functions*.

| Categories               | Land use categories              | Possible goal                                                                     |
| ------------------------ | ---------------------- | --------------------------------------------------------------------------------- |
| Agricultural productions | Agricultural land uses | Increase the food production for future population growth                         |
| Socioeconomic activities | Urban land uses        | Develop more residential land uses in THLD area to solve the future housing issue |
| Ecological functions     | Conservational land    | Protect conservational land                                                       |

#### 1.2.2 Define Objectives and sub

We use the goal in *Socioeconomic activities*, which is **Develop more
residential land uses in THLD area to solve the future population growth**, as
an example. The possible objectives and sub-objectives are represented in the
following chart:

<img src="../../../img/qgm/algtbl/m4_Goal_obj_sub.svg" alt= "goal_obj_sub" width="600">

We want to develop objectives for the residential land use goal to accommodate
the future population growth. Considering the physical suitability aspect,
we have four sub-objectives. For the economic objective, we have five
sub-objectives.
## 2. AHP
The LUCIS uses Analytic Hierarchy Process (AHP) to arrange the goals,
objectives, sub-objectives, and stakeholders in a hierarchy for two purposes:
1. AHP provides an overall view of the complex relationships inherent
   in the situation.
2. AHP helps the decision-maker assess whether the issues in each level
   are of the same order of magnitude so that he can compare such homogeneous
   elements accurately.

When advising how vital agricultural productions, socioeconomic activities,
and ecological functions are in a district, the decision-making process usually
involves five stakeholders to determine the land use developing direction of
the future.
These stakeholders include farmers, property developers, local government,
non-governmental organizations (NGOs), and the central government.
The decision-making intends to decide the preference of three land-use types:
agricultural land uses, urban land uses, and conservational land.

<img src="../../../img/dgrm/" alt= "RowCrops_model" width="400">

The first step of AHP is to structure the intention as a hierarchy.
In the first level is the overall goal of land-use preferences.
In the second level are the five stakeholders who have interests in
land development, and the third level are the three land use types which are
to be evaluated by each stakeholders in the second level. 

The second step is the elicitation of pairwise comparison judgments.
The elements to be compared pairwise are the different land-use types
for which one is more important in future land development according to
each stakeholder in level 2.
The scale to use in making the judgments is given in table that land-use types
are compared using values from 1 (equally important) to 9 (extremely important).
Thus there will be five 3 X 3 matrices of judgments since there are
five elements in level 2, and 3 land-use types to be pairwise compared
for each element.
Then, the pairwise values (1–9) are entered in the cells of five matrices.
>  :bulb: **Why judgments are given in the form of paired comparisons**<br>
>  The most effective way to concentrate judgment is to take a pair of
>  elements and compare them on a single property without concern for other
>  properties or other elements.
>  This is why paired comparisons in combination with
>  the hierarchical structure are useful in deriving measurement.

Again, the matrices contain the judgments of the stakeholders involved.
To understand the judgments, a brief description of
each stakeholder's interests is shown below.

Farmers want to protect their interests in the district to have enough
agricultural land for future development. Therefore, farmers would like
to assign land-use suitability for each purpose as follows:

Property developers want to optimize their interests during the process of
developing the district that they wish urban land could occupy the most of area
in the district.
Therefore, property developers would like to assign land-use suitability
for each purpose as follows:

The local government wishes to develop more urban land in the future,
whereas their straitened financial circumstances do not allow them to
sustain too many urban infrastructure facilities.
Therefore, the local government would like to assign land-use suitability for
each purpose as follows:

The non-governmental organization (NGO) has focused on forest conservation in
this district for many years, and they wish the conservation land could
cover more closed forests.
Therefore, the NGO would like to assign land-use suitability for each purpose
as follows:

The central government predicts this district will have relatively
large population growth in the future, and they wish to introduce
manufacturing industries funded by foreign investment in this district.
The central government believes this district demands more urban land
in the future.
Therefore, the central government would like to assign land-use suitability
for each purpose as follows:


The third step is to establish the composite or global priorities of the houses.
In this case, opinions from each stakeholder are viewed as equally important.
When arranging the elements in the second level into a matrix and comparing
them one by one for the relative importance of the elements concerning
the overall goal, each of the five stakeholders will receive
the same priority of 20%.


The table lays out the local priorities of land-use types with respect to
each stakeholder in a matrix and multiply each column of vectors by
the priority of the corresponding stakeholder and add across each row
which results in the desired vector of land-ues importance dgree in the table. 





## 3. Row Crops Models

The intent of the row crops model is to identify lands most suitable for growing row crops.
The suitability of the land to grow row crops depends on two aspects: whether this land has relatively appropriate physical conditions to optimize the production; and how much development or transportation costs it can save compared with others.
Therefore, this model set up two objectives, physical suitability and economic suitability, for measuring the success of choosing a suitable land.
The following figure shows the Row Crops model.

<img src="../../../img/dgrm/RowCrops_model.svg" alt= "RowCrops_model" width="400">

In terms of physical suitability, we look for conditions in which land
growing Row Crops can have the optimized production.
In this objectives, we consider [_Landscape Condition_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#land-condition-physical)
and [_Soil Condition_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#soil-condition-physical)
as important criteria to determine how many IDUs in THLD district are physically suitable to grow Row Crops.

In terms of economic suitability, we evaluate the economic efficiency of each IDU in THLD district.
We expect the land owners who grow Row Crops spend the lowest cost on transportation.
Therefore, we need to ensure lands growing Row Crops have shorter distance to
primary/secondary roads and small/middle/large cities than those without growing Row Crops.
To achieve that, we choose
[_Transport Accessibility_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#transport-accessibility-economic)
and [_Market_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#market-economic)
as criteria to evaluate how many IDUs in THLD district are economically suitable.



## 4. Weighting Method


