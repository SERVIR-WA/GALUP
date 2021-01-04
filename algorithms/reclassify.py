from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterField,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterString)
import sys
import os
from pylusat import rescale


class Reclassify(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    INPUT_FIELD = "INPUT_FIELD"
    OLD_VALUE = "OLD_VALUE"
    NEW_VALUE = "NEW_VALUE"
    NODATA = "NODATA"
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
        return "reclassify"

    def displayName(self):
        return self.tr("Reclassify Field")

    def shortHelpString(self):
        return self.tr("Reclassify a field in the input table.\n"
                       "Reclassify an existing field based on predefined "
                       "rules and store the translated values in a new field.")

    def createInstance(self):
        return Reclassify()

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
                self.tr('Field to reclassify'),
                parentLayerParameterName=self.INPUT
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.OLD_VALUE,
                self.tr('Old values')
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.NEW_VALUE,
                self.tr('New values')
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                self.NODATA,
                self.tr('No data value'),
                optional=True,
                defaultValue=0,
                type=QgsProcessingParameterNumber.Integer
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                self.OUTPUT_COLUMN,
                self.tr('Output column name')
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
        old_val = self.parameterAsString(parameters, self.OLD_VALUE, context)
        new_val = self.parameterAsString(parameters, self.NEW_VALUE, context)
        nodata = parameters[self.NODATA]
        output_clm = self.parameterAsString(parameters, self.OUTPUT_COLUMN, context)
        output_file = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import (LUCISOpenQGISUtils,
                            StringParameterNumberList,
                            StringParameterIntervalList,
                            StringParameterCategoryList)

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)

        try:
            re_key = StringParameterIntervalList(input_clm,
                                                 old_val).as_tuple_list
        except ValueError:
            try:
                re_key = StringParameterNumberList(input_clm,
                                                   old_val).as_number_list
            except ValueError:
                re_key = StringParameterCategoryList(input_clm,
                                                     old_val).as_category_list
        try:
            re_val = StringParameterNumberList(input_clm,
                                               new_val).as_number_list
        except ValueError:
            re_val = StringParameterCategoryList(input_clm,
                                                 new_val).as_category_list
        re_dict = dict(zip(re_key, re_val))
        nodata = float(nodata)
        output = rescale.reclassify(input_gdf, input_clm, re_dict,
                                    output_clm, nodata)

        output.to_file(output_file)

        return {self.OUTPUT: output_file}
