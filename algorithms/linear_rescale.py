import sys
import os
from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterField,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterString)
from pylusat import rescale
import geopandas as gpd


class LinearRescale(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    INPUT_FIELD = "INPUT_FIELD"
    START = "START"
    END = "END"
    NEW_MIN = "NEW_MIN"
    NEW_MAX = "NEW_MAX"
    OUTPUT_FIELD = "OUTPUT_FIELD"
    OUTPUT = "Rescaled"

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)

    def group(self):
        return self.tr("LUCIS-OPEN for QGIS")

    def groupId(self):
        return "lucisopen"

    def name(self):
        return "linearrescale"

    def displayName(self):
        return self.tr("Rescale Field Linearly")

    def shortHelpString(self):
        html_doc = '''
        <p>Rescale values in a field into a new bound.</p>

        <h3>Input layer</h3>
        <p>Input vector layer.</p>

        <h3>Field to rescale</h3>
        <p>Transform values in a field to a specified continuous \
        scale, i.e., on a 1 to 9 scale</p>

        <h3>Start/End value for rescaling</h3>
        <p>If Start is less than end, the rescaling is in the \
        same direction as values in the input field, i.e., \
        smaller (bigger) values in the input field correspond to \
        smaller (bigger) values in the output.

        If argument Start is greater than end, the rescaling is \
        in the reverse direction as values in the input field, \
        i.e., smaller (bigger) values in the input field correspond \
        to bigger (smaller) values in the output.</p>


        <h3>New minimum/maximum</h3>
        <p>Values beyond the specified bound will be assigned to \
        Output minimum and Output maximum, depending on which side \
        they are on, i.e., when start value is less than end, values \
        smaller than start value will be recorded as Output minimum</p>


        <h3>Output field name</h3>
        <p>Name the rescaled field in Input table.</p>


        <h3>Output layer</h3>
        <p>Output vector layer</p>
        '''
        return html_doc

    def createInstance(self):
        return LinearRescale()

    def __init__(self):
        super().__init__()

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                self.INPUT_FIELD,
                self.tr('Field to rescale'),
                parentLayerParameterName=self.INPUT,
                type=QgsProcessingParameterField.Numeric
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                name=self.START,
                description=self.tr('Start value for rescaling'),
                type=QgsProcessingParameterNumber.Double,
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                name=self.END,
                description=self.tr('End value for rescaling'),
                type=QgsProcessingParameterNumber.Double,
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                self.NEW_MIN,
                self.tr('New minimum'),
                optional=True,
                defaultValue=1
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                self.NEW_MAX,
                self.tr('New maximum'),
                optional=True,
                defaultValue=9
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.OUTPUT_FIELD,
                self.tr('Output field name')
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
        input_clm = self.parameterAsString(parameters, self.INPUT_FIELD, context)
        start = parameters[self.START]
        end = parameters[self.END]
        output_min = self.parameterAsDouble(parameters, self.NEW_MIN, context)
        output_max = self.parameterAsDouble(parameters, self.NEW_MAX, context)
        output_clm = self.parameterAsString(parameters, self.OUTPUT_FIELD, context)
        output_file = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        output = rescale.linear(
            input_gdf, input_clm, output_clm, start, end,
            output_min, output_max
        )

        output.to_file(output_file)
        return {self.OUTPUT: output_file}
