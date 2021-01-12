from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterString)
from pylusat import distance
import sys
import os


class LineDistance(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    LINE = "LINE"
    CELL_SIZE = "CELL_SIZE"
    METHOD = "METHOD"
    DATA_TYPE = "DATA_TYPE"
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
        return "linedistance"

    def displayName(self):
        return self.tr("Distance to Line Features")

    def shortHelpString(self):
        html_doc = '''
        <p>Calculate distance for each feature in the input data to \
        its nearest neighbor in the line layer.<p>
        
        <h3>Input Layer</h3>
        <p>Input vector layer.</p>

        <h3>Line Layer</h3>
        <p>Input line layer.</p>

        <h3>Cell Size for Rasterizing Line Features</h3>
        <p>The size of cells, to which the line features are rasterized.</p>

        <h3>Distance Method</h3>
        <p>Choose between
        <a href="https://www.wikiwand.com/en/Euclidean_distance">Euclidean Distance</a> or
        <a href="https://www.wikiwand.com/en/Taxicab_geometry">Manhattan Distance</a>.</p>

        <h3>Output Data Type</h3>
        <p>Choose between <i>integer</i> or <i>float</i> (default) \
        output value.</p>

        <h3>Output Column Name</h3>
        <p>Name of the column storing distances in the output layer.</p>

        <h3>Output</h3>
        <p>Output vector layer.</p>
        '''
        return html_doc

    def createInstance(self):
        return LineDistance()

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
        self.addParameter(
            QgsProcessingParameterNumber(
                self.CELL_SIZE,
                self.tr('Cell size for rasterizing line layer'),
                defaultValue=30,
                type=QgsProcessingParameterNumber.Double
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
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        input_lyr = self.parameterAsVectorLayer(parameters, self.INPUT, context)
        line_lyr = self.parameterAsVectorLayer(parameters, self.LINE, context)
        cell_size = self.parameterAsDouble(parameters, self.CELL_SIZE, context)
        method = self.method[self.parameterAsEnum(parameters, self.METHOD, context)][0]
        data_type = self.parameterAsEnum(parameters, self.DATA_TYPE, context)
        output_clm = self.parameterAsString(parameters, self.OUTPUT_COLUMN, context)
        output_file = self.parameterAsOutputLayer(parameters, self.OUTPUT,
                                                  context)
        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        line_gdf = LUCISOpenQGISUtils.vector_to_gdf(line_lyr)
        data_type = int if data_type == 0 else float

        input_gdf[output_clm] = distance.to_line(
            input_gdf, line_gdf, cell_size, method
        ).astype(data_type)

        input_gdf.to_file(output_file)
        return {self.OUTPUT: output_file}
