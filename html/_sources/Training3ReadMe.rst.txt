.. role:: raw-html-m2r(raw)
   :format: html


Workshop 3: Integrated Decision Units for Land Use Suitability Modeling
=======================================================================

..

   **Instructor**\ : `Dr. Changjie Chen <https://github.com/chjch>`_ (\ :raw-html-m2r:`<ins>chj.chen@<i></i>ufl.edu</ins>`\ ).\ **Date**\ : April 11 - April 15, 2022


Goal and Objectives
-------------------

The third GALUP workshop focuses on the creation of Integrated Decision Units
(IDUs) using geoprocessing tools in **QGIS**.
IDUs are land units, within which land properties (or attributes) are
homogeneous.
Such **homogeneity** ensures the integrity of a land use decision.
For rural or less developed area, **\ *delineation of land units*\ ** is a critical
step that must take place before the process of land suitability analysis.
Participants will be able to independently create IDUs for any region if base
input data are provided.
Specific objectives of this workshop include:


* Understand key concepts of IDU and why it is useful to land use planning
* Capable of using **16 tools** in QGIS involved in the process
* Independently create IDUs for different regions

An Integral Part of Land-Use Planning
-------------------------------------

In 1976, the Food and Agriculture Organization (FAO) of the United Nations
published :raw-html-m2r:`<a href="#a framework for land evaluation">
<i>A Framework for Land Evaluation</i></a>`\ , in which a system of philosophy and
principles on the evaluation of land potential was developed.
The **\ *framework*\ ** was tested and adopted in many countries.
In 1990, FAO published another report,
:raw-html-m2r:`<a href="#land evaluation for development">
<i>Land Evaluation for Development</i></a>`\ ,
reiterated the significance of reliable **land evaluation** in the context of
land-use planning and rural development, i.e., developing a rural area into
an area of higher intensity of human activities, i.e., urban area.
In this newer report, land evaluation and its relationship to (i.e., being a
part of) the overall land-use planning process was further elaborated.
As shown in the figure below, land evaluation is a procedure between Stage 2
and Stage 6, as well as a part of the Stage 7.

.. list-table::
   :header-rows: 1

   * - 
     .. image:: ./GithubPagesImages/LandEvaluationModelFAO.jpg
        :target: ./GithubPagesImages/LandEvaluationModelFAO.jpg
        :alt: FAO land evaluation framework
     
   * - Fig 1. The process of land-use planning. *Source*\ : FAO. (1990).


The Stage 4, in parallel with identifying land uses (Stage 3), is identifying
land units, e.g., IDUs.

Key Concepts
------------


* Land unit: areas of land with specific characteristics (or qualities).
  For a comprehensive introduction of *land unit*\ , please check
  :raw-html-m2r:`<a href="#land unit">Zonneveld's paper</a>`.
* Land characteristic: simple attribute that can be measured or estimated. For
  example, *mean annual rainfall*.
* Land quality: a complex attribute that usually reflects the interaction of
  many land characteristics, such as *susceptibility to flooding*.

Implication of IDU
------------------

Although any parcel of land can be considered a land unit, it is more efficient
and meaningful to use parcels that can be adequately described in terms of one
or a combination of land properties.
A land unit should therefore represent an area that is, in terms of
predetermined properties (such as floodplain, land cover, climate, soil),
different from the surrounding land and can be assumed to have **homogeneous**
land properties.

IDUs essentially are a set of polygons with definite boundaries.
A specific land use can be assigned for each IDU based on land-use suitability
analysis.
Such assignment is referred to as a land-use decision.
Due to homogeneity, the integrity of land-use decisions is assured.
Since land-use decisions are intrinsically discrete (two adjacent parcels can
have different uses, for example), a vector (polygon) representation is more
applicable than a raster representation.
That's why we need to have a system of polygons, such as IDUs, to begin the
land evaluation process.
This is the first, however, critical step to develop a spatially explicit
land-use plan.

Content
-------


* `Integrated Decision Units for Land Use Suitability Modeling <module.md>`_
* `Exercise: Create IDUs for AAC <exercise.md>`_
* `Submit post-training survey <https://ufl.qualtrics.com/jfe/form/SV_0vNRnI3WsOjXM1g>`_

Assignment Submission and Help
------------------------------

The participants will have to sign into their GitHub accounts to submit assignments. Below is a video explaining how to submit the module assignments and how to request help through GitHub. Note: It may be convenient to open videos in the workshop in a new tab or window to easily navigate the GitHub page.


.. raw:: html

   <p align="center">
     <a href="https://mediasite.video.ufl.edu/Mediasite/Play/9741afe237094a77aff3acbf6c2df8a91d" target="_blank">
       <img src="https://user-images.githubusercontent.com/84922404/139679866-11650dd6-855f-4420-82c1-fa0f4071ee37.png" alt= "GEE Tutorial" width="800">
     </a>
   </p>


Reference
---------


#. :raw-html-m2r:`<a id="a framework for land evaluation"></a>`\ FAO. (1976). A framework for
   land evaluation (No. 32; Soils Bulletins). Food and Agriculture Organization
   of the United Nations. http://www.fao.org/3/X5310E/x5310e00.htm
#. :raw-html-m2r:`<a id="land evaluation for development"></a>`\ FAO. (1990). Land evaluation for
   development. Food and Agriculture Organization of the United Nations.
   https://www.fao.org/3/U1980E/u1980e00.htm
#. :raw-html-m2r:`<a id="land unit"></a>`\ Zonneveld, I. S. (1989). The land unit—A fundamental
   concept in landscape ecology, and its applications. *Landscape Ecology*\ ,
   3(2), 67–86. https://doi.org/10.1007/BF00131171
