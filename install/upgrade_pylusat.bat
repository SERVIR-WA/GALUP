@echo off
rem Ask user to provide the path to QGIS root folder
set "QGIS_ROOT=C:\Program Files\QGIS 3.10"
set PATH=%QGIS_ROOT%\bin;%PATH%
set PATH=%PATH%;%QGIS_ROOT%\apps\qgis\bin

@echo off
call "%QGIS_ROOT%\bin\o4w_env.bat"
call "%QGIS_ROOT%\bin\qt5_env.bat"
call "%QGIS_ROOT%\bin\py3_env.bat"

@echo off
path %QGIS_ROOT%\apps\qgis\bin;%PATH%

set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES
rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%

cd /d %~dp0

python -m pip install --upgrade pip
python -m pip install --upgrade pylusat
PAUSE