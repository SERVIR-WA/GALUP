import sys
import os
from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterString,
                       QgsProcessingParameterVectorDestination)
from pylusat import distance


class RasterCellDistance(QgsProcessingAlgorithm):
    INPUT = 'INPUT'
    RASTER = 'RASTER'
    VALUE = 'VALUE'
    NODATA = 'NODATA'
    METHOD = 'METHOD'
    DATA_TYPE = 'DATA_TYPE'
    OUTPUT_COLUMN = 'OUTPUT_COLUMN'
    OUTPUT = 'OUTPUT'

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)

    def group(self):
        return self.tr('LUCIS-OPEN Tools for QGIS')

    def groupId(self):
        return 'lucisopen'

    def name(self):
        return 'celldistance'

    def displayName(self):
        return self.tr('Distance to Raster Cell')

    def shortHelpString(self):
        html_doc = '''
        <p>Calculate distance for each feature in the input data to its \
        nearest cell with the specified value in the raster layer. You must \
        make sure that the specified value is valid, i.e., it exists in the \
        raster layer.</p>
        
        <h3>Input</h3>
        <p>Input vector layer.</p>
        
        <h3>Raster</h3>
        <p>Input raster layer.</p>
        
        <h3>Cell Value</h3>
        <p>The value of cells, to which distances are calculated.</p>
        
        <h3>No Data</h3>
        <p>Value should be considered as "no data" in the raster layer.</p>
        
        <h3>Distance Method</h3>
        <p>Choose between \
        <a href="https://www.wikiwand.com/en/Euclidean_distance">Euclidean Distance</a> or \
        <a href="https://www.wikiwand.com/en/Taxicab_geometry">Manhattan Distance</a>.</p>
        
        <h3>Output Data Format</h3>
        <p>Choose between <i>integer</i> or <i>float</i> (default) output value.</p>
        
        <h3>Output Column Name</h3>
        <p>Name of the column storing distances in the output layer.</p>
        
        <h3>Output</h3>
        <p>Output vector layer</p>
        '''
        return html_doc

    def createInstance(self):
        return RasterCellDistance()

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

    def initAlgorithm(self, configuration={}):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.RASTER,
                self.tr('Raster layer'),
            )
        )
        self.addParameter(
            QgsProcessingParameterNumber(
                self.VALUE,
                self.tr('Cell value equals to'),
                type=QgsProcessingParameterNumber.Integer
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
                self.tr('Output layer'),
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        input_lyr = self.parameterAsVectorLayer(
            parameters, self.INPUT, context
        )
        raster_lyr = self.parameterAsRasterLayer(
            parameters, self.RASTER, context
        )
        value = self.parameterAsInt(parameters, self.VALUE, context)
        nodata = parameters[self.NODATA]
        method = self.method[self.parameterAsEnum(
            parameters, self.METHOD, context)
        ][0]
        data_type = self.parameterAsEnum(
            parameters, self.DATA_TYPE, context
        )
        output_clm = self.parameterAsString(
            parameters, self.OUTPUT_COLUMN, context
        )
        output_file = self.parameterAsOutputLayer(
            parameters, self.OUTPUT, context
        )

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        raster_path = raster_lyr.dataProvider().dataSourceUri()
        data_type = int if data_type == 0 else float

        input_gdf[output_clm] = distance.to_cell(
            input_gdf, raster_path, value, nodata, method, data_type
        )
        output = input_gdf.to_file(output_file)
        return {self.OUTPUT: output}
