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
        return self.tr("Rescale a field linearly.\n"
                       "If Start is greater than end, the rescaling is in the "
                       "same direction as values in the input field, i.e., "
                       "smaller (bigger) values in the input field correspond "
                       "to smaller (bigger) values in the output. If argument "
                       "Start is less than end, the rescaling is in the "
                       "reverse direction as values in the input field. The "
                       "start and end of the input input do not necessarily "
                       "to be the minimum and maximum of the input field. "
                       "Values beyond the specified bound will be assigned to "
                       "Output minimum and Output maximum, depending on which "
                       "side they are on.")

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
        from .loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        output = rescale.linear(
            input_gdf, input_clm, output_clm, start, end,
            output_min, output_max
        )

        output.to_file(output_file)
        return {self.OUTPUT: output_file}
