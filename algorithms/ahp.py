from PyQt5.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingAlgorithm,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterMatrix,
                       QgsProcessingParameterString,
                       QgsProcessingOutputNumber,
                       QgsProcessingOutputString,
                       QgsProcessingParameterFileDestination)
import numpy as np
import codecs
from pylusat import utils


class AHP(QgsProcessingAlgorithm):
    OP = "OP"
    CRITERIA = "CRITERIA"
    COMPARE_TABLE = "COMPARE_TABLE"
    PRIORITY_VECTOR = "PRIORITY_VECTOR"
    CR = "CR"
    OUTPUT_HTML_FILE = "OUTPUT_HTML_FILE"

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)

    def group(self):
        return self.tr("LUCIS-OPEN Tools for QGIS")

    def groupId(self):
        return "lucisopen"

    def name(self):
        return "ahp"

    def displayName(self):
        return self.tr("Compute AHP Weights")

    def shortHelpString(self):
        return self.tr("Compute AHP weights.")

    def createInstance(self):
        return AHP()

    def __init__(self):
        super().__init__()
        self.op_option = (
            ('Defined AHP weights', self.tr('Defined AHP weights')),
            ('Random AHP weights', self.tr('Random AHP weights'))
        )

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterEnum(
                self.OP,
                self.tr('Weights generating options'),
                options=[op[1] for op in self.op_option],
                defaultValue=0
            )
        )
        self.addParameter(
            QgsProcessingParameterMatrix(
                self.CRITERIA,
                self.tr('List of criteria to weight'),
                headers=['Name'],
                defaultValue=['Criterion 1', 'Criterion 2', 'Criterion 3']
            )
        )
        self.addParameter(
            QgsProcessingParameterMatrix(
                self.COMPARE_TABLE,
                self.tr('Comparison table for creating the reciprocal matrix'),
                headers=['Row id', 'Column id', 'Pair-wise importance'],
                defaultValue=[
                    1, 2, 5,
                    1, 3, 4,
                    2, 3, 1/3
                ],
                optional=True
            )
        )
        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.OUTPUT_HTML_FILE,
                self.tr('HTML report'),
                fileFilter=self.tr('HTML files (*.html)'),
                defaultValue=None,
                optional=True
            )
        )
        self.addOutput(
            QgsProcessingOutputString(
                self.PRIORITY_VECTOR,
                self.tr('priority vector')
            )
        )
        self.addOutput(
            QgsProcessingOutputNumber(
                self.CR,
                self.tr('consistency ratio')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        op = self.op_option[self.parameterAsEnum(parameters, self.OP,
                                                 context)][0]
        criteria = parameters[self.CRITERIA]
        num_weights = len(criteria)
        feedback.pushInfo(str(num_weights))
        compare_table = self.parameterAsMatrix(parameters, self.COMPARE_TABLE,
                                               context)
        output_file = self.parameterAsFileOutput(parameters,
                                                 self.OUTPUT_HTML_FILE,
                                                 context)

        com_tbl = np.array(compare_table).reshape((-1, 3))
        n_row = np.sum(np.arange(num_weights)).item()
        assert n_row == com_tbl.shape[0], (
            f'Given {num_weights} weights, there should be {n_row} in the '
            f'compare table. Unable to construct a valid reciprocal matrix.'
        )
        r_mtx = np.identity(num_weights)
        for i in range(n_row):
            row_id, col_id, value = com_tbl[i]
            r_mtx[int(row_id)-1, int(col_id)-1] = value

        r_mtx[np.tril_indices(num_weights, -1)] = (
            1 / r_mtx.T[np.tril_indices(num_weights, -1)]
        )
        if op == 'Defined AHP weights':
            priority_vector, cr = utils.ahp(r_mtx)
        else:
            priority_vector, cr = utils.random_ahp(num_weights)
        if output_file:
            self.createHTML(output_file, criteria, priority_vector, cr, op)

        return {self.PRIORITY_VECTOR: priority_vector,
                self.CR: cr,
                self.OUTPUT_HTML_FILE: output_file}

    def createHTML(self, output_file, criteria, weights, cr, op):
        with codecs.open(output_file, 'w', encoding='utf-8') as f:
            f.write('<html><head>')
            f.write('<meta http-equiv="Content-Type" content="text/html; '
                    'charset=utf-8" /></head><body>')
            f.write(self.tr('<h1>Analytic Hierarchy Process</h1>'))
            f.write(self.tr(f'<p><b>Weights</b> (option: {op})</p>'))
            f.write('<ul>')
            for i, w in enumerate(weights):
                f.write(f'<li><i>{criteria[i]}</i>: {w:.3f}</li>')
            f.write('</ul>')
            f.write(self.tr(f'<p>Consistency Ratio (CR):</p>'))
            f.write(f'<p>{cr:.5f}</p></body></html>')
