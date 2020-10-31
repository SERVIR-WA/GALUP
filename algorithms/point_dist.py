import sys
import os
from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterString,
                       QgsProcessingParameterEnum)
from pylusat import distance


class PointDistance(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    POINT = "POINT"
    METHOD = "METHOD"
    DATA_TYPE = "DATA_TYPE"
    OUTPUT_COLUMN = 'OUTPUT_COLUMN'
    OUTPUT = "OUTPUT"

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)

    def group(self):
        return self.tr("LUCIS-OPEN Tools for QGIS")

    def groupId(self):
        return "lucisopen"

    def name(self):
        return "pointdistance"

    def displayName(self):
        return self.tr("Distance to Point Features")

    def shortHelpString(self):
        return self.tr("Calculate distance to point features.\n"
                       "Calculate distance for each feature in the input data "
                       "to its nearest neighbor in the point dataset.")

    def __init__(self):
        super().__init__()
        self.method = (
            ('Euclidean', self.tr('Euclidean')),
            ('Manhattan', self.tr('Manhattan'))
        )
        self.data_type = (
            ('Integer', self.tr('Integer')),
            ('Float', self.tr('Float'))
        )

    def createInstance(self):
        return PointDistance()

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.POINT,
                self.tr('Point layer'),
                types=[QgsProcessing.TypeVectorPoint]
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.METHOD,
                self.tr('Distance method'),
                options=[m[1] for m in self.method],
                defaultValue=0
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.DATA_TYPE,
                self.tr('Output data type'),
                options=[dtype[1] for dtype in self.data_type],
                defaultValue=1
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                name=self.OUTPUT_COLUMN,
                description=self.tr('Output column name'),
            )
        )
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT,
                self.tr('Output shapefile')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        input_lyr = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        point_lyr = self.parameterAsVectorLayer(parameters, self.POINT, context)
        method = self.method[self.parameterAsEnum(parameters,
                                                  self.METHOD,
                                                  context)][0]
        data_type = self.parameterAsEnum(parameters, self.DATA_TYPE, context)
        output_clm = self.parameterAsString(parameters, self.OUTPUT_COLUMN, context)
        output_shp = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from .loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        point_gdf = LUCISOpenQGISUtils.vector_to_gdf(point_lyr)
        data_type = int if data_type == 0 else float

        input_gdf[output_clm] = distance.to_point(input_gdf, point_gdf,
                                                  method, data_type)
        input_gdf.to_file(output_shp)
        return {self.OUTPUT: output_shp}
