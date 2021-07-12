# Module 4 - Making Land-Use Decisions using the LUCIS Framework

**What will you learn from this module?**

- Understand the general workflow of suitability modeling,
- Get to know the QGIS **Graphical Modeler**,
- Learn how to build suitability models with LUCIS-OPEN tools for QGIS in the
  Graphical Modeler,
- Learn the details and the logic behind the suitability models for
  ***Row Crops***.

## 1. The LUCIS Philosophy

The **Land-Use Conflict Identification Strategy** (LUCIS) is a
***goal-driven*** GIS model that produces a <ins>spatial representation</ins>
of **probable patterns** of future land use.
The following diagram shows the general process of the LUCIS Framework.

![lucis_workflow](../../../img/dgrm/lucis_workflow.svg)

You will recall that the broad land-use categories LUCIS employs are agriculture, conservation, and urban, and each of these categories are broken down into more specific uses; for example, urban is comprised of industrial, office and commercial, retail, and residential. Objectives and sub-objectives capture the evaluation criteria, for example, identification of quiet areas for residential use.

The fundamental premise of LUCIS is that land-use conflict is inevitable because of the different values and motivations of the stakeholder groups that represent the interests of the three land-use categories. In order to identify where that future land-use conflict is likely to occur, it is essential that the biases of each stakeholder group be captured when suitabilities are being determined.

In real-world settings—for instance, the development of a county’s future land-use plan—bias can be acknowledged by asking representatives of each stakeholder group to participate in the assignment of suitability values. Conservation interests might be represented by members of locally active conservation organizations, urban development stakeholders might include representatives of the homebuilders and real estate associations, and agriculture stakeholders might include members of the local farm bureau or a cattlemen and ranchers group.

Once the three suitability values, and later, preference values, are determined, potential future land-use conflict can be identified. The results of this approach are revealing and realistic because the biases of each group are represented.

### 1.1 Hierarchical Structure of LUCIS

Goals and objectives are a hierarchical set of statements that first define
what is to be accomplished (goal), and second, define how each accomplishment
is to be achieved (objectives) (Carr & Zwick, 2007). Goals and objectives are occasionally enhanced by a third
or even fourth tier of supporting statements (sub-objectives) (Lyle, 1985; Steiner, 2000).

A broad range of time and effort is normally devoted to the development of goals and objectives


In the LUCIS Framework, the first step is to ascertain the **goals** of the project.
We need to inquire the intents of stakeholders and separate their intents into
three categories: 1) agricultural productions, 2) socioeconomic activities, and 3) ecological functions.
Specifically, these three categories can be turned into three land uses
correspondingly: 1) agricultural land uses, 2) urban land uses, and 3) conservational land.
Therefore, the goals are to identify land use for agricultural land uses, urban
land uses, and conservational land.

For example, if one intent of the stakeholders is to develop a land-use scenarios for THLD area to accommodate the population projected for the year 2050.

We can distill some goals from this intent according to the three categories: 1) agricultural productions, 2) socioeconomic activities, and 3) ecological functions. One possible goal for the agricultural productions is to plan for the agricultural land uses to increase the food production for future population growth. In terms of the socioeconomic activities, the possible goal can be that to develop more residential land uses in THLD area to solve the future housing issue. For the ecological functions, goals for protecting conservational land should be considered.



The second step is to ascertain the objectives for each goal. For agricultural land uses and urban land uses, we always consider the suitability, in which two perspectives are commonly used to derive objectives: 1) physical suitability, and 2) economic suitability. In terms of conservational land, we consider the significance of conservational land and two perspectives are commonly used: 1) existing ecological value, and 2) potential ecological value.

If we continue to use the example mentioned before, for instance, we want to develop objectives for the residential land use goal to accommodate the future population growth. Considering the physical suitability aspect, one objective for physical suitability is public transportation accessibility since the pubic transit is an important amenity for residential area. As for economic suitability aspect, land price should be an objective for residential land use.


In this last step, sub-objectives is the specified objectives. For example, if the the objective is to consider the physical suitability perspective (objective) of the residential land use (a goal in urban land uses), one of the sub-objectives can be that to evaluate the proximity of research areas to educational facilities. Note that not all objectives are required to have sub-objectives.

To continue think about the example of residential land use goal. Now we are supposed to develop specific sub-objectives for our objectives. Let's say we want to set specific sub-objectives for public transportation accessibility, the distance to public bus stops and distance to subway stations are two suitable sub-objectives. Whereas, for the land price object, it does not necessarily to have sub-objectives as land price is an objective that is already measured by price.

### 1.2 Example

## 2. AHP

## 3. Row Crops Models

Each IDU in the THLD area will be assigned to one of the four land uses by
comparing land use scores: Row Crops, Livestock, Timberland, and Urban.

In Row Crops model, we evaluate the IDUs' suitability in growing Row Crops based
on two objectives: physical suitability and economic suitability.
The following figure shows the Row Crops model.

<img src="../../../img/dgrm/RowCrops_model.svg" alt= "RowCrops_model" width="400">


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




The intent of the row crops model is to identify lands most suitable for growing row crops.
The suitability of the land to grow row crops depends on two aspects: whether this land has relatively appropriate physical conditions to optimize the production; and how much development or transportation costs it can save compared with others.
Therefore, this model set up two objectives, physical suitability and economic suitability, for measuring the success of choosing a suitable land.
The following figure shows the Row Crops model.

<img src="../../../img/dgrm/RowCrops_model.svg" alt= "RowCrops_model" width="400">

In terms of physical suitability, we look for conditions in which land
growing Row Crops can have the optimized production.
In this objectives, we consider [_Landscape Condition_](https://github.com/SERVIR-WA/GALUP/wiki/models_ag#land-condition-physical)
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

## 4. Weighting Method
