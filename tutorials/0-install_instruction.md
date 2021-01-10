# How to Install

## 1. Install QGIS

1. **Step 1 - Download**:
   - Go to the [this page](https://qgis.org/en/site/) and follow the instruction below to download the right version of *QGIS (3.8.10)*.
   - Go to the https://github.com/chjch and follow the instruction below to download **_lucis_qgis_** folder.

![qgis_mainpage](images/qgis_mainpage.png)
2. **Step 2 - Install**:

3. 

 (1) Double-click the *QGIS (3.8.10)* installation file you just downloaded from last step, follow the instructions to install the application on your computer.

 (2）Open the *lucis_qgis* folder (the folder name is **lucis_qgis-master**) you just download from last step.

  - Open the *install* folder and the copy the *QGIS 3.10.8* folder to the root folder of the *QGIS (3.8.10)* (**here is the QGIS 3.10**).

  - Open the *QGIS 3.10.8* folder and double click the *install_pylusat* file.

  - Specify the root folder of **QGIS 3.10** for the first question and type *Y*
for the second question.

  - Press Enter key and wait the installation to be completed.


- **Step 3 - Open the software**: 

 (1) Open the QGIS 3.10 folder on the desktop and double click the *QGIS Desktop 3.10.8* file. 
  
  - Click the python icon in the *Processing Toolbox* and click *add script to tool box*.

  - Find the the *lucis_qgis* folder we download in the first step and open the *algorithm* folder.

  - Add all files into the QGIS. And you can find all the tools in the *Scripts* branch in the *Processing Toolbox*.

## 3. Getting to know Q GIS

### 3.1 Create a Q GIS Project

- Open a Project and Create a New Project
 * Click Project at menu toolbar and choose Open to select projects created before.
 * Click Project at menu toolbar and choose New to creat a new project. (or press Ctrl + N)


### 3.2 Getting to know the User Interface

1. Project Ribbon
 * Map Tab: basic mapping operations
 * Menu Toolbar: displays the available menus and commands. 
 * Analysis Tab: Project Toolbar, Data Source Manager Toolbar and more

2. The Browser Panel - navigate your database (View ‣ Panels ‣ Browser)
- Access to common vector files (e.g. ESRI shapefile or MapInfo files), databases (e.g.PostGIS, Oracle, Spatialite or MSSQL Spatial) and WMS/WFS connections. You can also view your GRASS data.

3. The Layers List
* Expanding collapsed items (by clicking the arrow or plus symbol beside them) will provide you with more information on the layer’s current appearance.
* Right-clicking on a layer will give you a menu with lots of extra options。

4. Processing Toolbox
* It shows the list of all available algorithms grouped in different blocks called Providers, and custom models and scripts you can add to extend the set of tools.

5. The Stature Bar
- Shows you information about the current map. Also allows you to adjust the map scale and see the mouse cursor’s coordinates on the map.

### 3.3 Add Data to Map and work with symbology
- Add Study area boundary
- Work with vector symbology: census block
- Work with raster symbology: LULC ca. 2015