.. role:: raw-html-m2r(raw)
   :format: html


Module 2 - Remote Sensing Applications using Google Earth Engine
================================================================

**What will you learn from this module?**


* Set up Google Earth Engine (GEE)
* Familiarize with GEE Interface
* Download and visualize RS data using Code Editor in GEE 

1. Setting up GEE
-----------------

Please request an account with Google Earth Engine (GEE) as follows:


* Go to the GEE webpage `here <https://earthengine.google.com/>`_
* Select “Sign Up” at the top right of the page and input institution and intention for use (e.g. using remote sensing datasets for land use suitability modeling).

:pushpin: Approval may not happen immediately, so please be sure to sign up in advance of the workshop to provide a few days for completion.

2. Exploring GEE Interface
--------------------------

The video and Figure below show general interface functions for GEE. Further description of the components of the Figure can be found `here <https://github.com/SERVIR-WA/GALUP/wiki/GEE-Interface>`_. 


.. raw:: html

   <p align="center">
     <a href="https://mediasite.video.ufl.edu/Mediasite/Play/55447fcbfc2f487ebaae8d1258e829ca1d" target="_blank">
       <img src="https://user-images.githubusercontent.com/84922404/135470199-719878b5-7cb6-4a7a-aacd-e40881cda2e3.JPG" alt= "GEE Tutorial" width="800">
     </a>
   </p>



.. image:: https://user-images.githubusercontent.com/84922404/132246323-4b2d7dee-6cdc-4828-aa9a-b3ab4193ffa5.png
   :target: https://user-images.githubusercontent.com/84922404/132246323-4b2d7dee-6cdc-4828-aa9a-b3ab4193ffa5.png
   :alt: GEEinterface


:pushpin: In this workshop, we will be programming in the GEE `code editor <https://code.earthengine.google.com/>`_ that uses the JavaScript language. There are extra `resources <https://developers.google.com/earth-engine/tutorials/tutorial_api_01>`_ available from Google to introduce the JavaScript Application Programming Interface (API).

3. Using GEE to Explore RS Concepts from Module-1
-------------------------------------------------

3.1 Downloading and Visualizing Landsat Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following example, we will use GEE to download and visualize Landsat satellite data in Ghana. Please use the video tutorial in Section 3.2 to follow along.


.. raw:: html

   <ul>
     <li>Copy the script <a href="https://github.com/SERVIR-WA/GALUP/wiki/Scripts">"01_search_and_display"</a> and paste into the GEE <a href="https://code.earthengine.google.com/">code editor</a>. This is the same script that will be used in Exercise with slight alterations necessary to complete the Exercise.</li>
     <li>The script includes:
       <ol type="a">
       <li>Defining variables for dates of interest: <b>ST_DATE</b> and <b>EN_DATE</b></li>
       <li>Defining the region of interest using 4 coordinates: <b>Longitude_min</b>, <b>Latitude_min</b>, <b>Longitude_max</b>, <b>Latitude_max</b></li>
       <li>Defining variables for RS data products: Here, data products from <b>Landsat 5, 7, and 8</b> are used.</li>
       <li>Selecting the data product: <b>Landsat 5</b>.</li>
       <li>Filtering the data product by the region and dates of interest, and by the amount of cloud cover.</li>
       <li>Repeating <i>d</i> and <i>e</i> with <b>Landsat 7 & 8</b>.</li>
       <li>Setting the visualization parameters for each product: <b>bands</b>, <b>min</b>, <b>max</b>, <b>gamma</b>.</li>
       <blockquote>
       For information on Landsat bands, please refer to <a href="https://github.com/SERVIR-WA/GALUP/blob/master/training/2_rs/module1.md">Module 1</a>. <br>
       The parameters <b>min</b>, <b>max</b>, and <b>gamma</b> describe the RGB visual representation. For more details on these, see <a href="https://developers.google.com/earth-engine/guides/image_visualization">here</a>.
       </blockquote>
       <li>Mapping the images: Centering, and adding RS data in three layers.</li>
       <li>Exporting images to Google Drive.</li>
       </ol>
     </li>
   </ul>


3.2 Video Tutorial for the Section 3.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the video tutorial to follow along with the example. This may also be useful in completing the exercise.


.. raw:: html

   <p align="center">
     <a href="https://mediasite.video.ufl.edu/Mediasite/Play/68693a462a914666807e47f992dedde11d" target="_blank" rel="noopener">
       <img src="https://user-images.githubusercontent.com/84922404/140551115-a0e9d6fa-ae4b-4357-99be-0a27b1901394.png" alt= "GEE Tutorial" width="800">
     </a>
   </p>


Exercise and Post-Module Survey (required)
------------------------------------------


#. Please complete and submit `Exercise <https://github.com/SERVIR-WA/GALUP/blob/master/training/2_rs/Exercises/M2_exercise1.md>`_ for Module 2.
#. Submit the Post-Module `survey <https://ufl.qualtrics.com/jfe/form/SV_6fIRnsK59HEwZ9k>`_. 

</p>

#
=

**Previous Section:**\ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; **Next Section:**

:raw-html-m2r:`<a href="module1.md" title="Module 1">Module 1</a>` &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :raw-html-m2r:`<a href="module3.md" title="Module 3">Module 3</a>`
