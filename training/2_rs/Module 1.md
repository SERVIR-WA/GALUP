## Module 1 - Introduction to Remote Sensing 

What will you learn from this module?

• Basics of EM spectrum

• Different types of remote sensing systems and sensors and their applications 

## 
_Remote sensing is the science and art of obtaining information about an object, area, or phenomenon through the analysis of data acquired by a device that is not in contact with the object, area, or phenomenon under investigation<sup>1</sup>._

Modern day remote sensing started with the advent of radar, sonar, and thermal infrared detection systems during WWII. Since then, detectors have been expanded to  run on most of the EM spectrum and variety of applications spanning from military use to agriculture. 

### 1. EM spectrum 
• **Electromagnetic spectrum** is the entire distribution of electromagnetic radiation according to frequency or wavelength. 

• **Observed energy** or **radiation** is primarily sensitive to molecular resonances in the to molecular resonances in the surface layer surface layer of target. 

• **Emitted**, **reflected**, and **backscattered radiation** is sensitive to temperature distribution, geometric, and electric properties of surface or volume. 

•**Near infrared (NIR)** is defined from 750 nm to 1400 nm and **shortwave infrared (SWIR)** from 1400 nm to 3000 nm.


<p align="center">
<img width="604" height="207" src="https://user-images.githubusercontent.com/87503837/132062813-8bd2faa0-336c-4fc7-b3f1-f8ae62822e9b.png">
</p>

The human eye is only able to detect wavelengths in the visible light range. However, many insects see in the 300 to 650 nm wavelength and can detect ultraviolet light because   they have special photoreceptors in their eyes.   


<br/>

| Band                         | Wavelength           |
|------------------------------|----------------------|
|     Blue                     |     0.45-0.51µm      |
|     Green                    |     0.53-0.59µm      |
|     Red                      |     0.64-0.67µm      |
|     Near Infrared            |     0.75-1µm         |
|     Short-wave infrared 1    |     1-1.6µm          |
|     Short-wave infrared 2    |     1.6-2.5µm        |
|     Thermal Infrared         |     10.60–12.51µm    |

<br/>

**1.1 Hyperspectral**

![image](https://user-images.githubusercontent.com/87503837/130195843-a8aea0e9-def9-40c4-80ce-b562fd56e918.png)

</p>

### 2. Remote sensing systems and sensors
**2.1 Sensors:** 

• **Active sensors** consist of a transmitter and a receiver that may (monostatic system) or may not be (bistatic system) co-located. It transmits a known signal at a particular wavelength and receives some portion of the signal in the direction of a receiver. In case of a monostatic system, the received signal is called “backscatter”. Examples include a camera with the flash, Light Detection and Ranging (LIDAR), Synthetic aperture radar (SAR). 

• **Passive Sensors** consist of receiver that receives naturally occurring EM energy from a target at a particular wavelength and direction. Examples include a camera without the flash and radiometers.

<br/>

<!--- 
**Types of Detectors:** 

**Thermal detectors**

• absorb incident flux and undergo temperature changes

• the power in absorbed radiation is typically small, and so the detector itself should be small to have a low heat capacity

• Ex: Bolometer 

![image](https://user-images.githubusercontent.com/87503837/133616355-0ff8f5fd-2d57-4e97-b781-786353fa934e.png)

**External Photo-effect detectors**

• has photocathode where incident light is partially absorbed and generates photoelectrons

• Ex: Photomultiplier Tube (PMT)


<img src="https://user-images.githubusercontent.com/87503837/133625438-5593a350-5cd9-414a-bd1e-24f23e051fc4.png" width="500" height="320">

**Internal Photo-effect detectors**

• semiconductors in which the electons undergo internal energy level transitions when they absorb an electron

• consists of **photoconductive detectors** and **photovoltaic detectors**

• Ex: 

<img align="center" src="https://user-images.githubusercontent.com/87503837/133616643-ba9e4e28-2811-4d02-bc5a-987a549af606.png" width="350" height="320">

-->

**2.2 Resolution:**

• **Spatial resolution** describes how far apart two targets have to be so that they are detected as separate signals.

• **Temporal resolution** describes how often a sensor observes the same target 

• **Radiometric resolution** describes the number of wavelengths observed. For example, multispectral sensors observe about 10s of bands (or wavelength regions) in the VI/NIR spectrum, providing discrete observations. 


Spectral sampling: Multispectral sensors and Hyperspectral sensors

<img src="https://user-images.githubusercontent.com/87503837/133636464-24493df3-1c5d-405f-b7ec-10fe64cec5e7.png" width="400" height="220"> <img src="https://user-images.githubusercontent.com/87503837/133636485-93336e1a-214b-4897-b1ca-c1206879b4e1.png" width="400" height="220">



<br/>

**2.3 Satellite Systems**

•	**Geo-stationary/geo-synchronous** : at about 36,000km above the earth's surface and follows direction of Earth's rotation 

•	**Polar orbiting**: circle the Earth in an almost north-south orbit, passing close to both poles

•	**Neither**: Tropical Rainfall Mapping Mission (TRMM) 

<br/>

**Data Sources**

A table of the bands from the Landsat satellite program are given below, with the differences between Landsat 5, 7, and 8 outlined. General uses for these bands are supplied, such as Land Use/Land Cover (LULC) and Land Surface Temperature (LST).


<p align="center">
<img src="https://user-images.githubusercontent.com/84922404/134026792-d1f488cd-3630-4266-ad2f-ed7062e52982.png" width="500" height="600">
</p>

For further information on remote sensing, this [video](https://www.youtube.com/watch?v=qiqUAlJK4vI) from NASA ARSET is a useful resource.

(M.U. Liaqat (February, 2016))

</p> 

### 2.4 Practice 

1. Download [Module 1 Practice](https://github.com/ecodynlab/GALUP/files/7390297/MODULE.1.zip) and unzip the file. 
2. Open the unzipped file in QGIS. 
3. Switch between the two layers to see the difference between the two types of remote sensing data. 
4. The file consists of NDVI and land surface temperature data. NDVI is a vegetation index that will be covered in another section.  

##

**Next Section**: 

<a href="Module 2.md" title="Module 2">Module 2</a>



