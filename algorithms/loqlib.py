# LUCIS_OPEN QGIS Library

from collections import defaultdict
from qgis.core import QgsVectorLayer
import pandas as pd
from shapely import wkt
import geopandas as gpd


class StringParameter:

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self._validate()

    def _validate(self):
        if not isinstance(self.value, str):
            raise TypeError("'{}' must be a string.".format(self.name))

    def __repr__(self):
        return "{}('{}', '{}')".format(self.__class__.__name__,
                                       self.name, self.value)

    def __str__(self):
        return "'{}', '{}'".format(self.name, self.value)


class StringParameterNumber(StringParameter):

    def __init__(self, name, value):
        super().__init__(name, value)
        if not self._validate_number():
            raise ValueError("'{}' cannot be used as a "
                             "valid number.".format(self.value))

    def _validate_number(self):
        try:
            float(self.value)
            return True
        except ValueError:
            return False

    @property
    def as_number(self):
        if "." in self.value:
            return float(self.value)
        else:
            return int(self.value)


class StringParameterNumberList(StringParameter):

    def __init__(self, name, value):
        super().__init__(name, value)
        if not self._validate_number_list():
            raise ValueError(
                "f'{self.value}' is not a valid number list "
                "since {self.err}")

    def _validate_number_list(self):
        try:
            self.number_list = [
                StringParameterNumber("number", _.strip()).as_number
                for _ in self.value.split(",")
            ]
            return True
        except ValueError as err:
            self.err = err
            return False

    @property
    def as_number_list(self):
        return self.number_list


class StringParameterInterval(StringParameter):

    def __init__(self, name, value):
        super().__init__(name, value)
        self._validate_interval()

    def _validate_interval(self):
        if "-" not in self.value:
            raise ValueError("'{}' is not a valid interval. "
                             "Use '-' to separate the start and "
                             "the end of a interval.".format(self.value))
        else:
            _interval = self.value.split("-")
            if len(_interval) != 2:
                raise ValueError("'{}' is not a "
                                 "valid interval.".format(self.value))
            _start, _end = [StringParameterNumber('bound', _bound)
                            for _bound in _interval]
            if _start.as_number >= _end.as_number:
                raise ValueError("'{}' is not a valid interval. A interval's "
                                 "start value must be smaller than "
                                 "its end value.".format(self.value))
            else:
                self.start = _start.as_number
                self.end = _end.as_number

    @property
    def as_tuple(self):
        return self.start, self.end


class StringParameterIntervalList(StringParameter):

    def __init__(self, name, value, enforce_ascending=False):
        super().__init__(name, value)
        self.enforce_ascending = enforce_ascending
        if not self._validate_interval_list():
            raise ValueError("'{}' is not a valid definition, since '{}' "
                             "is not a valid list of intervals. "
                             "`if enforce_ascending == True`, make sure "
                             "bounds of each interval follows an ascending "
                             "order.".format(self.name, self.value))

    def _validate_interval_list(self):
        try:
            self.interval_list = [
                StringParameterInterval("interval", _.strip()).as_tuple
                for _ in self.value.split(",")
            ]
            if self.enforce_ascending:
                from itertools import chain
                chained_list = list(chain.from_iterable(self.interval_list))
                assert sorted(chained_list) == chained_list
            return True
        except AssertionError:
            return False

    @property
    def as_tuple_list(self):
        return self.interval_list


class StringParameterCategoryList(StringParameter):

    def __init__(self, name, value):
        super().__init__(name, value)
        if not self._validate_category_list():
            raise ValueError("{} is not a valid category list "
                             "since {}".format(self.value, self.err))

    def _validate_category_list(self):
        try:
            self.category_list = [StringParameter("category", _.strip()).value
                                  for _ in self.value.split(",")]
            return True
        except TypeError as err:
            self.err = err
            return False

    @property
    def as_category_list(self):
        return self.category_list


class LUCISOpenQGISUtils:

    def __init__(self):
        self.agg_dict = defaultdict(set)

    def to_agg_dict(self, column: str, statistic: str):
        self.agg_dict[column].add(statistic)

    @classmethod
    def vector_to_gdf(cls, qgis_vector_lyr: QgsVectorLayer) -> gpd.GeoDataFrame:

        def _catch_null(attribute):
            try:
                if attribute.isNull():
                    return None
            except AttributeError:
                return attribute

        feature_list = [
            [_catch_null(attr) for attr in feature.attributes()] +
            [feature.geometry().asWkt()]
            for feature in qgis_vector_lyr.getFeatures()
        ]

        columns = [field.name() for field in qgis_vector_lyr.fields()]
        columns.append('geometry')
        df = pd.DataFrame(feature_list, columns=columns)
        df['geometry'] = df['geometry'].apply(wkt.loads)
        if qgis_vector_lyr.wkbType() == 6:   # if geometry is MultiPolygon
            df['geometry'] = df['geometry'].apply(
                lambda x: x[0] if len(x) == 1 else x
            )
        return gpd.GeoDataFrame(df, crs=qgis_vector_lyr.crs().toWkt(),
                                geometry='geometry')
