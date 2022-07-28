.. role:: raw-html-m2r(raw)
   :format: html


Module 3 - Common RS Indices and Environmental Variables
========================================================

**What will you learn from this module?**


* Search, extract, and visualize common RS indices and environmental variables for potential use in landscape assessment and regional scale planning exercises,
* Use Google Earth Engine to assess spatial and temporal trends in these data.

1. RS Indices
-------------

**Remote sensing indices** (or spectral indices) are arithmentic combinations of reflectance at two or more bands that help provide measurable estimates of the relative abundance of indicators of interest. Vegetation indices (such as the normalized difference vegetation index: NDVI) are the most widely known, but indices can be formulated for tracking burn areas, exposed soil or built-up areas.


* 
  Spectral/Image indices are generally calculated using simple mathematical transformations (addition, subtraction, division) conducted on satellite bands of specific wavelength regions. Values of image indices can range from -1 - +1 (normalized difference indices), to arbitrary scales for other ratio-based indices. See :raw-html-m2r:`<a href="https://www.usgs.gov/core-science-systems/nli/landsat/landsat-surface-reflectance-derived-spectral-indices?qt-science_support_page_related_con=0#qt-science_support_page_related_con">this link</a>` for a good introduction to indices that can be obtained using Landsat data.

* 
  Some commonly used RS indices include

  .. code-block::

     <blockquote>
     Normalized Difference Vegetation Index (NDVI)<br>
     Enhanced Vegetation Index (EVI)<br>
     Soil Adjusted Vegetation Index (SAVI)<br>
     Modified Soil Adjusted Vegetation Index (MSAVI)<br>
     Normalized Difference Moisture Index (NDMI)<br>
     Normalized Burn Ratio (NBR)<br>
     Normalized Burn Ratio 2 (NBR2)<br>
     Normalized Difference Snow Index (NDSI)<br>
     </blockquote>


* The Table below provides reflectances used to calculate the above indices. 


.. raw:: html

   <p align="center">
   <img src="https://user-images.githubusercontent.com/87503837/142231637-77253803-79a2-4f34-939a-f8d234d796bb.png" height="50%" width="50%">
   </p>



* For example, NDVI is a combination of reflectances in the red and NIR wavelengths as shown in the Figure below. Healthy vegetation reflects more solar radiation in the NIR wavelength than unhealthy vegetation. Thus, the NDVI for healthy vegetation is higher. 

  .. raw:: html

     <p align="center">
     <img src="https://user-images.githubusercontent.com/84922404/135468275-adaf7a44-b8f7-4d4e-9276-625a7a59f9d4.png" width="400">
     </p>


:pushpin: A database of remote sensing indices and their respective sensors and areas of application are compiled `here <https://www.indexdatabase.de/>`_. 

2. Sources for Preprocessed RS Indices for Regional-scale Applications
----------------------------------------------------------------------


* In general, computing RS requires that data be radiometrically calibrated and converted to apparent at-surface reflectance. However, some commonly used indices are often made available by agencies such as NASA or USGS to make regional-scale comparisons of landscape condition  easier. These data have been pre-processed and cleaned for artifacts (clouds, missing data) as 'analysis-ready' products. The Table below provides the spatial and temporal resolutions of the RS indices and environment variables, along with their sensors/sources.

.. list-table::
   :header-rows: 1

   * - RS Indices and Environmental Variables
     - Sensor(s)
     - Temporal Resolution
     - Spatial Resolution
   * - EVI
     - MODIS (\ `MOD13A2.006 Terra Vegetation Indices <https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD13A2>`_\ ); Landsat `5 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T1_8DAY_EVI>`_\ , `7 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1_8DAY_EVI>`_\ , `8 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_8DAY_EVI#:~:text=These%20composites%20are%20created%20from,following%20year%20by%203%20days.>`_ (8-Day EVI Composite generated from GEE)
     - 16-Day; 8-Day
     - 1 km; 30 m
   * - NDVI
     - MODIS (\ `MOD13A2.006 Terra Vegetation Indices <https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD13A2>`_\ ); Landsat `5 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T1_8DAY_NDVI>`_\ , `7 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1_8DAY_NDVI>`_\ , `8 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_8DAY_NDVI_>`_ ([8-Day NDVI Composite generated from GEE])
     - 16-Day; 8-Day
     - 1 km; 30 m
   * - NDWI
     - MODIS (\ `Terra Daily NDWI <https://developers.google.com/earth-engine/datasets/catalog/MODIS_MOD09GA_006_NDWI>`_\ ); Landsat 8 (\ `8-Day NDWI Composite <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_8DAY_NDWI>`_ generated from GEE)
     - Daily; 8-Day
     - 463 m; 30 m
   * - Precipitation
     - Global Precipitation Measurement (\ `IMERG <https://developers.google.com/earth-engine/datasets/catalog/NASA_GPM_L3_IMERG_V06>`_\ )
     - Hourly
     - 10 km
   * - Land Surface Temperature
     - MODIS (\ `MOD11A1.006 Terra Land Surface Temperature and Emissivity <https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD11A1>`_\ ); Landsat `5 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T2_SR>`_\ , `7 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T2_SR>`_\ , `8 <https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T2_SR>`_ (Surface Reflectance Tier 1);
     - Daily; 16-Day
     - 1 km; 30 m


3. Environment Variables Available on Google Earth Engine
---------------------------------------------------------


* In addition to satellite imagery and derived data, multiple environmental datasets are available on the GEE platform for ingestion into analytical processes. Commonly used enviornmental data include
  .. code-block::

     <blockquote>
     TerraClimate: Monthly Climate and Climatic Water Balance (includes precipitation, temperature, drought severity etc.) <a href="https://www.nature.com/articles/sdata2017191">Reference</a> <br>
      SRTM Digital Elevation Data <a href="https://srtm.csi.cgiar.org/">Reference</a><br>
      GCOM-C/SGLI L3 Land Surface Temperature (LST) <a href="https://suzaku.eorc.jaxa.jp/GCOM/index.html">Reference</a><br>
      OpenLandMap Soil textures, water holding capacity etc. <a href="https://www.openlandmap.org/">Reference</a><br>
     Fire detection <a href="https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/about-firms">Reference</a><br>
     </blockquote>

Exercise and Post-Module Survey (required)
------------------------------------------

This video may be useful in completing the exercises:


.. raw:: html

   <p align="center">
     <a href="https://mediasite.video.ufl.edu/Mediasite/Play/bfe5811813c04582a51f02f636dc31161d" target="_blank" rel="noopener">
       <img src="https://user-images.githubusercontent.com/84922404/142096329-b1cb29c6-411a-42d9-905c-20ec80f899b2.png" alt= "GEE Tutorial" width="800">
     </a>
   </p>



#. Please complete and submit `Exercise 1 <https://github.com/SERVIR-WA/GALUP/blob/master/training/2_rs/Exercises/M3_exercise1.md>`_ for Module 3.
#. Submit the Post-Module `survey <https://ufl.qualtrics.com/jfe/form/SV_bpjF7THHLlhtWCO>`_. 

</p>

#
=

**Previous Section:**\ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; **Next Section:**

:raw-html-m2r:`<a href="module2.md" title="Module 2">Module 2</a>` &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :raw-html-m2r:`<a href="module4.md" title="Module 4">Module 4</a>`
