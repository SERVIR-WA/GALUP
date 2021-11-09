# Module 2 Exercise 1 
## Description
In this exercise, we will cover satellite dataset visualization using GEE.

## Skills Practices
* Understand how to import and filter a dataset in GEE
* Create a visual map using specific bands
* Identify satellite differences over various years and regions


## Instruction
1. In the GEE [code editor](https://code.earthengine.google.com/), copy and paste the script for this exercise, ["01_search_and_display"](https://github.com/ecodynlab/GALUP/wiki/Scripts).

This video from the Module 2 example may be useful for following along with this exercise.
<p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/68693a462a914666807e47f992dedde11d" target="_blank" rel="noopener">
    <img src="https://user-images.githubusercontent.com/84922404/140551115-a0e9d6fa-ae4b-4357-99be-0a27b1901394.png" alt= "GEE Tutorial" width="800">
  </a>
</p>

2. Using the geometry tools (14.), identify a region of interest (roughly the size of a district) and draw a polygon around it following the procedure given in the video. This will be automatically imported into the code editor, modifying the existing script. 

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i. Note that if the region is too large, the image won't be able to be exported unless the maximum number of pixels is altered.
    
3. Choose dates over which satellite data will be collected in the format 'YYYY-MM-DD':

    a. Enter a set of dates during the summer months (May through August), and set the start and end dates about 3 months apart.
  
    b. Using the script as a guide, map the satellite images using your chosen region and dates of interest.
  
    c. Take a screenshot of the image displayed in the GEE map. 
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i. Tip: if no images appear, this is likely due to cloud cover. Try changing the region of interest or the cloud cover percentage (e.g. ```filterMetadata('CLOUD_COVER','less_than',70)``` to ```filterMetadata('CLOUD_COVER','less_than',90)```).
  
4. Repeat the process of 3(a-c) with a set of dates during the winter months (December to March). 
5. Questions: 

    a. What is the primary land cover in your chosen area (based upon Google maps and your knowledge of the area)? What are the changes in land cover change across the year/seasons?
    
    b. Do you notice any differences in the appearance of the images taken from the summer months and those from the winter months? If so, what could be causing these differences in your chosen area?
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i. Note: think about the cropping patterns, pre- or post- rain greenness etc.
    
    c. Run the script again after changing the cloud cover fraction filtered in GEE to 30% instead of the current value of 70% (.filterMetadata('CLOUD_COVER','less_than',70)) and run the script again. Do you see any changes in the final output? If so, what could be causing the changes in your chosen area? Did you notice a difference in the number of the images retrieved?
    
    
6.  Download this document [template](https://github.com/ecodynlab/GALUP/files/7487735/WS2_M2E2_Submission.docx) and add screenshots of your two mapped images (summer and winter) as well as the answers to questions 5a through 5c to it. Once completed, submit the document <a href="https://github.com/ecodynlab/GALUP/issues/new?assignees=&labels=Exercises&template=assignment-submission.md&title=Add+your+name+and+the+module+number+for+submission" title="here">here</a>\.


## Result
* Upon completion of the exercise, your screenshot should look similar to the file [here](https://github.com/ecodynlab/GALUP/blob/main/Exercises/M2_E1_sample.md).

</p>

Return to [Module 2](https://github.com/ecodynlab/GALUP/blob/main/Modules/Module%202.md) or move on to [Module 3](https://github.com/ecodynlab/GALUP/blob/main/Modules/Module%203.md).
