from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterString)
import sys
import os
from pylusat import density, base


class LineDensity(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    LINE = "LINE"
    CELL_SIZE = "CELL_SIZE"
    SEARCH_RADIUS = "SEARCH_RADIUS"
    AREAL_UNIT = "AREAL_UNIT"
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
        return "linedensity"

    def displayName(self):
        return self.tr("Density of Line Features")

    def shortHelpString(self):
        return self.tr("Calculate density of line features.\n"
                       "Calculate density of line features within the "
                       "specified search radius of each input polygon "
                       "features.")

    def createInstance(self):
        return LineDensity()

    def __init__(self):
        super().__init__()
        self.areal_unit = (
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
                self.LINE,
                self.tr('Line layer'),
                types=[QgsProcessing.TypeVectorLine]
            )
        )
        cell_size = QgsProcessingParameterDistance(
            self.CELL_SIZE,
            self.tr('Cell size for rasterizing line features'),
            defaultValue=30,
            parentParameterName=self.LINE,
            optional=True
        )
        cell_size.setMetadata({
            'widget_wrapper': {
                'decimals': 0
            }
        })
        self.addParameter(cell_size)
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
                self.AREAL_UNIT,
                self.tr('Areal unit (for density value)'),
                options=[u[1] for u in self.areal_unit],
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
        source_lyr = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        line_lyr = self.parameterAsVectorLayer(parameters, self.LINE, context)
        cell_size = self.parameterAsDouble(parameters, self.CELL_SIZE, context)
        search_radius = self.parameterAsDouble(parameters, self.SEARCH_RADIUS,
                                               context)
        areal_unit = self.areal_unit[self.parameterAsEnum(parameters,
                                                          self.AREAL_UNIT,
                                                          context)][0]
        output_clm = self.parameterAsString(parameters, self.OUTPUT_COLUMN, context)
        output_file = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import LUCISOpenQGISUtils

        source_gdf = LUCISOpenQGISUtils.vector_to_gdf(source_lyr)
        line_gdf = LUCISOpenQGISUtils.vector_to_gdf(line_lyr)
        search_radius = (f'{search_radius} '
                         f'{base.GeoDataFrameManager(source_gdf).geom_unit_id}')
        source_gdf[output_clm] = density.of_line(source_gdf, line_gdf, cell_size,
                                                 search_radius, areal_unit)
        source_gdf.to_file(output_file)
        return {self.OUTPUT: output_file}
