.. role:: raw-html-m2r(raw)
   :format: html


Module 2 - Introduction to LUCIS-OPEN Tools for QGIS
====================================================

**What will you learn from this module?**


* Get to know the LUCIS-OPEN Tools for QGIS,
* Learn when and how to use different tools,
* Use the tools to answer planning-related questions.

1. Density of Line Features
---------------------------

*Density of Line Features* calculates the line density in a polygon (i.e., the
total length of line features that fall within a polygon feature divided by the
polygon's area).
The polygon features (i.e., Input layer) and line features (i.e., Line layer)
are two required parameters for using this tool. There are five additional
parameters that can be specified, which are outlined
`here <https://github.com/SERVIR-WA/GALUP/wiki/Tools#density-of-line-features>`_.

1.1 Usage
^^^^^^^^^

This tool is often used to calculate the density of linear features, such as
roads and rivers, in a polygon area. Results of this tool can help us
understand the magnitude of a certain phenomenon within a territory.

Only the portion of a line within the neighborhood (a polygon feature or a
radius around a polygon feature) is considered when calculating the density.
If no lines fall within the neighborhood of a particular polygon, a
"\ `Null value <https://www.cadlinecommunity.co.uk/hc/en-us/articles/360013744338-QGIS-NULL-Values#:~:text=By%20default%2C%20when%20you%20browse,will%20show%20a%20NULL%20value>`_\ "
will be given to that polygon.

Search radius, if specified, will be used to calculate the line density by
using the total length of line features fall within the area of a circle (the
centroid of a polygon as the center and the search radius as the radius)
divided by the circle's area.

`Cell size <https://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-images/cell-size-of-raster-data.htm>`_
is used to calculate the total length of line features fall within the area of
a circle by rasterizing those line features.
The smaller the value, the more precise the outcome, but the longer time will
be taken to run the tool.

1.2 Example
^^^^^^^^^^^

In the following example, we use this tool to calculate the density of
underground water veins in the THLD area. The datasets used are listed below:

.. list-table::
   :header-rows: 1

   * - ID
     - File Name
     - Data Format
     - Type
     - Description
   * - 1
     - THLD_poly.shp
     - vector
     - polygon
     - IDUs\ :raw-html-m2r:`<sup>1</sup>` in the THLD\ :raw-html-m2r:`<sup>2</sup>` District Assembly
   * - 2
     - Hydro.shp
     - vector
     - line
     - Underground water veins in the THLD District


1: Integrated Decision Unit. :raw-html-m2r:`<br>`
2: Twifo-Hemang-Lower-Denkyira.

The two figures below display the specific parameter settings
 and the output of the tool.\ :raw-html-m2r:`<br>`

..

   :pushpin: Check the details of an image:\ :raw-html-m2r:`<br>`
   If you can't see the image clearly, click on the image to view it in a
   new page, which will show the image in its original size.


.. list-table::
   :header-rows: 1

   * - Parameter Setting
     - Output Map
   * - 
     .. image:: ../../../img/gui/window/m2_linedensity_ParametersSetting.png
        :target: ../../../img/gui/window/m2_linedensity_ParametersSetting.png
        :alt: PS1
     
     - 
     .. image:: ../../../img/map/m2_linedensity_Output.png
        :target: ../../../img/map/m2_linedensity_Output.png
        :alt: am1
     


In the output map, we used **Blues** `Graduated Color <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module1.md#33-change-symbology-of-a-layer>`_ to indicate different ranges of the line density (per square meter). Specifically, the darker the blue the higher the density of underground water veins.

1.3 Video Tutorial
^^^^^^^^^^^^^^^^^^

:raw-html-m2r:`<a href="https://mediasite.video.ufl.edu/Mediasite/Play/454f67d210d843889b84dc1a1bc25f421d">
  <img src="../../../img/timg/m2_den_line.png" alt= "density of line" width="800">
</a>`

2. Distance to Point Features
-----------------------------

*Distance to Point Features* calculates the distance between an input feature and its nearest point feature in another layer. The polygon features (i.e., Input layer) and point features (i.e., Point layer) are two required parameters for using this tool. There are four additional parameters that can be specified, which are outlined `here <https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-point-features>`_.

2.1 Usage
^^^^^^^^^

This tool is often used to calculate the distance of the nearest point feature around a vector feature. For example, this tool can be used to find the nearest school or the nearest hospital around each residential area.

In the Distance method, `Euclidean Distance <https://en.wikipedia.org/wiki/Euclidean_distance>`_ and
`Manhattan Distance <https://en.wikipedia.org/wiki/Taxicab_geometry>`_ are two different methods to measure the distance between an input feature and its nearest point feature.

2.2 Example
^^^^^^^^^^^

In the following example, we use the tool to calculate the distance between each polygon in the THLD area and its nearest education facility. The datasets used are listed below:

.. list-table::
   :header-rows: 1

   * - ID
     - File Name
     - Data Format
     - Type
     - Description
   * - 1
     - THLD_poly.shp
     - vector
     - polygon
     - IDUs in the THLD District Assembly
   * - 2
     - Education_Facilities.shp
     - vector
     - point
     - Education facilities in THLD District


The two figures below display the specific parameter settings
 and the output of the tool.

.. list-table::
   :header-rows: 1

   * - Parameter Setting
     - Output
   * - 
     .. image:: ../../../img/gui/window/m2_distopoint_ParametersSetting.png
        :target: ../../../img/gui/window/m2_distopoint_ParametersSetting.png
        :alt: PS2
     
     - 
     .. image:: ../../../img/map/m2_distopoint_Output.png
        :target: ../../../img/map/m2_distopoint_Output.png
        :alt: am2
     


2.3 Video Tutorial
^^^^^^^^^^^^^^^^^^

:raw-html-m2r:`<a href="https://mediasite.video.ufl.edu/Mediasite/Play/7b5a5d92d18543df8ccb5e9839d9e2ba1d">
  <img src="../../../img/timg/m2_dist_pnt.png" alt= "distance to point" width="800">
</a>`

3. Reclassify Field
-------------------

*Reclassify Field* reclassifies a field in the input table based on predefined rules and stores the translated values in a new field. The input table (i.e., Input layer), the field to be reclassified (i.e., Field to reclassify), the predefined rules (i.e., Old values and New values), and the new field (i.e., Output column name) are required parameters. There are two additional parameters that can be specified, which are outlined `here <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_.

3.1 Usage
^^^^^^^^^

This tool is used to reclassify or change the values of the feature to alternative values.

Old values are the values (or value ranges) you want to reclassify, the New
values are the values that will be assigned to the old values.
For example, a vector of soil type may be assigned new values of 1 to 10 to
represent erosion potential.

No data value is the new value that will be assigned to the no data value.
In most cases, the no data value will be 255, so the new value 0 (default
setting of No data value) will replace the old value 255 in the field after
running the tool.

This tool is useful when you are trying to do a suitability model, it allows
you to assign new values to different evaluation indicators under a uniform
scoring system (e.g., 1 to 10) on which the final weighting step will be based.

3.2 Example
^^^^^^^^^^^

Recall that, in Exercise 2 of Module 1, we calculated the population density of
Ghana by district in 2018.
In the following example, in order to know the population density level of
Ghana by district in 2018, we use the Reclassify Field tool to reclassify the
population density of Ghana by district in 2018 according to the criteria that
old values: 7-60, 60-100, 100-186, 186-490, and 490-18804 will be assigned new
values: 1, 2, 3, 4, and 5, respectively.
The datasets used are listed below:

.. list-table::
   :header-rows: 1

   * - ID
     - File Name
     - Data Format
     - Type
     - Description
   * - 1
     - Gh_260_MMDA.shp
     - vector
     - polygon
     - Districts of Ghana


The two figures below display the specific parameter settings and the output
of the tool.

.. list-table::
   :header-rows: 1

   * - Parameter Setting
     - Output
   * - 
     .. image:: ../../../img/gui/window/m2_reclassify_ParametersSetting.png
        :target: ../../../img/gui/window/m2_reclassify_ParametersSetting.png
        :alt: PS3
     
     - 
     .. image:: ../../../img/map/m2_reclassify_Output.png
        :target: ../../../img/map/m2_reclassify_Output.png
        :alt: am3
     


3.3 Video Tutorial
^^^^^^^^^^^^^^^^^^

:raw-html-m2r:`<a href="https://mediasite.video.ufl.edu/Mediasite/Play/4f1c71dcc1c34ee8a350bb248ffba49e1d">
  <img src="../../../img/timg/m2_reclass_field.png" alt= "reclassify" width="800">
</a>`

4. Spatial Join
---------------

*Spatial Join* evaluates spatial relationships (i.e., **Intersect**\ ,
**Contains**\ , **Within**\ ) between features in the **Target Layer** and the **Join Layer**.
The tool joins the columns from the **Join Layer** to the **Target Layer** if
any two features, one from each layer (we call them "matched" for each other),
satisfy the specified spatial relationship. There are three additional parameters
that can be specified, which are outlined `here <https://github.com/SERVIR-WA/GALUP/wiki/Tools#spatial-join>`_.\ :raw-html-m2r:`<br>`

When there are multiple "matched" features in the **Join Layer**\ , you can
choose either **Join one to many** or **Join one to one**.
If **Join one to many** is selected, features in the **Target Layer**
will be duplicated multiple times (as many as the number of "matched"
features) to combine with each "matched" feature in the **Join Layer**.
On the contrary, if  **Join one to one** is selected, all "matched"
features in the **Join Layer** will be aggregated, and then combined with
a target feature.\ :raw-html-m2r:`<br>`

4.1 Usage
^^^^^^^^^

*Spatial Join* matches rows from the Join Features to the Target Features based
on their relative spatial locations.
Moreover, this tool is taken a step further in that it not only evaluates
spatial relationships but also allows users to specify the column of interest
from the Join Layer and then calculate particular statistics, e.g., **first**\ ,
**last**\ , **sum**\ , **mean**\ , **median**\ , **max**\ , **min**\ , **std** (standard
deviation), **var** (variance), **count**.

4.2 Example
^^^^^^^^^^^

In the following example, we choose the **Join one to one** option to find out
the **count** (number of records) of points of interest (tourism) within each
District Assembly of Ghana.
The datasets used are listed below:

.. list-table::
   :header-rows: 1

   * - ID
     - File Name
     - Data Format
     - Type
     - Description
   * - 1
     - Gh_260_MMDA.shp
     - vector
     - polygon
     - Districts of Ghana
   * - 2
     - PointOfInterest.shp
     - vector
     - point
     - Point of interest in Ghana


The two figures below display the specific parameter settings and the output of the tool.
|         Parameters setting     |       Output        |
|:------------------------------:|:------------------------------------------:|
| :raw-html-m2r:`<img src="../../../img/gui/window/m2_spatialjoin_ParametersSetting.png" alt= "Add data to Map Canvas" width="600">`   |  :raw-html-m2r:`<img src="../../../img/map/m2_spatialjoin_Output.png" alt= "Add data to Map Canvas" width="580">`   |

In the output map,  we used Reds
`Graduated Color <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module1.md#33-change-symbology-of-a-layer>`_
to indicate different ranges of the number of point of interest in Ghana.
Specifically, the darker the red the higher the number of point of interest.

4.3 Video Tutorial
^^^^^^^^^^^^^^^^^^

:raw-html-m2r:`<a href="https://mediasite.video.ufl.edu/Mediasite/Play/0fb02ede595f4440b8f72446168f0a961d">
  <img src="../../../img/timg/m2_select_by_location.png" alt= "spatial join" width="800">
</a>`

5. Zonal Statistics
-------------------

*Zonal Statistics* calculates statistics (i.e., **mean**\ , **median**\ ,
**sum**\ , **minimum**\ , **maximum**\ , **standard deviation**\ , **majority**\ ,
**minority**\ , **unique**\ , **range**\ ) on values of **Raster Layer** within the
zones of **Input Layer**.
There are three additional parameters that can be specified, which are outlined
`here <https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics>`_.\ :raw-html-m2r:`<br>`

5.1 Usage
^^^^^^^^^

This tool is often used to calculates statistic on values you are interested from
**Raster Data** within the zones defined by **Input Layer**.

5.2 Example
^^^^^^^^^^^

In the following example, we use this tool to **sum** population based
on values of raster dataset within each district of Ghana to show the
distribution of population in Ghana.

  The datasets used are listed below:

.. list-table::
   :header-rows: 1

   * - ID
     - File Name
     - Data Format
     - Type
     - Description
   * - 1
     - Gh_260_MMDA.shp
     - vector
     - polygon
     - Districts of Ghana
   * - 2
     - population_gha_2018-10-01.tif
     - raster
     - tiff
     - Population of Ghana in 2018


  The two figures below display the specific parameter settings and the output of the tool.

.. list-table::
   :header-rows: 1

   * - Parameters setting
     - Output
   * - :raw-html-m2r:`<img src="../../../img/gui/window/m2_zonalstats_ParametersSetting.png" alt= "Add data to Map Canvas" width="565">`
     - :raw-html-m2r:`<img src="../../../img/map/m2_zonalstats_Output.png" alt= "Add data to Map Canvas" width="530">`


In the output map, we used *Reds*
`Graduated Color <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/modules/module1.md#33-change-symbology-of-a-layer>`_
to indicate different ranges of the number of population in Ghana.
Specifically, the darker the red the higher the number of population.

5.3 Video Tutorial
^^^^^^^^^^^^^^^^^^

:raw-html-m2r:`<a href="https://mediasite.video.ufl.edu/Mediasite/Play/ee051550edd14f4fa19238694aa215181d">
  <img src="../../../img/timg/m2_zonal_stats.png" alt= "zonal stats" width="800">
</a>`

6. Select by Location
---------------------

*Select By Location* allows you to select features from **Input layer** based on
their location relative (i.e., **Intersect**\ , **Contains**\ , **Within**\ , **Within a distance**\ )
to features in **Selection layer**. There are two additional parameters that can be specified, which are outlined
  `here <https://github.com/SERVIR-WA/GALUP/wiki/Tools#select-by-location>`_.\ :raw-html-m2r:`<br>`

6.1 Usage
^^^^^^^^^

This tool is often used to select features spatially relative to the feature you
are interested in.

6.2 Example
^^^^^^^^^^^

In the following example, we use this tool to select all the districts
within a 100-kilometer buffer of the railway line in Ghana.

  The datasets used are listed below:

.. list-table::
   :header-rows: 1

   * - ID
     - File Name
     - Data Format
     - Type
     - Description
   * - 1
     - Gh_260_MMDA.shp
     - vector
     - polygon
     - Districts of Ghana
   * - 2
     - RailwayLine.shp
     - vector
     - line
     - Railway line in Ghana


  The two figures below display the specific parameter settings and the output of the tool.

.. list-table::
   :header-rows: 1

   * - Parameters setting
     - Output
   * - :raw-html-m2r:`<img src="../../../img/gui/window/m2_selectbylocation_ParametersSetting.png" alt= "Add data to Map Canvas" width="570">`
     - :raw-html-m2r:`<img src="../../../img/map/m2_selectbylocation_Output.png" alt= "Add data to Map Canvas" width="521">`


In the output map, we used Green color to indicate the served area of railway
in Ghana.

6.3 Video Tutorial
^^^^^^^^^^^^^^^^^^

:raw-html-m2r:`<a href="https://mediasite.video.ufl.edu/Mediasite/Play/9bf6d0b1150849bc8d91e71db48625281d">
  <img src="../../../img/timg/m2_select_by_location.png" alt= "select by location" width="800">
</a>`

7. Exercises and Post-training Survey
-------------------------------------


* Please complete the `Exercise 1 <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise1.md>`_.
* Please complete the `Exercise 2 <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise2.md>`_.
* Please complete the `Exercise 3 <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise3.md>`_.
* Please complete the `Exercise 4 <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m2_exercise4.md>`_.
* Please take this post-training
  `survey <https://ufl.qualtrics.com/jfe/form/SV_9nLiduVDMRRE4t0>`_ (required).
* Please submit your exercises `here <https://github.com/SERVIR-WA/GALUP/issues/new?assignees=muribasterra&labels=exercise+w1m2&milestone=Module+2+Exercises&template=w1m2-exercise-submission.md&title=Module+2+exercises+%5Breplace+with+your+name%5D>`_.

8. What's Next?
---------------

Module 3 - Create Suitability Models with QGIS Graphical Modeler.
