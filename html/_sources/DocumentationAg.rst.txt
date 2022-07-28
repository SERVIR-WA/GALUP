.. role:: raw-html-m2r(raw)
   :format: html


1. Row Crops
============

Land Condition (Physical)
-------------------------

The tool aims to evaluate the capacity of land to respond to rain and produce useful pasture.
The assessment of land condition includes the evaluation of slope percent and land cover condition.Weight should be separated by comma.

**Name**
~~~~~~~~~~~~

``rcrp_Physical_LandCondition.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
#. `Reclassify by table <https://docs.qgis.org/3.4/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html#reclassify-by-table>`_
#. `Weight Sum of Fields <https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields>`_
#. `Zonal Statistics <https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics>`_
   #### **\ *Input parameters*\ **

   #. Input layer: Input vector layer.
   #. Land cover: Input raster layer. Land cover is usually comprised of lands with different woodland conditions and built up area.
   #. Add value for land cover: Add new value for different land cover types in table.Table is fixed as 3 row table. Row 1 represents the number of land cover types. Row 2 is the number of land cover types plus 1. Row 3 represents the value the land cover types will be given. Different columns represent different types of land cover.
   #. Slope: Input slope raster data.
   #. Parameters for LCC: Land Capability Classification is defined as a system of grouping land into various classes based on inherent limitations imposed on sustained use by soil attributes, topography, drainage and climate. Slope percent could be attributed into 5 classes in following range\ :raw-html-m2r:`<a href="#ref1"><sup>[1]</sup></a>`\ :
        | Slope (percent rise) | Suitability |
        |----------------------|-------------|
        | 0-2                  | 9           |
        | 2-8                  | 7           |
        | 8-15                 | 5           |
        | 15-25                | 3           |
        | 25-45                | 1           |
   #. LCC Classes: Defined Classes respond to the range of Slope percent.
   #. Weight by LC Slope: Weight the suitability of land cover condition for agriculture activities and slope percent. Weight should be separated by comma.
      #### **Output**
      ``rcrp_LandCondition`` (output vector layer for land condition).

Soil Condition (Physical)
-------------------------

This model uses "Zonal Statistics" to convert raster data to vector data (with mean statistics), then runs the "Reclassify" tool to reclassify data values, and finally calculates the rating for the soil condition by using the "Weighted Sum of Fields" tool.

Note: when enter multiple field names in the "field", please separate multiple field names by  semicolon, and no space needed between different field names (e.g., Res_D_BC;Res_D_MC;Res_D_SC).

**Name**
~~~~~~~~~~~~

``rcrp_Physical_SoilCondition.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
#. `Rescale Field Linearly <https://github.com/SERVIR-WA/GALUP/wiki/Tools#rescale-field-linearly>`_
#. `Weight Sum of Fields <https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields>`_
#. `Zonal Statistics <https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics>`_
   #### **\ *Input Parameters*\ **
#. InputPolygon: The research area polygon.
#. Root Zone Depth: The available root zone depth (cm) for crops.
#. Drainage: The drainage index of soil.
#. Soil (0-5 cm) PH Value: The soil PH value at the 0-5 cm soil depth.
#. Soil (5-15 cm) PH Value: The soil PH value at the 5-15 cm soil depth.
#. Soil (15-30 cm) PH Value: The soil PH value at the 15-30 cm soil depth.
#. Soil (30-60 cm) PH Value: The soil PH value at the 30-60 cm soil depth.
#. Soil (60-100 cm) PH Value: The soil PH value at the 60-100 cm soil depth.
#. Soil (100-200 cm) PH Value: The soil PH value at the 100-200 cm soil depth.
#. Weights for RZD, Drainage, and PH (different depths): The weights assigned to different parameters are according to official documents, and agriculture literatures. The default value setting is 0.33, 0.33, 0, 0, 0, 0.089, 0.236, 0.005. These values derive from the table of the Estimated Production of Major Crops 2016 (District Medium Term Development Plan 2018-2021, pp.82)\ :raw-html-m2r:`<a href="#ref2"><sup>[2]</sup></a>`\ , and root zone depth information for 6 major crops in the THLD (Maize, Rice, Cassava, Yam, Cocoyam, Plantain) is from different agricultural articles\ :raw-html-m2r:`<a href="#ref2"><sup>[3]</sup></a>`\ :raw-html-m2r:`<a href="#ref2"><sup>[4]</sup></a>`\ :raw-html-m2r:`<a href="#ref2"><sup>[5]</sup></a>`\ :raw-html-m2r:`<a href="#ref2"><sup>[6]</sup></a>`.
   #### **Output**
   ``rcrp_SoilCondition`` (output vector layer for soil condition).

Market (Economic)
-----------------

This model will firstly calculate the distance between the potential locations for marketplace (InputPolygon) and the target cities (Large city, Medium city, Small city), then rescale those distance values and set appropriate weights for different cities' sizes.

Finally, the model will generates the "Market_Weighted" value for rating each potential marketplaces (InputPolygon) by using the weighted sum algorithm （Note: when enter multiple field names in the "field", please separate multiple field names by  semicolon, and no space needed between different field names. e.g., Res_D_BC;Res_D_MC;Res_D_SC). The higher the value, the more suitable for the location to be the marketplace.

**Name**
~~~~~~~~~~~~

``rcrp_Economic_Market.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Distance to Point Features <https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-point-features>`_
#. `Rescale Field Linearly <https://github.com/SERVIR-WA/GALUP/wiki/Tools#rescale-field-linearly>`_
#. `Weight Sum of Fields <https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields>`_
   #### **\ *Input Parameters*\ **
#. InputPolygon: This is the polygon where the potential marketplaces might be located.
#. LargeCity: The point data that symbolizes the large cities.
#. MediumCity: The point data that symbolizes the medium cities.
#. SmallCity: The point data that symbolizes the small cities.
#. Weights by City Level: This is a weight setting for different size of cities.
   #### **Output**
   ``rcrp_Market`` (output shapefile for the market).

Transport Accessibility (Economic)
----------------------------------

Transport Accessibility model are used to evaluate automobile accessibility in each parcel. The tool is able to calculate the distance to two types of roads and then weight the rescaled distances.

**Name**
~~~~~~~~~~~~

``rcrp_Economic_TransportAccessibility.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Distance to Line Features <https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-line-features>`_
#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
#. `Weight Sum of Fields <https://github.com/SERVIR-WA/GALUP/wiki/Tools#weighted-sum-of-fields>`_
   #### **\ *Input parameters*\ **
#. Input Polygon: Input vector layer.
#. Major Roads: Input vector layer.Roads with the largest capacity  usually are viewed as Major Roads.
#. Secondary Roads: Input vector layer.
#. Weighted by Roads level: Weight value by which to multiply the fields. It can be any positive or negative decimal value. Weights should be separated by comma (Note: the weighted fields should be separated by semicolon without space, i.e., field1;field2).
   #### **Outputs**
   ``rcrp_TransportAccessibility`` (Output vector layer for Transport Accessibility).

2. Timber Production
====================

3. Livestock
============

Built Area
----------

This tool will calculate the Euclidean distance between the Built Area (point feature) and the Research Area (polygon feature) by using Distance to Point Features tool, and then it will reclassify the distance value from 1 to 9. The larger the distance value the lager the assigned value.

**Name**
~~~~~~~~~~~~

``Livestock_BuiltArea.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Distance to Point Features <https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-point-features>`_
#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
   #### **\ *Input parameters*\ **

   #. InputPolygon: The research area polygon.
   #. Built Area: The built area of the research area, point data required.
        | Distance (meter) | Suitability Value |
        |------------------|-------------|
        | 0-500            | 1           |
        | 500-1000         | 3           |
        | 1000-1500        | 5           |
        | 1500-2500        | 7           |
        | 2500-10000       | 9           |
      #### **Output**
      ``Livestock_Blt_Area`` (output shapefile for the Built Area).

Grazing Land (IDW Distance-based)
---------------------------------

Major Roads
-----------

This tool will calculate the Euclidean distance between the Major Roads (line feature) and the Research Area (polygon feature) by using Distance to Line Features tool, and then it will reclassify the distance value from 1 to 9.

**Name**
~~~~~~~~~~~~

``Livestock_MajorRoads.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Distance to Line Features <https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-line-features>`_
#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
   #### **\ *Input parameters*\ **

   #. InputPolygon: The research area polygon.
   #. Major Roads: The major roads of the research area, line data required.
        | Distance (meter) | Suitability Value |
        |------------------|-------------|
        | 0-100            | 1           |
        | 100-500         | 9           |
        | 500-1000        | 7           |
        | 1000-2000        | 5           |
        | 2000-10000       | 3           |
      #### **Output**
      ``Livestock_Mjr_Rds`` (output shapefile for the Built Area).

Slope
-----

This model will first assign the Slope value (degree) (raster layer) to the Research Area (polygon feature) by using Zonal Statistics (with mean statistics), and then it will reclassify the value from the slope value from 1 to 9.

**Name**
~~~~~~~~~~~~

``Livestock_Slope.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Zonal Statistics <https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics>`_
#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
   #### **\ *Input parameters*\ **

   #. InputPolygon: The research area polygon.
   #. Slope: The slope value of the research area, raster data required.
        | Slope (degree) | Suitability Value |
        |------------------|-------------|
        | 0-5            | 9           |
        | 5-10         | 7           |
        | 10-15        | 5           |
        | 15-20        | 3           |
        | 20-40       | 1           |
      #### **Output**
      ``Livestock_Slp`` (output shapefile for the Slope).

Soil Fertility
--------------

This model will first assign the Landcover code value (raster layer) to the Research Area (polygon feature) by using Zonal Statistics (with majority statistics), and then it will reclassify the value from the slope value from 1 to 9.

**Name**
~~~~~~~~~~~~

``Livestock_SoilFertility.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Zonal Statistics <https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics>`_
#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
   #### **\ *Input parameters*\ **

   #. InputPolygon: The research area polygon.
   #. Land Cover: The Landcover code value of the research area, raster data required.
        | Landcover Code\ :raw-html-m2r:`<a href="#ref2"><sup>[7]</sup></a>` | Suitability Value |
        |------------------|-------------|
        | 2-10            | 7           |
        | 11         | 3           |
        | 12        | 9           |
        | 13        | 1           |
        | 14       | 9           |
      #### **Output**
      ``Livestock_SilFtlt`` (output shapefile for the Soil Fertility).

Surface Water
-------------

This tool will generate the centroid of the surface water (polygon feature) and calculate the Euclidean distance between the centroid and the Research Area (polygon feature) by using Distance to Point Features tool, and then it will reclassify the distance value from 1 to 9. The larger the distance value the lager the assigned value.

**Name**
~~~~~~~~~~~~

``Livestock_SurfaceWater.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Centroid <https://docs.qgis.org/2.6/en/docs/user_manual/processing_algs/qgis/vector_geometry_tools/polygoncentroids.html>`_
#. `Zonal Statistics <https://github.com/SERVIR-WA/GALUP/wiki/Tools#zonal-statistics>`_
#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
   #### **\ *Input parameters*\ **

   #. InputPolygon: The research area polygon.
   #. Surface Water: The surface water area of the research area, polygon data required.
        | Distance (meter) | Suitability Value |
        |------------------|-------------|
        | 0-1000            | 1           |
        | 1000-2000         | 3           |
        | 2000-3000        | 5           |
        | 3000-4000        | 7           |
        | 4000-10000       | 9           |
      #### **Output**
      ``Livestock_SfWtr`` (output shapefile for the Surface Water).

Underground Water
-----------------

This tool will calculate the Euclidean distance between the Underground Water (line feature) and the Research Area (polygon feature) by using Distance to Line Features tool, and then it will reclassify the distance value from 1 to 9. The larger the distance value the lager the assigned value.

**Name**
~~~~~~~~~~~~

``Livestock_UndergourndWater.model3``

**Tools used in the model**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#. `Distance to Line Features <https://github.com/SERVIR-WA/GALUP/wiki/Tools#distance-to-line-features>`_
#. `Reclassify Field <https://github.com/SERVIR-WA/GALUP/wiki/Tools#reclassify-field>`_
   #### **\ *Input parameters*\ **

   #. InputPolygon: The research area polygon.
   #. Underground Water: The underground water area of the research area, line data required.
        | Distance (meter) | Suitability Value |
        |------------------|-------------|
        | 0-1000            | 1           |
        | 1000-2000         | 3           |
        | 2000-3000        | 5           |
        | 3000-4000        | 7           |
        | 4000-10000       | 9           |
      #### **Output**
      ``Livestock_UW`` (output shapefile for the Underground Water).

Reference
=========


#. :raw-html-m2r:`<a id="ref1"></a>`\ Scopesi, C., Olivari, S., Firpo, M., Scarpellini, P., Pini, S., & Rellini, I. (2020). Land capability classification of Vernazza catchment, Cinque Terre National Park, Italy. Journal of Maps, 16(2), 357-362.
#. :raw-html-m2r:`<a id="ref2"></a>`\ DISTRICT MEDIUM TERM DEVELOPMENT PLAN (2018-2021) “An Agenda for Jobs : Creating Prosperity And Equal Opportunity for All”. District Planning Coordinating Unit (DPCU), April. 2017.
#. :raw-html-m2r:`<a id="ref3"></a>`\ Grace, M. R. (1977). Cassava Processing. Rome: FAO.
#. :raw-html-m2r:`<a id="ref4"></a>`\ O'SULLIVAN, J. N. (2008). Root distribution of yam (Dioscorea alata) determined by strontium tracer. Experimental Agriculture, 44(2), 223.
#. :raw-html-m2r:`<a id="ref5"></a>`\ Scaling Soil Nutrient Balances: Enabling Mesolevel Applications for African Realities. (2004). Italy: Food and Agriculture Organization of the United Nations.
#. :raw-html-m2r:`<a id="ref6"></a>`\ Albert, S. (2017, July 27). Plantain Organic Weed Control. Retrieved January 27, 2021, from https://harvesttotable.com/plantain-organic-weed-control/#:~:text=Root%20System%3A%20Plantain%20has%20a,depth%20of%20about%2018%20inches.
#. :raw-html-m2r:`<a id="ref6"></a>`\ Sulla-Menashe, D.,Friedl, M. A. (2018) User Guide to Collection 6 MODIS Land Cover (MCD12Q1 and
   MCD12C1) Product (pp.7). Retrieved January 27, 2021, from https://icdc.cen.uni-hamburg.de/fileadmin/user_upload/icdc_Dokumente/MODIS/mcd12_user_guide_v6.pdf.
