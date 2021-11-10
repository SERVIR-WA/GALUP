# Module-2 Exercise
## Description
In this exercise, we will cover Landsat dataset visualization using GEE.

## Skills Developed
* Understand how to import and filter RS products in GEE
* Create a visual map using specific bands
* Identify satellite differences over various years and regions

## Instructions
1. In the GEE [code editor](https://code.earthengine.google.com/), copy and paste the script for this exercise, ["01_search_and_display"](https://github.com/SERVIR-WA/GALUP/wiki/Scripts). This video may be useful for following along with this exercise.

<p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/9d0bd66164844d478357dbb876e9a8b91d" target="_blank" rel="noopener">
    <img src="https://user-images.githubusercontent.com/84922404/141026786-f85ea3c1-1241-44f7-8edd-3b243ffac099.png" alt= "GEE Tutorial" width="800">
  </a>
</p>

2. Using the geometry tools (*#14 from the Figure in Module-2*), identify a region of interest that is roughly the size of a district, and draw a polygon around it following the procedure given in the video above. This will be automatically imported into the code editor, modifying the existing script. <br/>

:pushpin: Note that if the region chosen is too large, the image may not be exported unless the maximum number of pixels is altered.
    
3. Choose start and end dates over which satellite data will be collected using the format 'YYYY-MM-DD':

    a. Enter start and end dates about 3 months apart during the summer months (e.g. May through August).
  
    b. Using the script as a guide, map the Landsat images using your chosen region and dates of interest.<br/>
    :pushpin: Tip: If no image appears, it is likely due to cloud cover. Changing the region of interest or the cloud cover percentage (e.g. from ```filterMetadata('CLOUD_COVER','less_than',70)``` to ```filterMetadata('CLOUD_COVER','less_than',90)```).
  
    c. Take a screenshot of the image displayed in the GEE map. 
  
4. Repeat the process of 3(a-c) with a set of dates during the winter months (e.g. December to March). 
5. Download this document [template](https://github.com/SERVIR-WA/GALUP/files/7508860/WS2_M2E2_Submission.docx) and add screenshots of your two mapped images (summer and winter) as well as the answers to the follwing questions: 

    a. What is the primary land cover in your chosen area based upon Google maps and/or your knowledge of the area)? What are the changes in land cover change across the year/seasons?
    
    b. Do you notice any differences in the appearance of the images taken from the summer months and those from the winter months? If so, what could be causing these differences in your chosen area? <br/>
    
    :pushpin: Note: Think about the cropping patterns, pre- or post- rain greenness etc.
    
    c. Run the script again after changing the cloud cover fraction filtered in GEE to 30% instead of the current value of 70% (```.filterMetadata('CLOUD_COVER','less_than',70)```). Do you see any changes in the final output? If so, take a screen shot of the new image and include it in the document as well. What could be causing the changes in your chosen area? Did you notice a difference in the number of the images retrieved?
    
6. Once completed, submit the document <a href="https://github.com/SERVIR-WA/GALUP/issues/new?assignees=&labels=exercise+w2m2&template=w2m1-exercise-submission.md&title=Module+2+exercises+%5Breplace+with+your+name%5D" title="here">here</a>\. Please submit the Post-Module-2 survey [here](https://ufl.qualtrics.com/jfe/form/SV_6fIRnsK59HEwZ9k).


## Result
* Upon completion of the exercise, your screenshot should look similar to the file [here](https://github.com/SERVIR-WA/GALUP/blob/master/training/2_rs/Exercises/M2_E1_sample.md).


