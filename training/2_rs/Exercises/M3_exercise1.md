# Module-3 Exercise 1
## Description
In this exercise, we will build upon module 1 by extracting Landsat imagery, deriving image indices, and visualizing temporal changes in indices and other environmental variables.

## Skills Developed
- Understand how image indices are derived,
- Use graphing techniques available in GEE to perform spatial and temporal analysis of indices, 
- Search, extract, and plot other environmental data from the GEE data repository.

## Instructions
1. In the GEE [code editor](https://code.earthengine.google.com/), copy and paste the script for this exercise, ["02_image_indices_environmental_data"](https://github.com/SERVIR-WA/GALUP/wiki/Scripts#02_image_indices_environmental_data). This video, also included on the Module 3 page, may be useful for following along with this exercise. <br>
 <p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/bfe5811813c04582a51f02f636dc31161d" target="_blank" rel="noopener">
    <img src="https://user-images.githubusercontent.com/84922404/142096329-b1cb29c6-411a-42d9-905c-20ec80f899b2.png" alt= "GEE Tutorial" width="800">
  </a>
</p>

2. Adjust the variables "YEAR1", "YEAR2","ST_DATE", and "END_DATE" to indicate a time period of interest.
3. Choose a region of interest by either drawing a polygon to automatically import a geometry or by manually specifying the Longitue_Min, Latitude_Min, LongitudeMax, and LatitudeMax as coordinates of a rectangle.
4. Alter the given function: <br> ```var getNDVI = function(image){``` <br>
  ```var ind = image.expression('(nir-red)/(nir+red)',{'nir':image.select('nir'),'red':image.select('red')}``` <br>
  ```var ret = ind.copyProperties({source: image,properties: ['system:time_start']});``` <br>
  ```return ret;``` <br>
  ```};``` <br> 
  to represent another chosen variable <br>
 :pushpin: Some common indices are given at the bottom of the script. <br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i. If you change the variable name "getNDVI" (e.g. to "getSAVI") (this is good coding practice), ensure that the rest of the code &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; that utilizes the "getNDVI" function is also changed.
5. Run the script over the chosen region and time period, and take screenshots of: <br>
    a. The raw Landsat image <br>
    b. The image of the chosen index <br>
    c. The SRTM elevation image <br>
    d. The LST image <br>
    e. The time series chart for the chosen index <br>
    f. The time series chart for LST <br>
  :pushpin: Check and Uncheck the layers in the GEE map to be able to see each image individually. 
5. Download this document [template](https://github.com/ecodynlab/GALUP/files/7550880/WS2_M3E1_Template.docx) and add the 6 screenshots stated above, as well as the answers to the follwing questions:<br>
    a. What does your chosen index represent? Do you notice any distinct patterns in values of the chosen index over the course of the chosen time period? <br>
    b. What do you notice about the images that represent each different layer (Landsat, index, SRTM elevation, and LST)? Can you infer any information about the chosen region through these images? <br>
5. Once completed, submit the document <a href="https://github.com/ecodyn/GALUP/issues/new?assignees=&labels=exercise+w2m2&template=w2m2-exercise-submission.md&title=Module+2+exercises+%5Breplace+with+your+name%5D" title="here">here</a>\. Please submit the Post-Module-3 survey [here](https://ufl.qualtrics.com/jfe/form/SV_bpjF7THHLlhtWCO).
## Result
Upon completion of the exercise, your map should look something like the image [here](https://github.com/ecodynlab/GALUP/blob/main/Exercises/M3_E1_sample.md).
