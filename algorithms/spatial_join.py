from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterString)
from pylusat import geotools
import sys
import os


class SpatialJoin(QgsProcessingAlgorithm):
    TARGET = "TARGET"
    JOIN = "JOIN"
    OP = "OP"
    COLUMNS_AGG = "COLUMNS_AGG"
    HOW = "HOW"
    KEEP_ALL = "KEEP_ALL"
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
        return "spatialjoin"

    def displayName(self):
        return self.tr("Spatial Join")

    def shortHelpString(self):
        return self.tr("Join attributes from the join features to the target "
                       "features based on specified spatial relationship.")

    def createInstance(self):
        return SpatialJoin()

    def __init__(self):
        super().__init__()
        self.op = (
            ('intersects', self.tr('intersects')),
            ('contains', self.tr('contains')),
            ('within', self.tr('within'))
        )
        self.how = (
            ('one to one', self.tr('one to one')),
            ('one to many', self.tr('one to many'))
        )

    def initAlgorithm(self, config=None):
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
        op = QgsProcessingParameterEnum(
            self.OP,
            self.tr('Join option (geometric predicate)'),
            options=[p[1] for p in self.op],
            allowMultiple=False,
            defaultValue=0
        )
        op.setMetadata({
            'widget_wrapper': {
                'useCheckBoxes': True,
                'columns': 3
            }
        })
        self.addParameter(op)
        self.addParameter(
            QgsProcessingParameterString(
                self.COLUMNS_AGG,
                self.tr('Columns to join (separated by semicolon)'),
                defaultValue=None
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                self.HOW,
                self.tr('Join type'),
                options=[o[1] for o in self.how],
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
        target = self.parameterAsVectorLayer(parameters, self.TARGET, context)
        join = self.parameterAsVectorLayer(parameters, self.JOIN, context)
        op = self.op[self.parameterAsEnum(parameters, self.OP, context)][0]

        columns_agg = self.parameterAsString(parameters, self.COLUMNS_AGG, context)
        how = self.how[self.parameterAsEnum(parameters, self.HOW, context)][0]
        keep_all = self.parameterAsBoolean(parameters, self.KEEP_ALL, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import LUCISOpenQGISUtils
        process_util = LUCISOpenQGISUtils()

        aggs = (tuple(item.strip().split()) for item in columns_agg.split(";"))
        for column, statistic in aggs:
            process_util.to_agg_dict(column, statistic)

        output_shp = self.parameterAsFileOutput(parameters, self.OUTPUT, context)

        target_gdf = LUCISOpenQGISUtils.vector_to_gdf(target)
        join_gdf = LUCISOpenQGISUtils.vector_to_gdf(join)
        output = geotools.spatial_join(target_gdf, join_gdf, op,
                                       process_util.agg_dict, how, keep_all)
        output.to_file(output_shp)

        return {self.OUTPUT: output_shp}
