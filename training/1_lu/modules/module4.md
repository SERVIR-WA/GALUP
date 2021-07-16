# Module 4 - Making Land-Use Decisions using the LUCIS Framework

**What will you learn from this module?**

- Understand the framework of LUCIS,
- Get to know the AHP,
- Learn more weights assignment methods in land-use decisions.

## 1. The LUCIS Philosophy

In the planning process, when planners make land-use decisions, the common
problem is the **land-use conflicts** caused by the different values and
motivations of the stakeholder groups that represent the interests of the three
land-use categories: 1) **agricultural land uses**, 2) **urban land uses**,
and 3) **conservational land use**.

To identify the **land-use conflicts**, planners will refer to
the **Land-Use Conflict Identification Strategy** (LUCIS) which is a
***goal-driven*** GIS model that produces a <ins>spatial representation</ins>
of **probable patterns** of future land use.

### LUCIS Workflow:

1. [Define goals, objectives, and sub-objectives](https://tinyurl.com/wtm9ddj2)
2. Dataset Preparation
3. [Suitability Modeling](https://tinyurl.com/yxvmhy68)
4. [Analytic Hierarchy Process (AHP)]()

![lucis_workflow](../../../img/dgrm/lucis_workflow.svg)

The diagram above shows the general process of the LUCIS Framework. In this
framework, planners will first inquire **the values or interests of
stakeholders**. Agriculture stakeholders might include members of the local
farm bureau or a cattlemen and ranchers group. Urban development
stakeholders might include representatives of the homebuilders and real
estate associations. Conservation interests might be represented by members
of locally active conservation organizations.

Next, planners will define **goals** by sorting out these values and interests
into three categories (*agricultural productions*, *socioeconomic activities*,
and *ecological functions*) which match three land uses categories respectively: **agricultural land uses**, **urban land uses**, and **conservational land**.

Then, after having goals, different **objectives** according to different
land-use goals will be developed to help to accomplish the goals. Generally,
for **agricultural** and **urban land uses**, we always consider two
objectives:

- Physical suitability
- Economic suitability

In terms of **conservational land**, we consider the significance of
conservational land and two objectives are commonly used:

- Existing ecological value
- Potential ecological value

**Sub-objectives** are a group of statements that can help to evaluate the
objective. Single utility assignment will be conducted in sub-objectives.
Utility values are the units by which suitability is measured or assigned.
The assignment of utility values for individual features in a single layer
of spatial data, the foundation upon which GIS suitability modeling rests,
is called a **single utility assignment (SUA)**. The assignment of utility
values that represent the suitability of particular features in a data layer
for a single distinct purpose is accomplished by the GIS analyst, experts
in the field, or stakeholders.

Data preparation will be conducted according to the data requirements of
**Sub-objectives**.

**Analytic Hierarchy Process (AHP)** is used to decide the preference of goals,
objectives, or sub-objectives by arranging them and stakeholders in a hierarchy
and doing paired comparisons. AHP will turn suitability to preference
when choices are made about the relative weights of the goals within a
category. The advantages of the AHP method are its simplicity and its potential
to support participation by a wide range of individuals, including experts,
community leaders, the general public, and other stakeholders.

Finally, in the last step, after we getting the preference results from AHP,
we can identify the land-use conflict areas by using normalized and collapsed preference values.

This module will introduce **Define Goals and Objectives and Sub-objectives**
and **Analytic Hierarchy Process (AHP)**. Dataset preparation will not be
elaborated in this module, and recall that the suitability modeling has been
introduced in Module 3.

### 1.2 Example

In this section, we will use an example of THLD area to illustrate the
workflow of defining **Goals**, **Objectives** and **Sub-objectives** in LUCIS.

#### 1.1.1 Define Goals

As a planner, first we need to ask the intents of stakeholders. Let's say one
intent of the stakeholders is to <ins>***develop a land-use scenarios for THLD
area to accommodate the population projected for the year 2035***</ins>.

<img src="../../../img/plot/THLD_pop2035_projection.svg" alt= "pop_pro" width="500">

We can distill a goal from this intent for *socioeconomic activities*. As
shown in the THLD Area Population Projection by 2035 chart above, the two
dotted lines are two scenarios representing the upper limit and lower limit of
the population projection by 2035 respectively. The middle solid line is
the general scenario. we can see there would be 71,060 people in THLD area.
Therefore, one possible goal is to **develop more residential land uses in THLD
area to solve the future housing issue**.

| Categories              | Land use categories     | Possible goal                                                                      |
| ----------------------- | ----------------------- | ---------------------------------------------------------------------------------- |
| Socioeconomic activities | Urban land uses | Develop more residential land uses in THLD area to solve the future housing issue. |

#### 1.2.2 Define Objectives and Sub-objectives

We use the goal in *Socioeconomic activities*, which is **Develop more
residential land uses in THLD area to solve the future housing issue**, as
an example. The possible objectives and sub-objectives are represented in the
following chart and the hierarchy relationship between goal, objectives and
sub-objectives is denoted by the following map:

 |  Goal, Objectives, Sub-objectives        |    Hierarchy Map   |
|:------------------------------------------:|:------------------------------------------:|
| <img src="../../../img/qgm/algtbl/m4_Goal_obj_sub.svg" alt= "goal_obj_sub" width="800"> | <img src="../../../img/dgrm/m4_hierarchy_goal_obj_sub.svg" alt= "goal_obj_sub" width="800"> |

> :bulb: Note:<br>
> The goal, objectives, and sub-objectives are denoted by the numbers in the
> hierarchy map.

We want to develop objectives for the residential land use goal to accommodate
the future population growth. Considering the physical suitability aspect,
we have four sub-objectives. For the economic objective, we have five
sub-objectives.

<<<<<<< HEAD
## 2. AHP
The LUCIS uses Analytic Hierarchy Process (AHP) to arrange the goals,
=======
## 2. Analytic Hierarchy Process

The [Analytic Hierarchy Process](https://en.wikipedia.org/w/index.php?title=Analytic_hierarchy_process&oldid=1026677776)
(AHP) is a structured technique for organizing and analyzing complex decisions,
which is based on the solution of <img src="../../../img/eqn/AHP.svg" alt= "AHP equation" width="80">.

The LUCIS uses AHP to arrange the goals,
>>>>>>> cb45b117ea9f68fa5c3f16e7d6ba7eb0a5924930
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
These stakeholders include five people representing the farmer,
the property developer, the government official,
the Non-Governmental Organization (NGO), and the homeowner.
The decision-making intends to decide the preference of three land-use types:
agricultural land uses, urban land uses, and conservational land.

<img src="../../../img/dgrm/lucis_AHP_structure.svg" alt= "RowCrops_model" width="650">

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

<img src="../../../img/qgm/algtbl/m4_ahp_Intensityofimportance.svg" alt= "RowCrops_model" width="600">

Again, the matrices contain the judgments of the stakeholders involved.
To understand the judgments, a brief description of
each stakeholder's interests is shown below:
1. Farmer wants to protect farmers' interests in the district to have enough
   agricultural land for future development.
2. Property developer wants to optimize developers' interests during
   the process of developing the district that he wish urban land could
   occupy the most of area in the district.
3. Government official wishes to develop more urban land in the future,
   whereas the straitened financial circumstances do not allow government to
   sustain too many urban infrastructure facilities.
4. Non-governmental organization (NGO) has focused on forest conservation in
   this district for many years, and NGO wishes the conservation land could
   cover more closed forests.
5. Homeowner wants to have more convenient transportation and better
   living condition.
   However, he indicates that agricultural land is equally important as
   urban land since many residents are taking agricultural production for
   a living.

Therefore, the five stakeholders would like
to assign land-use suitability for each purpose as follows:

<img src="../../../img/qgm/algtbl/m4_ahp_localprioritytable.svg" alt= "RowCrops_model" width="800">

The third step is to establish the global priorities of
the suitable land use preference.
In this case, opinions from each stakeholder are viewed as equally important.
When arranging the elements in the second level into a matrix and comparing
them one by one for the relative importance of the elements concerning
the overall goal, each of the five stakeholders will receive
the same priority of 20%.

<img src="../../../img/qgm/algtbl/m4_ahp_prioritytable.svg" alt= "RowCrops_model" width="700">

The table lays out the local priorities of land-use types with respect to
each stakeholder in a matrix and multiply each column of vectors by
the priority of the corresponding stakeholder and add across each row
which results in the desired vector of land-ues importance dgree in the table.
In this case, Urban land use had the largest priority of land development in
this district.
Agricultural land use was less desirable than urban land use, and
Conservation land was the least important in the three land-use types.

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


