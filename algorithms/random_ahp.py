from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterString)
# from pylusat.geotools import spatial_join
import geopandas as gpd
from collections import defaultdict


class _AggStringToDict:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, column, statistic):
        self.data[column].add(statistic)


# class _ValidateField:


class RandomAHP(QgsProcessingAlgorithm):
    TARGET = "TARGET"
    JOIN = "JOIN"
    OP = "OP"
    COLUMNS_AGG = "COLUMNS_AGG"
    JOIN_TYPE = "JOIN_TYPE"
    KEEP_ALL = "KEEP_ALL"
    OUTPUT = "OUTPUT"

    OP_OPTION = ["intersects", "contains", "within"]
    JOIN_OPTION = ["one to one", "one to many"]

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)

    def group(self):
        return self.tr("LUCIS_OPEN for QGIS")

    def groupId(self):
        return "lucisopen"

    def name(self):
        return "randomahp"

    def displayName(self):
        return self.tr("Generate Random AHP Weights")

    def shortHelpString(self):
        return self.tr("Join attributes from the join features to the target "
                       "features based on specified spatial relationship.")

    def createInstance(self):
        return RandomAHP()

    def __init__(self):
        super().__init__()

    def initAlgorithm(self, config=None):
        # self.predicates = (
        #
        # )

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.TARGET,
                self.tr('Target layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.JOIN,
                self.tr('Join layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.OP,
                self.tr('Overlap type'),
                options=self.OP_OPTION,
                defaultValue=0
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.COLUMNS_AGG,
                self.tr('Columns join to target features (separate by semicolon)'),
                defaultValue=None
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.JOIN_TYPE,
                self.tr('Join type'),
                options=self.JOIN_OPTION,
                defaultValue=0
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.KEEP_ALL,
                self.tr('Keep all features in the target layer'),
                defaultValue=True
            )
        )
        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.OUTPUT,
                self.tr('Output shapefile'),
                'Shapefile (*.shp)'
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        target_shp = self.parameterDefinition('TARGET').valueAsPythonString(
            parameters['TARGET'], context)
        join_shp = self.parameterDefinition('JOIN').valueAsPythonString(
            parameters['JOIN'], context)
        columns = self.OP_OPTION[self.parameterAsEnum(parameters, self.OP,
                                                      context)]
        op = self.OP_OPTION[self.parameterAsEnum(parameters, self.OP, context)]
        output_shp = self.parameterAsFileOutput(parameters, self.OUTPUT,
                                                context)
        feedback.pushInfo(target_shp)
        target_gdf = gpd.read_file(target_shp[1:-1])
        join_gdf = gpd.read_file(join_shp[1:-1])
        # output = spatial_join(target_gdf, join_gdf, op, col,
        #                                      op, buffer)
        # output.to_file(output_shp)

        return {self.OUTPUT: output_shp}
