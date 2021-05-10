# Module 1 - Software and Data Preparation

**What will you learn from this module?**

- Installing QGIS and PyLUSAT (Python for Land Use Suitability Analysis Tools),
- Introducing the interface of QGIS 3.10.8,
- Visualizing the datasets prepared for this series of trainings in QGIS.

**Upon completion, please take this [survey](https://docs.google.com/document/d/1p1oy635ZMgXBcyxPJPv2Je-62xTVaNV6xCtltQYvde0/edit)
to help us improve this tutorial.**

<hr style="height:1px;border-width:0;background-color:LightGray"> </hr>

## 1. Software Installation

- Follow the [instruction](https://github.com/chjch/lucis_qgis/wiki/Installation)
  to install the QGIS software and the Python package, PyLUSAT, which must be
  installed before we can successfully load and run the tools GALUP have
  developed.
  - [QGIS 3.10.8](https://qgis.org/en/site/)
  - [PyLUSAT v0.4.0](https://pypi.org/project/pylusat/)

## 2. Get familiar with QGIS user interface

We will explore the QGIS user interface so that you are familiar with the
menus, toolbars, map canvas and layers list that form the basic structure of
the interface.

- Elements of the QGIS GUI (Graphic User Interface)
  - Layers List / Browser Panel
  - Toolbars
  - Map canvas
  - Status bar
  - Side Toolbar
  - Locator bar
  - Attribute Table
    - Put the cursor on a layer of your interest, and right click the layer and click _Open Attribute Table_.
    - The title of the Attribute Table window includes the name of the layer, the total number of the features in the layer, the number of features are filtered, and the number of features are selected. You can find the attributes of all features in the layer.
  - Basemap
    - To install the basemap, you need to go to the menu toolbar, click _Plugins_, and click _Manage and Install Plugins..._. ![basemap1](../../../images/Basemap/basemap.png)
    - In the **Plugin** Window, search for **QuickMapServices** then click Install button. ![basemap_ins](../../../images/Basemap/quick_map_ins.png)
    - After it installs, you should be able to find the _QuickMapServices_ button in the Web Toolbar. ![QuickMapServices](../../../images/Basemap/quick_service.png)
    - Click the _QuickMapServices_ button and click _Settings_.
    - In the **QuickMapServices Settings** window, click the _More Services_ tab, and click _Get contributed pack_ to get more basemaps.
    ![settings](../../../images/Basemap/settings.png)
    - Now try to click the _QuickMapServices_ button again, and you will see more basemap options.
  - Export your Own Map
    - After you finishing your map, then you are ready to export it. You can click the _Show Layout Manager_ button on the attribute toolbar to open the **Layout Manager** window.(Or you can click the _Project_ button on the menu toolbar and click _Layout Manager..._)
    - In the **Layout Manager** window, click the _Create..._ button, and name your map and click _OK_ to open the map window.![create_layout](../../../images/Export_ur_own_map/layout_manager.png)
    - In the map window, click the _Add Item_ button on the main menu bar, and click add map. Select an area to render your map. ![add_map](../../../images/Export_ur_own_map/add_map.gif)
    - In order to have a decent map, you might need _Add Label_ to set the name of your map, _Add Legend_ to identify the elements in the map, _Add Scale Bar_ to use a scale bar to indicates the scale of the map, _Add North Arrow_ to add a north arrow. You can add these items under the _Add Item_ button.
    - You can edit the items you added at windows the right side.
    ![edit](../../../images/Export_ur_own_map/edit.png)
    - After you finishing all the layout of your map, click the _Layout_ button on the main menu bar, and click _Export as PDF..._ to export your map.
  
- Customize the QGIS GUI to fits your own preferences and needs.

## 3. Get to know the datasets

- [Download](https://github.com/chjch/lucis_qgis) the datasets from GitHub
- Open data in QGIS
- Change the symbology of the dataset

## 4. Exercises

- Please complete the exercise [here](https://github.com/chjch/lucis_qgis).

## 5. Additional Resources

- [What is GIS and why use QGIS](https://www.youtube.com/watch?v=8oEnJvLzDnQ)
- [QGIS User Guide](https://docs.qgis.org/3.16/en/docs/user_manual/)

## 6. What's Next?

Module 2 - Introduction to LUCIS<sup>OPEN</sup> Tools