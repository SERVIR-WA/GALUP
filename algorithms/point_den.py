import sys
import os
from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterField,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterString)
from pylusat import density, base


class PointDensity(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    POINT = "POINT"
    POP_COLUMN = 'POP_COLUMN'
    SEARCH_RADIUS = "SEARCH_RADIUS"
    AREA_UNIT = "AREA_UNIT"
    OUTPUT_COLUMN = "OUTPUT_COLUMN"
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
        return "pointdensity"

    def displayName(self):
        return self.tr("Density of Point Features")

    def shortHelpString(self):
        return self.tr("Calculate density of point features.\n"
                       "Calculate density of point features within the "
                       "specified search radius of each input features.")

    def createInstance(self):
        return PointDensity()

    def __init__(self):
        super().__init__()
        self.area_unit = (
            ('Square meters', self.tr('Square meters')),
            ('Square kilometers', self.tr('Square kilometers')),
            ('Hectares', self.tr('Hectares')),
            ('Square feet', self.tr('Square feet')),
            ('Square miles', self.tr('Square miles')),
            ('Acres', self.tr('Acres'))
        )

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
            QgsProcessingParameterField(
                self.POP_COLUMN,
                self.tr('Population field'),
                parentLayerParameterName=self.POINT,
                type=QgsProcessingParameterField.Numeric
            )
        )
        search_radius = QgsProcessingParameterDistance(
            self.SEARCH_RADIUS,
            self.tr('Search radius'),
            parentParameterName=self.INPUT
        )
        search_radius.setMetadata({
            'widget_wrapper': {
                'decimals': 2
            }
        })
        self.addParameter(search_radius)
        self.addParameter(
            QgsProcessingParameterEnum(
                self.AREA_UNIT,
                self.tr('Area unit (for density value)'),
                options=[u[1] for u in self.area_unit],
                defaultValue=0
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
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        input_lyr = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        point_lyr = self.parameterAsVectorLayer(parameters, self.POINT, context)
        pop_clm = self.parameterAsString(parameters, self.POP_COLUMN, context)
        search_radius = self.parameterAsDouble(parameters, self.SEARCH_RADIUS,
                                               context)
        area_unit = self.area_unit[self.parameterAsEnum(parameters,
                                                        self.AREA_UNIT,
                                                        context)][0]
        output_clm = self.parameterAsString(parameters, self.OUTPUT_COLUMN,
                                            context)
        output_shp = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from .loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        point_gdf = LUCISOpenQGISUtils.vector_to_gdf(point_lyr)
        search_radius = (f'{search_radius} '
                         f'{base.GeoDataFrameManager(input_gdf).geom_unit_id}')
        input_gdf[output_clm] = density.of_point(input_gdf, point_gdf, pop_clm,
                                                 search_radius, area_unit)
        input_gdf.to_file(output_shp)
        return {self.OUTPUT: output_shp}
