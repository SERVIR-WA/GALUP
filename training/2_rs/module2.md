# Module 2 - Remote Sensing Applications using Google Earth Engine

**What will you learn from this module?**

- Set up Google Earth Engine (GEE)
- Familiarize with GEE Interface
- Download and visualize RS data using Code Editor in GEE 

## 1. Setting up GEE 
Please request an account with Google Earth Engine (GEE) as follows:
- Go to the GEE webpage [here](https://earthengine.google.com/)
- Select “Sign Up” at the top right of the page and input institution and intention for use (e.g. using remote sensing datasets for land use suitability modeling).

:pushpin: Approval may not happen immediately, so please be sure to sign up in advance of the workshop to provide a few days for completion.


## 2. Exploring GEE Interface

The video and Figure below show general interface functions for GEE. Further description of the components of the Figure can be found [here](https://github.com/ecodynlab/GALUP/wiki/GEE-Interface). 

<p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/55447fcbfc2f487ebaae8d1258e829ca1d" target="_blank">
    <img src="https://user-images.githubusercontent.com/84922404/135470199-719878b5-7cb6-4a7a-aacd-e40881cda2e3.JPG" alt= "GEE Tutorial" width="800">
  </a>
</p>
  
![GEEinterface](https://user-images.githubusercontent.com/84922404/132246323-4b2d7dee-6cdc-4828-aa9a-b3ab4193ffa5.png)


:pushpin: In this workshop, we will be programming in the GEE [code editor](https://code.earthengine.google.com/) that uses the JavaScript language. There are extra [resources](https://developers.google.com/earth-engine/tutorials/tutorial_api_01) available from Google to introduce the JavaScript Application Programming Interface (API).

## 3. Using GEE to Explore RS Concepts from Module-1

### 3.1 Downloading and Visualizing Landsat Data
In the following example, we will use GEE to download and visualize Landsat satellite data in Ghana. Please use the video tutorial in Section 3.2 to follow along.
- Copy the script ["01_search_and_display"](https://github.com/ecodynlab/GALUP/wiki/Scripts) and paste into the GEE [code editor](https://code.earthengine.google.com/). This is the same script that will be used in Exercise with slight alterations necessary to complete the Exercise.  
- The script includes: <br/>
      **a.** Defining variables for dates of interest: **ST_DATE** and **EN_DATE** <br/>
      **b.** Defining the region of interest using 4 coordinates: **Longitude_min**, **Latitude_min**, **Longitude_max**, **Latitude_max** <br/>
            :pushpin: Latitudes south of Equator and Longitudes west of Greenwich Meridian are negative. <br/>
      **c.** Defining variables for RS data products: Here, data products from **Landsat 5, 7, and 8** are used.<br/>
      **d.** Selecting the data product: **Landsat 5** <br/>
      **e.** Filtering the data product by the region and dates of interest, and by the amount of cloud cover. <br/>
      **f.** Repeating **d** and **e** with **Landsat 7 & 8** <br/>
      **g.** Setting the visualization parameters for each product: **bands**, **min**, **max**, **gamma** <br/>
              > For information on Landsat bands, please refer to [Module-1](https://github.com/SERVIR-WA/GALUP/blob/master/training/2_rs/module1.md) <br/>
              > The parameters **min**, **max**, and **gamma** describe the RGB visual representation. For more details on these, see [here](https://developers.google.com/earth-engine/guides/image_visualization) <br/>
      **h.** Mapping the images: Centering, and adding RS data in three layers. <br/>
      **i.** Exporting images to Google Drive

### 3.2 Video Tutorial for the Section 3.1
Use the video tutorial to follow along with the example. This may also be useful in completing the exercise.

<p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/68693a462a914666807e47f992dedde11d" target="_blank" rel="noopener">
    <img src="https://user-images.githubusercontent.com/84922404/140551115-a0e9d6fa-ae4b-4357-99be-0a27b1901394.png" alt= "GEE Tutorial" width="800">
  </a>
</p>

## Exercise and Post-Module Survey (required)
1. Please complete and submit [Exercise](https://github.com/ecodynlab/GALUP/blob/main/Exercises/M2_exercise1.md) for Module 2.
2. Submit the Post-Module [survey](https://ufl.qualtrics.com/jfe/form/SV_6fIRnsK59HEwZ9k). 

</p>

##
**Next Section:**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; **Previous Section:**

<a href="Module 3.md" title="Module 3">Module 3</a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="Module 1.md" title="Module 1">Module 1</a>



