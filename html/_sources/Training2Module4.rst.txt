.. role:: raw-html-m2r(raw)
   :format: html


Module 4 - Land Cover Classification
------------------------------------

**What will you learn from this module?**


* Common methods using RS indices for supervised land cover classification (LCC)
* LCC systems
* Classify images in GEE 

1. Supervised Image Classification Methods
------------------------------------------

These methods identify spectrally similar areas on images by first identifying known classes from training sites and then directing the image processing using those training sites as reference for unknown sites. Following methods are commonly used for LCC:


* **Minimum-Distance to the Mean Classifier**\ : This technique calculates the mean point in digital parameter space, and uses multiple metrics such as Euclidean distance, normalized Euclidean distance, and Mahalanobis distance from that mean to classify unknown image data to known classes, as shown in the Figure below. Additional information is available `here <https://docs.lib.purdue.edu/larstech/25/>`_. (\ `Source <https://github.com/SERVIR-WA/GALUP/files/7573860/full_phd.pdf>`_\ )

</p>


.. raw:: html

   <p align="center">
     <img width="600" alt="CCDC1" src="https://user-images.githubusercontent.com/84922404/142700597-7ae7e638-a789-424e-af22-e432a9bea17f.png"/>
   </p>



* **Classification and Regression Trees (CART)**\ : This model uses binary decision trees to explain predicted values using a sample of training data with already known classifications. Large amount of data is recommended for good results because the branching process for the decision trees, as shown in the Figure below. Additional information is available `here <https://wiki.q-researchsoftware.com/wiki/Machine_Learning_-_Classification_And_Regression_Trees_(CART>`_\ ). (\ `Source <https://medium.com/geekculture/decision-trees-with-cart-algorithm-7e179acee8ff>`_\ )

</p>


.. raw:: html

   <p align="center">
     <img width="600" alt="CART" src="https://user-images.githubusercontent.com/84922404/142700539-f4e6b3bf-7945-4380-baf8-acfb064ee63f.png"/>
   </p>



* **Random Forest Classifier**\ : This is an ensemble learning method that creates a multitude of decision trees and takes the average of the trees for classification, as shown in the Figure below. The RF algorithm can also classify variable importance. Additional information is available `here <https://www.sciencedirect.com/science/article/pii/S0167865505002242>`_. (\ `Source <https://corporatefinanceinstitute.com/resources/knowledge/other/random-forest/>`_\ )

</p>


.. raw:: html

   <p align="center">
     <img width="600" alt="RF" src="https://user-images.githubusercontent.com/84922404/142700553-177ae5ae-169a-4a4d-8238-ff301f27c48e.png"/>
   </p>



* **Support Vector Machine (SVM) Classifier**\ : These are a collection of non-parametric learning algorithms which find the optimal separating hyperplane between classes by focusing on the training data, as shown in the Figure below. Additional information is available `here <https://www.tandfonline.com/doi/abs/10.1080/01431160110040323>`_. (\ `Source <https://github.com/SERVIR-WA/GALUP/files/7573858/sensors-21-04283-v3.pdf>`_\ )

</p>


.. raw:: html

   <p align="center">
     <img width="600" alt="SVM" src="https://user-images.githubusercontent.com/84922404/142700549-bc4d5f9c-432d-4bf5-b04d-808604b0ff58.png"/>
   </p>



* **Continuous Change Detection and Classification (CCDC)**\ : This is a general-purpose algorithm that evaluates changes in land cover, land use, or condition over time. The algorithm includes a two-step masking algorithm to eliminate any noisy data caused by snow, clouds, or cloud shadows, as shown in the Figure below. Classification occurs after change is detected in a pixel value. Additional information is available `here <https://sites.bu.edu/measures/project-methods/change-detection-and-classification-algorithm/>`_. (\ `Source <https://sites.bu.edu/measures/project-methods/change-detection-and-classification-algorithm/>`_\ )

</p>


.. raw:: html

   <p align="center">
     <img width="800" alt="SVM" src="https://user-images.githubusercontent.com/84922404/142701192-9ccaf49b-f5c1-4a01-b112-0728e5c9e21b.png"/>
   </p>


2. Land Cover Classification Systems
------------------------------------


* The **International Geosphere–Biosphere Programme (IGBP)** is used by the current MODIS Land Cover `Product <https://modis.gsfc.nasa.gov/data/dataprod/mod12.php>`_. The land cover scheme consists of 17 classes that were decided upon to meet IGBP science projects standards. The scheme considers ground biomass, longevity, and leaf type when creating classes. Additional info: http://www.igbp.net. The following (expandable) outline shows the classification scheme for the IGBP Ecosystems Surface Classifications:
  :raw-html-m2r:`<ul>`
  :raw-html-m2r:`<details>`

  .. raw:: html

     <summary> <b> IGBP (Class, Class name, Description) </b> </summary>



#. 
   **Evergreen needleleaf forests** - Lands dominated by needleleaf woody vegetation with a percent cover >60% and height exceeding 2m. Almost all trees remain green all year. Canopy is never without green foliage.

#. 
   **Evergreen broadleaf forests** - Lands dominated by broadleaf woody vegetation with a percent cover >60% and height exceeding 2m. Almost all trees and shrubs remain green year-round. Canopy is never without green foliage.

#. 
   **Deciduous needleleaf forests** - Lands dominated by woody vegetation with a percent cover >60% and height exceeding 2m. Consists of seasonal needleleaf tree communities with an annual cycle of leaf-on and leaf-off periods.

#. 
   **Deciduous broadleaf forests** - Lands dominated by woody vegetation with a percent cover >60% and height exceeding 2m. Consists of broadleaf tree communities with an annual cycle of leaf-on and leaf-off periods

#. 
   **Mixed forests** - Lands dominated by trees with a percent cover >60% and height exceeding 2m. Consists of tree communities with interspersed mixtures or mosaics of the other four forest types. None of the forest types exceeds 60% of landscape.

#. 
   **Closed shrublands** Lands with woody vegetation less than 2m tall and with shrub canopy cover >60%. The shrub foliage can be either evergreen or deciduous.

#. 
   **Open shrublands** - Lands with woody vegetation less than 2m tall and with shrub canopy cover between 10% and 60%. The shrub foliage can be either evergreen or deciduous.

#. 
   **Woody savannas** - Lands with herbaceous and other understory systems, and with forest canopy cover between 30% and 60%. The forest cover height exceeds 2m.

#. 
   **Savannas** - Lands with herbaceous and other understory systems, and with forest canopy cover between 10% and 30%. The forest cover height exceeds 2m.

#. 
   **Grasslands** - Lands with herbaceous types of cover. Tree and shrub cover is less than 10%.

#. 
   **Permanent wetlands** - Lands with a permanent mixture of water and herbaceous or woody vegetation. The vegetation can be present either in salt, brackish, or fresh water.

#. 
   **Croplands** - Lands covered with temporary crops followed by harvest and a bare soil period (e.g., single and multiple cropping systems). Note that perennial woody crops will be classified as the appropriate forest or shrub land cover type.

#. 
   **Urban and built-up lands** - Land covered by buildings and other man-made structures.

#. 
   **Cropland/natural vegetation mosaics** - Lands with a mosaic of croplands, forests, shrubland, and grasslands in which no one component comprises more than 60% of the landscape.

#. 
   **Snow and ice** - Lands under snow/ice cover throughout the year.

#. 
   **Barren** - Lands with exposed soil, sand, rocks, or snow and never have more
   than 10% vegetated cover during any time of the year.

#. 
   **Water bodies** -  Oceans, seas, lakes, reservoirs, and rivers. Can be either fresh or saltwater bodies.
   </details>
   </ul>


* 
  The **Modified Anderson Level II Land Use/Land Cover Classification System** is used by the US Geological Survey (USGS) to generate National Land Cover Database (NLCD). The Database provides a comprehensive land cover product for the US, that is available for all 50 states and Puerto Rico and updated every 5 years. It is primarily based on Landsat data. Additional information can be obtained at `MRLC <https://www.mrlc.gov/data/legends/national-land-cover-database-2019-nlcd2019-legend>`_.  It consists of 16 classes, as shown in the following outline: 
  :raw-html-m2r:`<ul>` 
  :raw-html-m2r:`<details>`


  .. raw:: html

     <summary> <b> Modified Anderson LULC (Class, Value, Description) </b> </summary>


   *Water*


  * 
    11 **Open Water** - areas of open water, generally with less than 25% cover of vegetation or soil.

  * 
    12 **Perennial Ice/Snow** - areas characterized by a perennial cover of ice and/or snow, generally greater than 25% of total cover.   

  *Developed*


  * 
    21  **Developed, Open Space** - areas with a mixture of some constructed materials, but mostly vegetation in the form of lawn grasses. Impervious surfaces account for less than 20% of total cover. These areas most commonly include large-lot single-family housing units, parks, golf courses, and vegetation planted in developed settings for recreation, erosion control, or aesthetic purposes.

  * 
    22  **Developed, Low Intensity** - areas with a mixture of constructed materials and vegetation. Impervious surfaces account for 20% to 49% percent of total cover. These areas most commonly include single-family housing units.

  * 
    23  **Developed, Medium Intensity** - areas with a mixture of constructed materials and vegetation. Impervious surfaces account for 50% to 79% of the total cover. These areas most commonly include single-family housing units.

  * 
    24  **Developed High Intensity** - highly developed areas where people reside or work in high numbers. Examples include apartment complexes, row houses and commercial/industrial. Impervious surfaces account for 80% to 100% of the total cover.

   *Barren* 


* 
  31 **Barren Land (Rock/Sand/Clay)** - areas of bedrock, desert pavement, scarps, talus, slides, volcanic material, glacial debris, sand dunes, strip mines, gravel pits and      other accumulations of earthen material. Generally, vegetation accounts for less than 15% of total cover.

  *Forest*


  * 
    41  **Deciduous Forest** - areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. More than 75% of the tree species shed - foliage simultaneously in response to seasonal change.

  * 
    42  **Evergreen Forest** - areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. More than 75% of the tree species maintain their leaves all year. Canopy is never without green foliage.

  * 
    43  **Mixed Forest** - areas dominated by trees generally greater than 5 meters tall, and greater than 20% of total vegetation cover. Neither deciduous nor evergreen species are greater than 75% of total tree cover.  

*Shrubland*


* 
  51 **Dwarf Scrub** - Alaska only areas dominated by shrubs less than 20 centimeters tall with shrub canopy typically greater than 20% of total vegetation. This type is often co-associated with grasses, sedges, herbs, and non-vascular vegetation.

* 
  52  **Shrub/Scrub** - areas dominated by shrubs; less than 5 meters tall with shrub canopy typically greater than 20% of total vegetation. This class includes true shrubs, young trees in an early successional stage or trees stunted from environmental conditions. 

 *Herbaceous*


* 
  71  **Grassland/Herbaceous** - areas dominated by gramanoid or herbaceous vegetation, generally greater than 80% of total vegetation. These areas are not subject to intensive management such as tilling, but can be utilized for grazing.

* 
  72  **Sedge/Herbaceous** - Alaska only areas dominated by sedges and forbs, generally greater than 80% of total vegetation. This type can occur with significant other grasses or other grass like plants, and includes sedge tundra, and sedge tussock tundra.

* 
  73  **Lichens** - Alaska only areas dominated by fruticose or foliose lichens generally greater than 80% of total vegetation.

* 
  74  **Moss** - Alaska only areas dominated by mosses, generally greater than 80% of total vegetation.  

  *Planted/Cultivated*

* 
  81  **Pasture/Hay** - areas of grasses, legumes, or grass-legume mixtures planted for livestock grazing or the production of seed or hay crops, typically on a perennial cycle. Pasture/hay vegetation accounts for greater than 20% of total vegetation.

* 
  82  **Cultivated Crops** - areas used for the production of annual crops, such as corn, soybeans, vegetables, tobacco, and cotton, and also perennial woody crops such as orchards and vineyards. Crop vegetation accounts for greater than 20% of total vegetation. This class also includes all land being actively tilled.   

*Wetlands*


* 
  90  **Woody Wetlands**\ - areas where forest or shrubland vegetation accounts for greater than 20% of vegetative cover and the soil or substrate is periodically saturated with or covered with water.

* 
  95  **Emergent Herbaceous Wetlands** - areas where perennial herbaceous vegetation accounts for greater than 80% of vegetative cover and the soil or substrate is periodically saturated with or covered with water.

</details>
</ul>


* **LCC System for Ghana**\ : Currently, the best available land cover maps for Ghana are those developed by the USGS at 30 m resolution for three years - 1975, 200, and 2013. The Figure below shows the classification of Ghana for the three years (\ `Source <https://eros.usgs.gov/westafrica/land-cover/land-use-land-cover-and-trends-ghana>`_\ ). 
  </p>
  :raw-html-m2r:`<p align="center">
  <img src="https://user-images.githubusercontent.com/87503837/142496834-09496d67-12e2-44a8-93bc-69001f5dbea9.gif" alt="animated" />
  </p>`

  .. raw:: html

     <ul>


Efforts are ongoing to develop a harmonized LCC specific for West Africa land covers. The current scheme for the Regional Land Cover Mapping (RLCM) in West Africa is given
below, and details are available :raw-html-m2r:`<a href="https://github.com/SERVIR-WA/GALUP/files/7573319/RLCM.pdf" target="_blank">here</a>`. 

 :raw-html-m2r:`<details>`


.. raw:: html

   <summary> <b> RLCM (Class name, Description) </b> </summary>



* **Forêt / Forest** - dense, closed canopy formation of evergreen or semi-evergreen broadleaf vegetation with a multiple strata structure that includes scattered emergent trees. Upper stratum of trees over 30 m tall. Understory composed of evergreen or semievergreen shrubs; herbaceous cover is discontinuous.
* **Forêt Galerie & Formation Ripicole / Gallery Forest & Riparian Forest** - forest formations forming a band or corridor of dense vegetation along permanent or temporary watercourses; generally closed canopy and similar in structure to forest; their width, extent, and luxuriance depend on the width, and depth of the valleys they follow, as well as the depth and dynamics of the water table. Riparian forest is similar in structure but is found bordering the edges of streams and rivers.
* **Forêt Dégradée / Degraded Forest** - dense, evergreen broadleaf forest with closed or partially closed canopy whose integrity has been degraded by logging or other forms of exploitation. Degraded forest can also be immature forest, or forest in various stages of regrowth after disturbance. Trees 10 to 30 m tall.
* **Forêt Claire / Woodland** - open formations of small to medium height trees; tree height over 10 m and tree cover generally between 50 and 75 percent; canopies are often contiguous, with open areas between trees; grass understory can be scattered to dense, often associated with other herbaceous plants.
* **Forêt Marécageuse / Swamp Forest** - open to dense forests associated with temporarily or permanently waterlogged soils; these forests are generally found in natural depressions, seasonally inundated.
* **Plantation** - regular stands of trees planted for the purpose of producing food, beverages, vegetable oils, raw materials for industry, wood, or for protection against wind and water erosion.
* **Mangrove** - coastal forests of stilted shrubs or trees bordering the ocean or coastal estuaries, composed of one or several mangrove species. 
* **Fourré / Thicket** - dense stand of shrubs, often thorny, forming generally impenetrable cover, with minimal or no herbaceous ground cover.
* **Savane / Savanna** - herbaceous vegetation with mainly grasses that generally exceed 80 cm in height; dominated by annual and perennial grasses typically associated with the Sudan and Guinea zones; ground cover often consumed by annual fires; woody vegetation is usually present. The savanna class includes several major types or subclasses, based on density of shrubs and trees; the land use/land cover maps do not distinguish between shrub savanna, tree savanna, and wooded savanna; nevertheless, it is useful to define them:
* **Savane Herbacée / Herbaceous Savanna** - continuous herbaceous ground cover; trees and shrubs normally absent; this class is represented on the land use / land cover maps.
* **Savane Sahélienne / Sahelian Short Grass Savanna** - scattered trees and shrubs (or only shrubs) with a continuous herbaceous understory usually dominated by annual grasses generally associated with the Sahelian zone; woody cover between 1 and 25 percent.
* **Bowé** – flat, open surfaces that generally occur as lateritic plateaus; the skeletal, ferruginous soils form a hardened, impenetrable surface, generally absent of woody vegetation, but supporting varying quantities of herbaceous cover during the rainy season.
* **Steppe** - open, discontinuous herbaceous ground cover, often mixed with shrubs and trees; insufficient cover to carry fire; scattered annual grasses accompanied by widely spaced perennials. 
* **Surfaces Sableuses / Sandy Area** – beach sand or shifting mounds of sand, formed by wind; active dunes.
* **Terrains Rocheux / Rocky Land** - areas of rocky surfaces or outcrops, consisting of rocky peaks, batholiths, talus slopes, crest lines, cliffs, conglomerates, etc.
* **Sols Dénudés / Bare Soil** - land with little or no vegetation cover, exposing the soil; examples include eroded slopes, gravesl plains, sebkhas, and badlands.
* **Habitations / Settlements** - built up areas comprising human communities in a village, town or city.
* **Zone de Culture / Agriculture** - cultivated areas, with crops dependent on rainfall.
* **Cultures Irriguées / Irrigated Agriculture** - cultivated areas where crops receive water through an irrigation system to support their growth without relying on rainfall.
* **Cultures des Bas-Fonds et de Décrue / Agriculture in Shallows and Recession** - cultivated areas in depressions or along river banks where crop development occurs as the waters recede during the dry season.
* **Cultures et Jachères Sous Palmier à Huile / Cropland and Fallow with Oil Palms** - cultivated areas, with scattered oil palms in the fields; crops are mainly dependent on rainfall.
* **Carrière / Open Mine** - open pit where rock material is mined
* **Prairie Marécageuse – Vallée Inondable / Wetland – floodplain** - herbaceous or aquatic vegetation in permanent or semi-permanent wetlands and swamps.
* **Plans D’eau / Water Bodies** - Any area with permanent or semipermanent surface water.
  </details>
  </ul>

3. Land cover classification in GEE
-----------------------------------

:pushpin: Explanations for SVM, random forests, and CCDC for Google Earth Engine can be found on the GEE guides: `Supervised Classification <https://developers.google.com/earth-engine/guides/classification>`_\ , `CCDC <https://gee-ccdc-tools.readthedocs.io/en/latest/>`_ 

The figure below shows the flow diagram of the classification process that will be used in this workshop.
</p>


.. raw:: html

   <p align="center">
     <img src="https://user-images.githubusercontent.com/84922404/142555956-2c22826e-671e-45bf-a6c7-68718c9cde28.png" />
   </p>


Exercise and Post-Module Survey (required)
------------------------------------------


#. Please complete and submit `Exercise 1 <https://github.com/SERVIR-WA/GALUP/blob/master/training/2_rs/Exercises/M4_Exercise1.md>`_ for Module 4.
#. Submit the Post-Module `survey <https://ufl.qualtrics.com/jfe/form/SV_6VxnjyVgVx04GuG>`_. 
#. Submit the Post-Training `survey <https://ufl.qualtrics.com/jfe/form/SV_8cvoKZLDrBllPkG>`_ 

#
=

**Previous Section:**

:raw-html-m2r:`<a href="module3.md" title="Module 3">Module 3</a>`
