# Module 1 - Software and Data Preparation

**What will you learn from this module?**

- Installing QGIS and PyLUSAT, and loading _LUCIS-OPEN Tools for QGIS_,
- Be familiar with the user interface of QGIS,
- Visualizing GIS data and creating maps.

## 1. Software Installation

> :pushpin: Note on installation:<br>
> To set up your computer, please **download** and **install** [QGIS 3.20](https://download.qgis.org/downloads/windows/3/3.20/QGIS-OSGeo4W-3.20.0-2.msi). We recommend all participants for the Chobe Open-LUCIS (COL) training to use this version of QGIS for consistency. The latest version of **QGIS** and other resources can be found [here](https://qgis.org/en/site/). Please follow the [instruction](https://servir-wa.github.io/GALUP/html/pylusat.html) to install the **Python for Land-use Suitability Analysis Tools** (PyLUSAT), which must be installed
> before we can successfully start the COL training. The PyLUSAT tools to be loaded and run for this training were developed by GALUP.

## 2. GIS Datasets

- The table below lists the GIS datasets used for this module.
- They can be found within the downloaded _zip_ folder from the previous
  section at `GALUP-master -> training -> 1_lu -> datasets`.

| ID | File Name                        | Data Format | Type    | Description                     |
|----|----------------------------------|-------------|---------|---------------------------------|
| 3  | BWA_Healthsites.shp              | vector      | point   | Health facilities in Botswana | 
| 4  | BWA_Roads_PrimarySecondary2023.shp | vector | line | Primary and secondary roads in Botswana |
| 1  |   BWA_ADM_2021.shp               | vector      | polygon | Districts of Botswana|
| 2  | BWA_Population_Density.tif | raster | tiff | Population of Botswana in 2022|

## 3. Working with QGIS

In this section, we will explore the QGIS
[Graphical User Interface](https://docs.qgis.org/3.10/en/docs/user_manual/introduction/qgis_gui.html)
(GUI) and the basic functions including visualizing GIS data and creating maps.

To get an overview and understand each GUI element's purposes, including
(1) **Layers List / Browser Panel**, (2) **Toolbars**, (3) **Map canvas**,
(4) **Status bar**, (5) **Side Toolbar**, (6) **Locator bar**, please checkout
this [page](https://docs.qgis.org/3.10/en/docs/training_manual/basic_map/overview.html).

Moreover, you can customize the GUI by dragging and moving _Panels_ and
_Toolbars_ to the place you prefer (see the animation below).
![gui_custom](../../../img/gif/m1_custom_guiBW.gif)

### 3.1 Add Data to [_Map Canvas_](https://docs.qgis.org/3.10/en/docs/training_manual/basic_map/mapviewnavigation.html)

1. The primary way to add data to QGIS Map Canvas is by **Drag-and-Drop**
   items in the [Browser panel](https://docs.qgis.org/3.10/en/docs/user_manual/introduction/browser.html?#the-browser-panel).
2. Another way to add data is by
   [**loading layer from a file**](https://docs.qgis.org/3.10/en/docs/user_manual/managing_data_source/opening_data.html?#loading-a-layer-from-a-file).<br> <br>
   > :pushpin: Use Favorites to quickly get to the data you used frequently:<br>
   > In the Browser Panel, you can also add the folder you frequently used to
   > [Favorites](https://docs.qgis.org/3.10/en/docs/training_manual/basic_map/overview.html?highlight=Favorites#basic-the-browser-panel). To avoid long path shown in
   > the Favorites, you can also `Rename Favorite...`.
3. Now, lets load _Districts of Botswana_, _Road Network_, and _Health Facility_
to Map Canvas, as shown in below.

<div align="center">

|               Add Data to Map Canvas            |
|:-------------------------------------------------:|
| <img src="../../../img/map/m1_AddDataBW.png" width="500"> |

</div>

### 3.2 Check data in the _Attribute Table_

The [Attribute Table](https://docs.qgis.org/3.10/en/docs/user_manual/working_with_vector/attribute_table.html?highlight=attribute#introducing-the-attribute-table-interface) displays
information on features of a selected layer.

- Right click the layer of your interest, and
  click `Open Attribute Table`.
- As circled in the image below, the title of the Attribute Table window
  includes: 1) the title of the layer, 2) the total number of the features in
  the layer, 3) the number of features are filtered, and 4) the number of
  features are selected.

<div align="center">

|               Attribute Table           |
|:-------------------------------------------------:|
| <img src="../../../img/gui/window/m1_attribute_tableBW.png" width="600"> |

</div>

### 3.3 Change Symbology of a Layer

The symbology of a layer is one of important functions in GIS. By presenting the
data with a dynamic visual appearance on the map, you can better explore the data
as you are working with it.

- Symbolize the vector layers using
  [Single Symbology](https://docs.qgis.org/3.10/en/docs/training_manual/basic_map/symbology.html?#basic-fa-changing-colors)
  in the layer properties.
- Choose the [Categorized](https://docs.qgis.org/3.10/en/docs/user_manual/working_with_vector/vector_properties.html?#categorized-renderer)
  option to present the data, if you have data that is
  broken into categories (the image in the middle is using region column).
- Choose the [Graduated](https://docs.qgis.org/3.10/en/docs/user_manual/working_with_vector/vector_properties.html?#graduated-renderer)
  option to present the data, if you have numeric data you want
  to symbolize (the image on the right is using the population column).

|  Single Symbology  |  Categorized Symbology |  Graduated Symbology  |
|:------------------:|:----------------------:|:---------------------:|
| ![basemap](../../../img/map/m1_SingleBW.png)  | ![basemap](../../../img/map/m1_CategorizedBW.png)  | ![basemap](../../../img/map/m1_GraduatedBW.png)  |

### 3.4 Add a _Basemap_ to Map Canvas

A [Basemap](https://rdkb.sgrc.selkirk.ca/Help/Content/Client_APIs/SV_User/SVU_AboutBaseMaps.htm)
is a layer with geographic information that serves as a background. A base map
provides context for additional layers that are overlaid on top of the base map.
In this module, we use [**QuickMapServices**](https://docs.qgis.org/3.10/en/docs/training_manual/qgis_plugins/plugin_examples.html#basic-fa-the-quickmapservices-plugin), a QGIS
[Plugin](https://docs.qgis.org/3.10/en/docs/user_manual/plugins/plugins.html),
to add basemap to Map Canvas.

1. Open the [**Plugins**](https://docs.qgis.org/3.10/en/docs/training_manual/qgis_plugins/fetching_plugins.html?#basic-fa-managing-plugins)
window at the _main menu toolbar_,
and click `Manage and Install Plugins...`.
2. Search and [install a new Plugin](https://docs.qgis.org/3.10/en/docs/training_manual/qgis_plugins/fetching_plugins.html?#basic-fa-installing-new-plugins) called **QuickMapServices**.
3. After installation, open the **QuickMapServices Settings** window, click the
_More Services_ tab, and click _Get contributed pack_ to get more basemaps.
For details, please check out this [tutorial](https://opengislab.com/blog/2018/4/15/add-basemaps-in-qgis-30).
4. Choose one basemap from the **QuickMapServices** and add it to Map Canvas.
   ![icons](../../../img/gui/menu/qms_web_icons.png)

<div align="center">

|                Layer with a Basemap                  |
|:-------------------------------------------------:|
| <img src="../../../img/map/m1_basemapBW.jpeg" alt= "basemap" width="400"> |

</div>

### 3.5 Create a _Layout_ to Print Your Map

After setting up the map, you are now ready to [layout](https://docs.qgis.org/3.10/en/docs/training_manual/map_composer/map_composer.html#ls-using-print-layout) your map and print it (as a pdf file)
to share with your colleagues.
  
- Open the [**Layout Manager**](https://docs.qgis.org/3.10/en/docs/training_manual/map_composer/map_composer.html#basic-fa-the-layout-manager) window, click the _Create..._ button, and
name your map and click _OK_ to open the map window.
- In the map window, click the [`Add Item`](https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/overview_composer.html#add-item-menu) button on the main menu bar, and
  click add map.
- In order to have a decent map, you need: 1) a [**Title**](https://docs.qgis.org/3.10/en/docs/training_manual/map_composer/map_composer.html#basic-fa-adding-a-title) for your map, 2) a
[**Legend**](https://docs.qgis.org/3.10/en/docs/training_manual/map_composer/map_composer.html#basic-fa-adding-a-legend)
to identify the elements in the map, 3) a [**Scale Bar**](https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/composer_items/composer_scale_bar.html?#the-scale-bar-item)
to indicates the scale of the map, 4) a [**North Arrow**](https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/composer_items/composer_image.html?#the-picture-and-the-north-arrow-items) to
indicate the direction. You can add these items under the `Add Item` button.
- After you finishing all the layout of your map, click the `Layout` button on
  the main menu bar, and click [`Export as PDF...`](https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/create_output.html#export-layout-pdf) to export your map. (If the basemap cannot be rendered
  in the PDF file, try a lower _dpi_ (e.g., 150 dpi) in the
  [**Export Setting**](https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/overview_composer.html#export-settings )
  in the [**Layout Panel**](https://docs.qgis.org/3.10/en/docs/user_manual/print_composer/overview_composer.html#the-layout-panel).)
- See the example map in PDF file [here](https://github.com/mogaetkpp/GALUP/tree/master/training/1_lu/pdf_maps/BWLayoutPrint.pdf).

## 4. Exercises and Post-training Survey

- Please complete the [Exercise 1](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/exercises/m1_exercise1.md#exercise-1).
- Please complete the [Exercise 2](https://github.com/mogaetkpp/GALUP/blob/master/training/1_lu/exercises/m1_exercise2.md#exercise-2).
- Please take this post-training
  [survey](https://ufl.qualtrics.com/jfe/form/SV_3n21W1ko0UPJNLo) (required).
- Please submit your exercises [here](https://github.com/SERVIR-WA/GALUP/issues/new?assignees=&labels=submission+w1m1&template=exercise-submission-template.md&title=Module+1+exercises+%5Breplace+with+your+name%5D).

## 5. Additional Resources

- [QGIS User Guide](https://docs.qgis.org/3.16/en/docs/user_manual/)
- [What is GIS and why use QGIS](https://www.youtube.com/watch?v=8oEnJvLzDnQ)
  (YouTube video by [Statistics Canada](https://www.youtube.com/channel/UCvfquhvHW5ffRamjLHdXDtQ))
- [Git & GitHub Tutorials for Beginners](https://www.youtube.com/playlist?list=PL4cUxeGkcC9goXbgTDQ0n_4TBzOO0ocPR)
  (YouTube playlist by [The Net Ninja](https://www.youtube.com/c/TheNetNinja))
- [OpenSourceOptions Tutorials](https://opensourceoptions.com/blog/)

## 6. What's Next?

Module 2 - Introduction to LUCIS-OPEN Tools for QGIS.
