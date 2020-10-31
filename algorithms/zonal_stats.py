import sys
import os
from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterString,
                       QgsProcessingParameterVectorDestination)
from pylusat import zonal


class ZonalStats(QgsProcessingAlgorithm):
    INPUT = 'INPUT'
    RASTER = 'RASTER'
    STATS = 'STATS'
    NODATA = 'NODATA'
    OUTPUT = 'ZonalStats'

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)

    def group(self):
        return self.tr('LUCIS-OPEN Tools for QGIS')

    def groupId(self):
        return 'lucisopen'

    def name(self):
        return 'zonalstats'

    def displayName(self):
        return self.tr('Zonal Statistics')

    def shortHelpString(self):
        return self.tr(
            """Compute specified statistics for each zonal feature.\n
            Compute various types of statistics of the values in the raster 
            layer using the input layer's geometries as boundaries.\n
            The types of stats defaults to ['count', 'min', 'max', 'mean'].\n 
            Other valid stats are ['sum', 'std', 'median', 'majority', 
            'minority', 'unique', 'range', 'nodata', 'nan'].
            """.strip()
        )

    def createInstance(self):
        return ZonalStats()

    def __init__(self):
        super().__init__()

    def initAlgorithm(self, configuration={}):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                types=[QgsProcessing.TypeVectorPolygon]
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.RASTER,
                self.tr('Raster layer'),
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.STATS,
                self.tr('Types of statistics (separated by space)')
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                self.NODATA,
                self.tr('No data value'),
                type=QgsProcessingParameterNumber.Integer,
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT,
                self.tr('Output layer'),
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        input_lyr = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        raster_lyr = self.parameterAsRasterLayer(parameters, self.RASTER, context)
        stats = self.parameterAsString(parameters, self.STATS, context)
        nodata = parameters[self.NODATA]
        output_file = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from .loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        raster_path = raster_lyr.dataProvider().dataSourceUri()

        output = zonal.zonal_stats_raster(input_gdf, raster_path, stats, nodata)
        output.to_file(output_file)
        return {self.OUTPUT: output_file}
