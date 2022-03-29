# Module-4 Exercise 1
## Description
In this exercise, we will use the index extraction covered in the last module to perform land cover classification in GEE.
## Skills Developed
- Understand how to collaboratively collect 'ground truth' data,
- Use ground truth data with different classification methods to generate land cover maps,
- Use GEE scripts to derive simple metrics of classification accuracy, 
- Download classified maps for your area.

## Instructions
📌 This process may be made easier by downloading and installing Google Eath Pro (<a href="https://www.google.com/earth/versions/#earth-pro">link</a>). <br>
This video may help in completing steps 1 through 5:

 <p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/38ea2eb245184e9d8bab2a4c6fc28ed31d" target="_blank" rel="noopener">
    <img src="https://user-images.githubusercontent.com/84922404/142556118-d1429e06-8332-44c5-bc2e-9baa7b4f87af.png" alt= "GEE Tutorial" width="800">
  </a>
</p>


1. Download these **KML files** that contain boxes assigned to your organization: <br>
    a. [AGRHYMET KML](https://github.com/ecodynlab/GALUP/files/7565808/BOXES_AGRHYMET.zip) <br>
    b. [CERSGIS KML](https://github.com/ecodynlab/GALUP/files/7565809/BOXES_CERSGIS.zip) <br>
    c. [ICRISAT KML](https://github.com/ecodynlab/GALUP/files/7565810/BOXES_ICRISAT.zip) <br>
    b. [LUSPA KML](https://github.com/ecodynlab/GALUP/files/7565811/BOXES_LUSPA.zip) <br>
2. Opening these files in Google Earth Pro will zoom to the entire country. Expand the dropdown list to reveal individual boxes. Double-clicking on the boxes should make Google Earth Pro zoom into that location.
3. 	~~Access this Google Spreadsheet~~.
4. Each organization has a tab assigned to it. The ID column corresponds to the ID of the boxes in the KML (do not change the ID). We have asumed each registered participant should be able to classify at least 100 locations by the end of the exercise, 
5. Double-click on any box in the KML to zoom to that location. On the spreadsheet, locate the row corresponding to the KML box ID and click on the "Landcover" cell to reveal several options. Click on an option to select the landcover class. Clicking on this cell will result in several options appearing in the "Subclass cell". These are details of the landcover you selected. Select an option if you are sure the land cover class can be better defined using one of the subclasses.
6. Once the sheet has been filled and the classification of each point completed, we will export the collected data and merge it with the coordinates of the random points.

**The classifications on the spreadsheet must be completed by Monday, 11/22 at 1:00 PM GMT**

7. Once you receive the merged files of the classifications and original random points (this will be in the form of a shapefile), download these files. The files will be available here on **Tuesday, 11/23**: one with the 7 main classes, and one with the 25 subclasses. Please click [here](https://github.com/SERVIR-WA/GALUP/files/7620440/GALUP_Classification_Updated2_Main.zip) to download the zipfile containing the shapefile of the 7 main classifications, and please click [here](https://github.com/SERVIR-WA/GALUP/files/7620443/GALUP_Classification_Updated2_Subclasses.zip) to download the zipfile containing the shapefile of the 25 subclasses.
8. Upload each zipfile into GEE as an asset (see this [link](https://developers.google.com/earth-engine/guides/asset_manager) for help with managing assets in GEE). The video below may also help with this and following steps. 

 <p align="center">
  <a href="https://mediasite.video.ufl.edu/Mediasite/Play/34f2887653d94667900f5eb240f954691d" target="_blank" rel="noopener">
    <img src="https://user-images.githubusercontent.com/84922404/143688697-041adf9f-3c25-4857-ad58-ced83aa2fc7c.png" alt= "GEE Tutorial" width="800">
  </a>
</p>


9. Once the assets have been loaded into GEE, run the script: [03_Landcover_Classification](https://github.com/SERVIR-WA/GALUP/wiki/Scripts#03_landcover_classification). This will utilize the training data (the asset) to classify Ghana's land cover using the Random Forest classification method. <br>
📌 Note that the different zipfiles will have different labels for the classifications. The main classification file will use the label 'LCODE' to represent the classes, while the subclass file will use 'LCODE2'. The visualization parameters will also be different for each of these class levels. <br>
10. Repeat step 6 using each of the three other classifiers (minimumDistance, libsvm, and smileCart), and choose the classifier that you think best represents the land cover of the region. Take a screenshot of the land cover classification map that results from using this classifier.
11. Download this [template](https://github.com/SERVIR-WA/GALUP/files/7572994/WS2_M4E1_Template.docx) and add the screenshot as well as answer the following questions:
    a. What land cover classification method did you choose to use (minimumDistance, libsvm, smileCart, or smileRandomForest)? Why did you choose this classifier and how does it compare to classifications from the other methods?
12. Once completed, submit the document [here](https://github.com/SERVIR-WA/GALUP/issues/new?assignees=&labels=exercise+w2m4&template=w2m4-exercise-submission.md&title=Module+4+exercises+%5Breplace+with+your+name%5D). Please submit the Post-Module-4 survey here.
