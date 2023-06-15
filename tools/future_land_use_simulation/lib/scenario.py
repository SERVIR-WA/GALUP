from typing import Tuple, Sequence, Dict, Any
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

from .lucis import LandUse


class Neighborhood:
    def __init__(self, lu_codes: Tuple[int]):
        if len(lu_codes) != 9:
            raise ValueError("Neighborhood must have 9 cells in the array.")
        self.landuses = np.array([LandUse(_) for _ in lu_codes])
        self.neighborhood_lu_codes = np.array(lu_codes)

    @property
    def center_cell_lu(self):
        center_cell_lu = self.landuses[4]
        if center_cell_lu.is_water() or center_cell_lu.is_border():
            raise ValueError("Center cell land use can't be water or border.")
        return center_cell_lu

    @property
    def compactness(self):
        if self.center_cell_lu.is_herb():
            return 1
        # change water to border
        self.neighborhood_lu_codes[self.neighborhood_lu_codes == 4] = 0
        n_same_as_center = np.sum(
            self.neighborhood_lu_codes == self.center_cell_lu.lu_code
        )
        n_valid_neighbor = np.count_nonzero(self.neighborhood_lu_codes)
        return (n_same_as_center - 1) / (n_valid_neighbor - 1)


class Scenario:
    def __init__(self, lu_array):
        # this array must contain all cells in a rectangular shape
        self.lu_array = lu_array
        self.n_row, self.n_col = lu_array.shape
        self.mask = np.isin(self.lu_array, [1, 2, 3, 5])
        self.water_indices = np.where(self.lu_array == 4)

    @property
    def n_ag(self):
        return np.count_nonzero(np.isin(self.lu_array, 1))

    @property
    def n_con(self):
        return np.count_nonzero(np.isin(self.lu_array, 2))

    @property
    def n_urb(self):
        return np.count_nonzero(np.isin(self.lu_array, 3))

    @property
    def water_indices_1d(self):
        return self.water_indices[0] * self.n_col + self.water_indices[1]

    def _neighborhoods(self):
        neighborhood_shape = (3, 3)  # a 3x3 neighborhood
        padded_scenario = np.pad(
            self.lu_array, ((1, 1), (1, 1)), "constant", constant_values=0
        )
        strides = padded_scenario.strides + padded_scenario.strides
        neighborhoods = np.lib.stride_tricks.as_strided(
            padded_scenario,
            shape=(
                (padded_scenario.shape[0] - neighborhood_shape[0] + 1,)
                + (padded_scenario.shape[1] - neighborhood_shape[1] + 1,)
                + neighborhood_shape
            ),
            strides=strides,
        ).reshape(self.lu_array.size, 9)
        neighborhoods_no_border_water = neighborhoods[self.mask.reshape(-1)]
        return np.apply_along_axis(
            Neighborhood, axis=1, arr=neighborhoods_no_border_water
        )

    def total_compactness(self):
        return np.sum([_.compactness for _ in self._neighborhoods()])

    def plot(self, data=None, ax=None):
        cmap = colors.ListedColormap(
            ["#FF000000", "#7FFF82", "#064808", "#B40300", "blue", "#A66907"]
        )
        norm = colors.BoundaryNorm([0, 1, 2, 3, 4, 5, 6], cmap.N)
        if data is None:
            data = self.lu_array
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.set_xticks([])
            ax.set_yticks([])
            return ax.pcolor(
                data[::-1], cmap=cmap, norm=norm, 
                dgecolors="k", linewidths=0.5
            )
        else:
            ax.set_xticks([])
            ax.set_yticks([])
            return ax.pcolor(
                data[::-1], cmap=cmap, norm=norm, 
                edgecolors="k", linewidths=0.5
            )
