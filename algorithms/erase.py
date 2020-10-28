import sys
import os
from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination)
from pylusat import geotools


class Erase(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    ERASE = "ERASE"
    OUTPUT = "Erased"

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)

    def group(self):
        return self.tr("LUCIS-OPEN Tools for QGIS")

    def groupId(self):
        return "lucisopen"

    def name(self):
        return "erase"

    def displayName(self):
        return self.tr("Erase")

    def shortHelpString(self):
        html_doc = '''
        Calculate distance to raster cells.
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
        <a href="https://en.wikipedia.org/w/index.php?title=Euclidean_distance&oldid=976383156">Euclidean Distance</a> \
        or \
        <a href/="vhttps://en.wikipedia.org/w/index.php?title=Taxicab_geometry&oldid=960454083">Manhattan Distance</a>.</p>
        <h3>Outp..ut Data Format</h3>
        <p>Choose between <i>integer</i> or <i>float</i> (default) \
        output value.</p>
        <h3>Output Column Name</h3>
        <p>Name of the column storing distances in the output layer.</p>
        <h3>Output</h3>
        <p>Output vector layer</p>
        '''
        return html_doc

    def createInstance(self):
        return Erase()

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
            QgsProcessingParameterFeatureSource(
                self.ERASE,
                self.tr('Erase layer'),
                types=[QgsProcessing.TypeVectorPolygon]
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
        erase_lyr = self.parameterAsVectorLayer(parameters, self.ERASE, context)
        output_file = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import LUCISOpenQGISUtils

        input_gdf = LUCISOpenQGISUtils.vector_to_gdf(input_lyr)
        erase_gdf = LUCISOpenQGISUtils.vector_to_gdf(erase_lyr)
        output = geotools.erase(input_gdf, erase_gdf)

        output.to_file(output_file)
        return {self.OUTPUT: output_file}
