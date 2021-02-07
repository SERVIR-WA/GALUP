from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorDestination,
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
        html_doc = '''
        <p>Join attributes from the join features to the target features based \
        on specified spatial relationship.</p>

        <h3>Target layer</h3>
        <p>Attributes of the target features and the attributes from the \
        joined features are transferred to the output feature class. However, \
        a subset of attributes can be defined in the field map parameter.</p>

        <h3>Join layer</h3>
        <p>The attributes from the join features are joined to the attributes \
        of the target features.</p>

        <h3>Join option</h3>
        <p>Defines the criteria used to match rows. The match options are:

        Intersect—The features in the join features will be matched if they \
        intersect a target feature. This is the default. Specify a distance in \
        the Search Radius parameter.

        Contains—The features in the join features will be matched if a target \
        feature contains them. The target features must be polygons or \
        polylines. For this option, the target features cannot be points, and \
        the join features can only be polygons when the target features are \
        also polygons.

        Within—The features in the join features will be matched if a target \
        feature is within them. It is opposite to Contains. For this option, \
        the target features can only be polygons when the join features are \
        also polygons. Point can be join feature only if point is target.</p>

        <h3>Columns to join</h3>
        <p>A new feature class containing the attributes of join features, i.e.\
        ,"<clm_name> <func>" e.g., "bldg_value sum". The types of function \
        defaults to ['first'], other valid functions are ['last', 'sum', \
        'mean', 'median', 'max', 'min','std', 'var', 'count', 'size'].

        First—Use the columns' first value.

        Last—Use the columns' last value..

        Sum—Calculate the total of the columns' values.

        Mean—Calculate the mean (average) of the columns' values.

        Median—Calculate the median (middle) of the columns' values.

        Min—Use the minimum value of all columns' values.

        Max—Use the maximum value of all columns' values.

        Std(Standard deviation)—Use the standard deviation classification method \
        on all columns' values.

        Var(Variance)—Calculates the variance for all records of the specified field.

        Count—Find the number of records included in the calculation.</p>

        <h3>Join type</h3>
        <p>Determines how joins between the target features and join features \
        will be handled in the output feature class if multiple join features \
        are found that have the same spatial relationship with a single target \
        feature.

        Join one to one—If multiple join features are found that have the same \
        spatial relationship with a single target feature, the attributes from \
        the multiple join features will be aggregated. For example, if a point \
        target feature is found within two separate polygon join features, the \
        attributes from the two polygons will be aggregated before being \
        transferred to the output point feature class. If one polygon has an \
        attribute value of 3 and the other has a value of 7, and a Sum merge \
        rule is specified, the aggregated value in the output feature class \
        will be 10.

        Join one to many—If multiple join features are found that have the same \
        spatial relationship with a single target feature, the output feature \
        class will contain multiple copies (records) of the target feature. For \
        example, if a single point target feature is found within two separate \
        polygon join features, the output feature class will contain two copies \
        of the target feature: one record with the attributes of one polygon, \
        and another record with the attributes of the other polygon.</p>

        <h3>Output shapefile</h3>
        <p>Output vector layer</p>
        '''
        return html_doc

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
            QgsProcessingParameterVectorDestination(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        target = self.parameterAsVectorLayer(parameters, self.TARGET, context)
        join = self.parameterAsVectorLayer(parameters, self.JOIN, context)
        op = self.op[self.parameterAsEnum(parameters, self.OP, context)][0]
        columns_agg = self.parameterAsString(parameters, self.COLUMNS_AGG, context)
        how = self.how[self.parameterAsEnum(parameters, self.HOW, context)][0]
        keep_all = self.parameterAsBoolean(parameters, self.KEEP_ALL, context)
        output_file = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
        from loqlib import LUCISOpenQGISUtils

        process_util = LUCISOpenQGISUtils()

        aggs = (tuple(item.strip().split()) for item in columns_agg.split(";"))

        for column, statistic in aggs:
            process_util.to_agg_dict(column, statistic)

        target_gdf = LUCISOpenQGISUtils.vector_to_gdf(target)
        join_gdf = LUCISOpenQGISUtils.vector_to_gdf(join)
        output = geotools.spatial_join(target_gdf, join_gdf, op,
                                       process_util.agg_dict,
                                       how, keep_all)
        output.to_file(output_file)
        return {self.OUTPUT: output_file}
