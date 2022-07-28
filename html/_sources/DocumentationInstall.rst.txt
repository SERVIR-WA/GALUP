.. role:: raw-html-m2r(raw)
   :format: html


Software Installation and Setup
===============================

System Requirements
-------------------


* *Operating system*\ : 32-bit or 64-bit version of
  `Windows&reg; <https://tinyurl.com/4jcaub97>`_.
* *Recommended Windows edition*\ : Windows 7, Windows 10.
* *Recommended memory size*\ : **8 GB** of `RAM <https://tinyurl.com/7s53ea9k>`_.
* *System permission*\ : **Administrator Privilege** is needed to install QGIS.

..

   :pushpin: **QGIS 3.10.8 is a MUST**\ :raw-html-m2r:`<br>`
   To successfully load the *Processing Algorithms* that the **GALUP** team
   developed, the QGIS **3.10.8** version is particularly **REQUIRED**. To avoid
   any potential conflicts, please first
   `perform an uninstallation <https://tinyurl.com/2bech66a>`_
   before moving forward on this instruction, if *another version* of QGIS is
   installed on your computer.


Installation Steps
------------------


#. `Install QGIS 3.10.8 <https://tinyurl.com/kwxcn6wd>`_
#. `Install PyLUSAT <https://tinyurl.com/27f4aepa>`_
#. `Load Processing Algorithms in QGIS <https://tinyurl.com/e6r2n7tm>`_

1. Install QGIS 3.10.8
^^^^^^^^^^^^^^^^^^^^^^


#. Go to `https://qgis.org/en/site/ <https://qgis.org/en/site/>`_.\ :raw-html-m2r:`<br>`\ :raw-html-m2r:`<br>`
   ..

      :bulb: **A tip for viewing external links**\ :raw-html-m2r:`<br>`
      By default, clicking on a link in this page will open the link from the
      *current tab* in the *current window* of the web browser,
      to :raw-html-m2r:`<ins>open a link in a **new tab**</ins>`\ , press and hold :raw-html-m2r:`<kbd>Ctrl</kbd>`
      while clicking; to :raw-html-m2r:`<ins>open a link in a **new window**</ins>`\ ,
      press and hold :raw-html-m2r:`<kbd>Shift</kbd>` while clicking.


#. Click  **\ `Download Now <https://qgis.org/en/site/forusers/download.html>`_\ **.
#. Go to **ALL RELEASES** where you can download
   **\ *Previous releases of QGIS are still available*\ **
   **\ *\ `here <https://qgis.org/downloads/>`_\ *\ **.
#. Download ``QGIS-OSGeo4W-3.10.8-1-Setup-x86_64.exe``\ , if you are using 64-bit
   system, or download ``QGIS-OSGeo4W-3.10.8-1-Setup-x86.exe``\ , if you are using
   32-bit system.
#. Double-click the downloaded installation file and follow the installation
   instruction to install **QGIS 3.10.8** on your computer.


.. raw:: html

   <h3> 2. Install <a url="https://pypi.org/project/pylusat/">PyLUSAT</a>:
   Python for Land-Use Suitability Analysis Tools</h3>


..

   :warning: **Is Internet connected?**\ :raw-html-m2r:`<br>`
   Internet connection is required throughout the installation process.



#. Go to `https://github.com/SERVIR-WA/GALUP <https://github.com/SERVIR-WA/GALUP>`_.
#. Click **Code**\ , and then click **Download ZIP** to download the *GALUP*
   repository (see image below).\ :raw-html-m2r:`<br>`

   .. image:: images/download_repo.gif
      :target: images/download_repo.gif
      :alt: github home

#. **Unzip** the downloaded ``GALUP-master.zip``.
#. Open ``GALUP-master -> install -> QGIS 3.10.8``.
#. Locate the folder that matches your operating system:

   .. raw:: html

      <ol type="a">
         <li>for <b>32-bit</b>: Copy <code>pylusat 32-bit</code>
         (<ins>entire folder</ins>) and paste to
         <code>C:\Program Files (x86)\QGIS 3.10</code>.</li>
         <li>for <b>64-bit</b>: Copy <code>pylusat 64-bit</code>
         (<ins>entire folder</ins>) and paste to
         <code>C:\Program Files\QGIS 3.10</code>.</li>
      </ol>


#. Open the copied folder (not the old one) and **Right Click**
   ``install_pylusat.bat`` to
   :raw-html-m2r:`<img src="images/admin.png" alt="admin" width="12">` *Run as administrator*.
#. A pop-up window will ask you two questions (animation below is for 32-bit):

   .. raw:: html

      <ol type="a">
         <li><b>Specify the root folder of QGIS</b>: Type or paste the same path
         as above, i.e., <code>C:\Program Files (x86)\QGIS 3.10</code> for 32-bit,
         or <code>C:\Program Files\QGIS 3.10</code> for 64-bit.</li>
         <li><b>Is the QGIS a long term release [Y/N]</b>: We indeed installed a
         "long term release" of QGIS, so type <b>Y</b> (case insensitive).</li>
      </ol>


#. Press **Enter** key and wait for the installation to complete.\ :raw-html-m2r:`<br>`

   .. image:: images/batch_window.gif
      :target: images/batch_window.gif
      :alt: batch_window

3. Load the *Processing Algorithms*\ : LUCIS-OPEN Tools for QGIS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. Open **QGIS Desktop 3.10.8** program from **Start Menu**.
#. Check out this *Processing* `\ *link* <https://tinyurl.com/25xc4rjd>`_
   to make sure **\ *Processing*\ **\ , a `Core Plugin <https://tinyurl.com/5r5xk5ua>`_
   of QGIS, is **activated**.\ :raw-html-m2r:`<br>` :raw-html-m2r:`<br>`
   ..

      :bulb: **Plugins are at the core of QGIS**\ :raw-html-m2r:`<br>`
      QGIS has been designed with a plugin architecture. This allows many new
      features and functions to be easily added to the application. Some of the
      features in QGIS are actually implemented as
      `plugins <https://tinyurl.com/h8ayxjyt>`_.


#. Open `Processing Toolbox <https://tinyurl.com/h9fpxw7p>`_ on the **Menu bar**
   or Press :raw-html-m2r:`<kbd>Ctrl</kbd>`\ +\ :raw-html-m2r:`<kbd>Alt</kbd>`\ +\ :raw-html-m2r:`<kbd>t</kbd>`.
#. Click *Add Script to Toolbox* (see the animation below).
#. Locate the *algorithms* folder within the ``GALUP-master`` folder you
   downloaded from GitHub.
#. Select all the ``*.py`` files and click **Open**.
#. Now you can find all `Processing Algorithms <https://tinyurl.com/scnmtabd>`_
   developed by **GALUP** under the `Scripts <https://tinyurl.com/wcxh8ahe>`_
   dropdown menu.\ :raw-html-m2r:`<br>`

   .. image:: images/qgis_load_tools.gif
      :target: images/qgis_load_tools.gif
      :alt: load_tools
