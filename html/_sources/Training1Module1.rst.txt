.. role:: raw-html-m2r(raw)
   :format: html


Module 1 - Software and Data Preparation
========================================

**What will you learn from this module?**


* Installing QGIS and PyLUSAT, and loading *LUCIS-OPEN Tools for QGIS*\ ,
* Be familiar with the user interface of QGIS 3.10.8,
* Visualizing GIS data and creating maps.

1. Software Installation
------------------------

..

   :pushpin: Note on installation:\ :raw-html-m2r:`<br>`
   Follow the `instruction <https://github.com/SERVIR-WA/GALUP/wiki/Install>`_
   to install `QGIS 3.10.8 <https://qgis.org/en/site/>`_ and
   `PyLUSAT v0.5.2 <https://github.com/chjch/pylusat>`_\ , which must be installed
   before we can successfully load and run the tools GALUP have developed.


2. GIS Datasets
---------------


* The table below lists the GIS datasets used for this module.
* They can be found within the downloaded *zip* folder from the previous
  section at ``GALUP-master -> training -> 1_lu -> datasets``.

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
   * - 3
     - healthsites.shp
     - vector
     - point
     - Health facilities in Ghana
   * - 4
     - GHARoads2020PrimarySecondary.shp
     - vector
     - line
     - Primary and secondary roads in Ghana


3. Working with QGIS 3.10.8
---------------------------

In this section, we will explore the QGIS
`Graphical User Interface <https://docs.qgis.org/3.10/en/docs/user_manual/introduction/qgis_gui.html>`_
(GUI) and the basic functions including visualizing GIS data and creating maps.

To get an overview and understand each GUI element's purposes, including
(1) **Layers List / Browser Panel**\ , (2) **Toolbars**\ , (3) **Map canvas**\ ,
(4) **Status bar**\ , (5) **Side Toolbar**\ , (6) **Locator bar**\ , please checkout
this `page <https://docs.qgis.org/3.10/en/docs/training_manual/basic_map/overview.html>`_.

Moreover, you can customize the GUI by dragging and moving *Panels* and
*Toolbars* to the place you prefer (see the animation below).

.. image:: ../../../img/gif/m1_custom_gui.gif
   :target: ../../../img/gif/m1_custom_gui.gif
   :alt: gui_custom


3.1 Add Data to `\ *Map Canvas* <https://docs.qgis.org/3.10/en/docs/training_manual/basic_map/mapviewnavigation.html>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. The primary way to add data to QGIS Map Canvas is by **Drag-and-Drop**
   items in the `Browser panel <https://docs.qgis.org/3.10/en/docs/user_manual/introduction/browser.html?#the-browser-panel>`_.
#. Another way to add data is by
   `\ **loading layer from a file** <https://docs.qgis.org/3.10/en/docs/user_manual/managing_data_source/opening_data.html?#loading-a-layer-from-a-file>`_.\ :raw-html-m2r:`<br>` :raw-html-m2r:`<br>`
   ..

      :pushpin: Use Favorites to quickly get to the data you used frequently:\ :raw-html-m2r:`<br>`
      In the Browser Panel, you can also add the folder you frequently used to
      `Favorites <https://docs.qgis.org/3.10/en/docs/training_manual/basic_map/overview.html?highlight=Favorites#basic-the-browser-panel>`_. To avoid long path shown in
      the Favorites, you can also ``Rename Favorite...``.


#. Now, lets load *Districts of Ghana*\ , *Road Network*\ , and *Health Facility*
   to Map Canvas, as shown in below.


.. raw:: html

   <div align="center">

   |               Add Data to Map Canvas            |
   |:-------------------------------------------------:|
   | <img src="../../../img/map/m1_AddData.png" width="600"> |

   </div>


3.2 Check data in the *Attribute Table*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `Attribute Table <https://docs.qgis.org/3.10/en/docs/user_manual/working_with_vector/attribute_table.html?highlight=attribute#introducing-the-attribute-table-interface>`_ displays
information on features of a selected layer.


* Right click the layer of your interest, and
  click ``Open Attribute Table``.
* As circled in the image below, the title of the Attribute Table window
  includes: 1) the title of the layer, 2) the total number of the features in
  the layer, 3) the number of features are filtered, and 4) the number of
  features are selected.


.. raw:: html

   <div align="center">

   |               Attribute Table           |
   |:-------------------------------------------------:|
   | <img src="../../../img/gui/window/m1_attribute_table.png" width="600"> |

   </div>


3.3 Change Symbology of a Layer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The symbology of a layer is one of important functions in GIS. By presenting the
data with a dynamic visual appearance on the map, you can better explore the data
as you are working with it.


* Symbolize the vector layers using
  `Single Symbology <https://docs.qgis.org/3.10/en/docs/training_manual/basic_map/symbology.html?#basic-fa-changing-colors>`_
  in the layer properties.
* Choose the `Categorized <https://docs.qgis.org/3.10/en/docs/user_manual/working_with_vector/vector_properties.html?#categorized-renderer>`_
  option to present the data, if you have data that is
  broken into categories (the image in the middle is using region column).
* Choose the `Graduated <https://docs.qgis.org/3.10/en/docs/user_manual/working_with_vector/vector_properties.html?#graduated-renderer>`_
  option to present the data, if you have numeric data you want
  to symbolize (the image on the right is using the population column).

.. list-table::
   :header-rows: 1

   * - Single Symbology
     - Categorized Symbology
     - Graduated Symbology
   * - 
     .. image:: ../../../img/map/m1_Single.png
        :target: ../../../img/map/m1_Single.png
        :alt: basemap
     
     - 
     .. image:: ../../../img/map/m1_Categorized.png
        :target: ../../../img/map/m1_Categorized.png
        :alt: basemap
     
     - 
     .. image:: ../../../img/map/m1_Graduated.png
        :target: ../../../img/map/m1_Graduated.png
        :alt: basemap
     


3.4 Add a *Basemap* to Map Canvas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A `Basemap <https://rdkb.sgrc.selkirk.ca/Help/Content/Client_APIs/SV_User/SVU_AboutBaseMaps.htm>`_
is a layer with geographic information that serves as a background. A base map
provides context for additional layers that are overlaid on top of the base map.
In this module, we use `\ **QuickMapServices** <https://docs.qgis.org/3.10/en/docs/training_manual/qgis_plugins/plugin_examples.html#basic-fa-the-quickmapservices-plugin>`_\ , a QGIS
`Plugin <https://docs.qgis.org/3.10/en/docs/user_manual/plugins/plugins.html>`_\ ,
to add basemap to Map Canvas.


#. Open the `\ **Plugins** <https://docs.qgis.org/3.10/en/docs/training_manual/qgis_plugins/fetching_plugins.html?#basic-fa-managing-plugins>`_
   window at the *main menu toolbar*\ ,
   and click ``Manage and Install Plugins...``.
#. Search and `install a new Plugin <https://docs.qgis.org/3.10/en/docs/training_manual/qgis_plugins/fetching_plugins.html?#basic-fa-installing-new-plugins>`_ called **QuickMapServices**.
#. After installation, open the **QuickMapServices Settings** window, click the
   *More Services* tab, and click *Get contributed pack* to get more basemaps.
   For details, please check out this `tutorial <https://opengislab.com/blog/2018/4/15/add-basemaps-in-qgis-30>`_.
#. Choose one basemap from the **QuickMapServices** and add it to Map Canvas.

   .. image:: ../../../img/gui/menu/qms_web_icons.png
      :target: ../../../img/gui/menu/qms_web_icons.png
      :alt: icons


.. raw:: html

   <div align="center">

   |                Layer with a Basemap                  |
   |:-------------------------------------------------:|
   | <img src="../../../img/map/m1_basemap.png" alt= "basemap" width="700"> |

   </div>


3.5 Create a *Layout* to Print Your Map
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After setting up the map, you are now ready to `layout <https://docs.qgis.org/3.10/en/docs/training_manual/map_composer/map_composer.html#ls-using-print-layout>`_ your map and print it (as a pdf file)
to share with your colleagues.


* Open the `\ **Layout Manager** <https://docs.qgis.org/3.10/en/docs/training_manual/map_composer/map_composer.html#basic-fa-the-layout-manager>`_ window, click the *Create...* button, and
  name your map and click *OK* to open the map window.
* In the map window, click the `\ ``Add Item`` <https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/overview_composer.html#add-item-menu>`_ button on the main menu bar, and
  click add map.
* In order to have a decent map, you need: 1) a `\ **Title** <https://docs.qgis.org/3.10/en/docs/training_manual/map_composer/map_composer.html#basic-fa-adding-a-title>`_ for your map, 2) a
  `\ **Legend** <https://docs.qgis.org/3.10/en/docs/training_manual/map_composer/map_composer.html#basic-fa-adding-a-legend>`_
  to identify the elements in the map, 3) a `\ **Scale Bar** <https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/composer_items/composer_scale_bar.html?#the-scale-bar-item>`_
  to indicates the scale of the map, 4) a `\ **North Arrow** <https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/composer_items/composer_image.html?#the-picture-and-the-north-arrow-items>`_ to
  indicate the direction. You can add these items under the ``Add Item`` button.
* After you finishing all the layout of your map, click the ``Layout`` button on
  the main menu bar, and click `\ ``Export as PDF...`` <https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/create_output.html#export-layout-pdf>`_ to export your map. (If the basemap cannot be rendered
  in the PDF file, try a lower *dpi* (e.g., 150 dpi) in the
  `\ **Export Setting** <https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/overview_composer.html#export-settings>`_
  in the `\ **Layout Panel** <https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/overview_composer.html#the-layout-panel>`_.)
* See the example map in PDF file `here <../pdf_download/PopulationMap.pdf>`_.

4. Exercises and Post-training Survey
-------------------------------------


* Please complete the `Exercise 1 <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m1_exercise1.md#exercise-1>`_.
* Please complete the `Exercise 2 <https://github.com/SERVIR-WA/GALUP/blob/master/training/1_lu/exercises/m1_exercise2.md#exercise-2>`_.
* Please take this post-training
  `survey <https://ufl.qualtrics.com/jfe/form/SV_3n21W1ko0UPJNLo>`_ (required).
* Please submit your exercises `here <https://github.com/SERVIR-WA/GALUP/issues/new?assignees=&labels=submission+w1m1&template=exercise-submission-template.md&title=Module+1+exercises+%5Breplace+with+your+name%5D>`_.

5. Additional Resources
-----------------------


* `QGIS User Guide <https://docs.qgis.org/3.16/en/docs/user_manual/>`_
* `What is GIS and why use QGIS <https://www.youtube.com/watch?v=8oEnJvLzDnQ>`_
  (YouTube video by `Statistics Canada <https://www.youtube.com/channel/UCvfquhvHW5ffRamjLHdXDtQ>`_\ )
* `Git & GitHub Tutorials for Beginners <https://www.youtube.com/playlist?list=PL4cUxeGkcC9goXbgTDQ0n_4TBzOO0ocPR>`_
  (YouTube playlist by `The Net Ninja <https://www.youtube.com/c/TheNetNinja>`_\ )
* `OpenSourceOptions Tutorials <https://opensourceoptions.com/blog/>`_

6. What's Next?
---------------

Module 2 - Introduction to LUCIS-OPEN Tools for QGIS.
