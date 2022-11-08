# Workshop 4: Introduction to Remote Sensing - II

> **Instructor**: [Dr. Aditya Singh](https://abe.ufl.edu/people/faculty/aditya-singh/) (<ins>aditya01@<i></i>ufl.edu</ins>) <br>
> **Date**:<br>
> **Co-authors**: 
## Goal
The fourth GALUP workshop aims at applying skills learned in the second workshop -Introduction to Remote Sensing using Google Earth Engine (GEE) for further analysis. The participants will learn basics in Time Series Analysis and Change Detection and apply this to land use studies and analysis. This workshop is the second phase toward understanding how RS data can be used for land-use assessments.

## Objectives
- Time Series Analysis <br>
- Land cover change detection <br>
- Advanced spatial analysis <br>

# A recap of Introduction to Satellite Remote Sensing I
## 1. What did we learn
### What is Remote Sensing
**Remote sensing** is the science and art of obtaining information about an object, area, or phenomenon through the analysis of data acquired by a device that is not in contact with the object, area, or phenomenon under investigation<sup>1</sup>. Modern day remote sensing started with the advent of radar, sonar, and thermal infrared detection systems during World War II. Since then, detectors have been expanded to obtain information from most of the bands in the EM spectrum, with a variety of applications spanning from military use to agriculture. <br> 

### Types of Resolutions: <br>
- **Spatial resolution** describes how far apart two targets have to be so that they are detected as separate signals.<br>
- **Temporal resolution** describes how often a sensor observes the same target . <br>
- **Radiometric resolution** describes the number of wavelengths observed. For example, in the Figures below, a multispectral sensor observing about 10s of discrete bands and a hyperspectral sensor observing 100s of bands in the optical/NIR region.<br>
 
<br/>

<p align="center"> <b> Spectral sampling: Multispectral sensors (left) and Hyperspectral sensors (right) </b> <p>

<p align="center"> 
<img src="https://user-images.githubusercontent.com/87503837/133636464-24493df3-1c5d-405f-b7ec-10fe64cec5e7.png" width="400" height="220"><img src="https://user-images.githubusercontent.com/87503837/133636485-93336e1a-214b-4897-b1ca-c1206879b4e1.png" width="400" height="220"> 
 </p>
 
<br/>

<p align="center"> 
  <img src = "https://user-images.githubusercontent.com/87503837/130195843-a8aea0e9-def9-40c4-80ce-b562fd56e918.png"/>
</p> <br/>

### Data Sources 
Satellite data can be obtained from multiple sources, some important repositories are:
- <a href="https://earthexplorer.usgs.gov/">USGS Earth Explorer</a>
- <a href="https://search.earthdata.nasa.gov/search?ac=true">NASA Earthdata Search</a>
- <a href="https://worldview.earthdata.nasa.gov/">NASA Worldview</a>
- <a href="https://scihub.copernicus.eu/dhus/#/home">Copernicus Open Access Hub</a>
<br>

## 2. Setting up GEE 
Please request an account with Google Earth Engine (GEE) as follows:
- Go to the GEE webpage [here](https://earthengine.google.com/)
- Select “Sign Up” at the top right of the page and input institution and intention for use (e.g. using remote sensing datasets for land use suitability modeling).

:pushpin: Approval may not happen immediately, so please be sure to sign up in advance of the workshop to provide a few days for completion.

## 3. Exploring GEE Interface

The figure below shows general interface functions for GEE. Further description of the components of the Figure can be found [here](https://github.com/SERVIR-WA/GALUP/wiki/GEE-Interface). 
  
![GEEinterface](https://user-images.githubusercontent.com/84922404/132246323-4b2d7dee-6cdc-4828-aa9a-b3ab4193ffa5.png)

:pushpin: In this workshop, we will be programming in the GEE [code editor](https://code.earthengine.google.com/) that uses the JavaScript language. There are extra [resources](https://developers.google.com/earth-engine/tutorials/tutorial_api_01) available from Google to introduce the JavaScript Application Programming Interface (API).

## 4. RS Indices
**Remote sensing indices** (or spectral indices) are arithmentic combinations of reflectance at two or more bands that help provide measurable estimates of the relative abundance of indicators of interest. Vegetation indices (such as the normalized difference vegetation index: NDVI) are the most widely known, but indices can be formulated for tracking burn areas, exposed soil or built-up areas.
- Spectral/Image indices are generally calculated using simple mathematical transformations (addition, subtraction, division) conducted on satellite bands of specific wavelength regions. Values of image indices can range from -1 - +1 (normalized difference indices), to arbitrary scales for other ratio-based indices. See <a href="https://www.usgs.gov/core-science-systems/nli/landsat/landsat-surface-reflectance-derived-spectral-indices?qt-science_support_page_related_con=0#qt-science_support_page_related_con">this link</a> for a good introduction to indices that can be obtained using Landsat data.

- Some commonly used RS indices include
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
  
  
- The Table below provides reflectances used to calculate the above indices. 


<p align="center">
<img src="https://user-images.githubusercontent.com/87503837/142231637-77253803-79a2-4f34-939a-f8d234d796bb.png" height="50%" width="50%">
</p>


:pushpin: A database of remote sensing indices and their respective sensors and areas of application are compiled [here](https://www.indexdatabase.de/). 

## 5. A Recap Video
<p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/fdf9ea02f3f247969e0a56bd8a1909411d" target="_blank">
    <img src="https://user-images.githubusercontent.com/85199074/200466106-3a918af2-601f-4d38-867e-6cdf50bd79f7.png" alt= "GEE Tutorial" width="800">
  </a>
</p>

**Recap ‘search_and_display’ and ‘image_indices_environmental_data’**

- Define a **geometry of interest**

- **ST_DATE and EN_DATE** give time range 

- **IMG_L#** give image collection 

- **filterBounds** filters by area of interest 

- **filterDate** filters by time range 

- **filterMetadata(‘CLOUD_COVER’)** filters cloudy images out 

- **visParams** provides visualization parameters to determine the color display of the output image 

- **Map.centerObject** centers the focus of the map on the area of interest 

- **Map.addLayer** adds an image or image collection to the map 

Functions of getLSAT, cloudMask, getNDVI are defined with input and filters 

- **getLSAT** has inputs of a Landsat image collection, geometry, start date, and end date. It retrieves the Landsat image collection and filters it by geometry, time range and cloud cover. The cloud cover is filtered through a cloud mask. Band names of the images in the collection are selected and renamed to be clearer, and Landsat 8 images have a different order of band names since its bands differ slightly from 5 and 7. 

- **cloudMask** has an input of an image and is used in get LSAT and extracts quality bits and ensures that cloudy data is removed from the image collection 

- **getNDVI** has an input of an image and selects NIR and Red bands from the image given. It then calculates the normalized difference of these values and returns an image with NDVI 

In the main part of the code, and **Landsat image (IMG_LT)** is created and the **median image extracted (MED_LT)**. Then an index (e.g., NDVI) is selected from the **image collection (IMG_IND)**, and the **median image of the index collection is extracted (MED_IND)**. These images are mapped, and a chart is created to show the index over time. This process can be conducted on NDVI, elevation, or land surface temperature 

## 6. Assignment Submission and Help

The participants will have to sign into their GitHub accounts to submit assignments. Below is a video explaining how to submit the module assignments and how to request help through GitHub. Note: It may be convenient to open videos in the workshop in a new tab or window to easily navigate the GitHub page.


<p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/9741afe237094a77aff3acbf6c2df8a91d" target="_blank">
    <img src="https://user-images.githubusercontent.com/84922404/139679866-11650dd6-855f-4420-82c1-fa0f4071ee37.png" alt= "GEE Tutorial" width="800">
  </a>
</p>


## 7. Pre-Workshop Exercise

- Please complete the [[Exercise 0]](https://github.com/ecodynlab/GALUP/blob/main/ExercisesM2/Exercise0.md)

- Please submit your exercise [[here]](https://github.com/SERVIR-WA/GALUP/issues/new?assignees=Achidago&labels=Exercise+W4M0&template=Exercise0Template.md&title=Workshop+4+exercise+0+%5Breplace+with+your+name%5D)

## 8. What's Next?

Module 1 - [Time Series Analysis](module1.md)
Module 2 - [Change Detection](module2.md)

## 9. Other Resources

Kindly refer to Workshop 2 - [Introduction to Satelite Remote Senisng I](https://servir-wa.github.io/GALUP/html/Training2ReadMe.html)

