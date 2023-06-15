from functools import partial

import numpy as np
import pandas as pd

import scoop
import deap.creator
import deap.base
import deap.tools
import jenkspy

from .scenario import Scenario
from . import config
# from .config import *
from .lucis import LandUse


# -------------------------Initialization---------------------- #
def nb_classify(sr, num_class=3):
    breaks = jenkspy.jenks_breaks(sr, n_classes=num_class)
    return pd.Series(
        pd.cut(
            sr, 
            bins=breaks, 
            labels=np.arange(1, num_class + 1), 
            include_lowest=True
        ),
        dtype="int",
    )


def random_scn(df, landuse, lu_col, n=3000):
    df = config.base_df
    n = config.INIT_SAMPLE_SIZE
    lu_col = config.CURRENT_LU
    print(df)
    print('above is df')
    print(config.base_df)
    print('above is config.base_df')
    if landuse == 0:  # copy the original scenario
        return df[lu_col].values
    if n > len(df) * 0.5:
        raise ValueError("n must be less than half of the dataframe size.")
    lu = LandUse(landuse)
    if lu.lu_code == 1:
        prob_dict = config.INIT_PROB_AG
    elif lu.lu_code == 2:
        prob_dict = config.INIT_PROB_CON
    elif lu.lu_code == 3:
        prob_dict = config.INIT_PROB_URB
    else:
        raise ValueError("landuse must be 1 (ag), 2 (con), or 3 (urb).")
    suit_col = lu.lu_abbr + "_suit"
    nbc_sr = nb_classify(df.loc[df[lu_col] != lu.lu_code, suit_col])
    prob_sr = pd.Series(prob_dict) / nbc_sr.value_counts()

    lu_sample = np.random.choice(
        nbc_sr.index.values,
        size=n,  # this can be changed depending on size of the scenario
        replace=False,
        p=nbc_sr.map(prob_sr),
    )
    scenario = df[lu_col].copy()
    scenario.iloc[lu_sample] = lu.lu_code
    return scenario.values


# -------------------------Crossover---------------------- #
def cx_grid(ind1, ind2, n_row=30, n_col=30, indpb=0.5):
    """customize crossover. crossover between 3x3 grid in ind1 and ind2.
    iff the center cell's land use is the same with at least one of the
    neighbors in the other individual's center cell.
    """
    cx_size = round(indpb * n_row * n_col)
    cx_position_1d = np.random.choice(len(ind1), cx_size, replace=False)
    cx_ir = cx_position_1d // n_col
    cx_ic = cx_position_1d % n_col
    # cx_ir = [1, 3, 1, 4]  # example row index
    # cx_ic = [1, 4, 0, 0]  # example column index
    ind1 = ind1.reshape((n_row, n_col))
    ind2 = ind2.reshape((n_row, n_col))
    ind1_padded = np.pad(ind1, ((1, 1), (1, 1)), "constant", constant_values=0)
    ind2_padded = np.pad(ind2, ((1, 1), (1, 1)), "constant", constant_values=0)
    for r, c in zip(cx_ir, cx_ic):
        ind1_change = False
        ind2_change = False
        if ind1[r, c] in ind2_padded[r : r + 3, c : c + 3]:
            ind2_change = ind1[r, c]
        if ind2[r, c] in ind1_padded[r : r + 3, c : c + 3]:
            ind1_change = ind2[r, c]
        if ind1_change:
            ind1[r, c] = ind1_change
        if ind2_change:
            ind2[r, c] = ind2_change
    return ind1.reshape(-1), ind2.reshape(-1)


# -------------------------Mutation---------------------- #
def mut_grid(ind, n_row=30, n_col=30, lu_in=(3,), lu_ex=(1,), indpb=0.1):
    """customize mutation. randomly select cells lu_in (inadequate land uses)
    with probability of indpb. convert selected and the surrounding neighbors
    (3x3 grid) to a land use randomly selected from lu_ex (excessive land uses)
    """
    mut_size = round(indpb * n_row * n_col)
    lu_ex_i = np.where(np.isin(ind, lu_ex))[0]
    if mut_size > len(lu_ex_i):
        mut_size = len(lu_ex_i)
    mut_i = np.random.choice(lu_ex_i, mut_size)
    mut_ir = mut_i // n_col
    mut_ic = mut_i % n_col
    # mut_ir = [1, 3]  # example row index
    # mut_ic = [1, 4]  # example column index

    ind_padded = np.pad(
        ind.reshape((n_row, n_col)), 
        ((1, 1), (1, 1)), 
        "constant", 
        constant_values=0
    )
    for r, c in zip(mut_ir, mut_ic):
        ind_padded[r : r + 3, c : c + 3] = np.random.choice(lu_in, 1)[0]

    ind[:] = ind_padded[1 : n_row + 1, 1 : n_col + 1].reshape(-1)
    return (ind,)



# -------------------------Evaluation (Fitness)---------------------- #
def get_ag_suit(base_df):    
    return base_df[config.AG_SUIT]


def get_con_suit(base_df):
    return base_df[config.CON_SUIT]


def get_urb_suit(base_df):
    return base_df[config.URB_SUIT]


def get_current_lu(base_df):
    return base_df[config.CURRENT_LU]


def evaluate(individual):
    individual = individual[0]
    scn = Scenario(individual.reshape(config.GRID_R, config.GRID_C))
    p = 4  # penalty coefficient
    grid_size = config.GRID_R * config.GRID_C

    # ------------------------ additive objective ------------------------ #
    # 1. conflict: minimize conflict due to allocating urban cells
    allocate_conf = np.sum(config.base_df["urban_conflict"][individual == 3])
    # minimize conflict
    f_conf = (allocate_conf - config.min_conf) / (config.max_conf - config.min_conf)

    # 2. suitability: maximize suitability for ag, con, and urb
    min_suit = grid_size
    max_suit = 9 * grid_size
    allocate_suit = (
        np.sum(get_ag_suit(config.base_df)[individual == 1])
        + np.sum(get_con_suit(config.base_df)[individual == 2])
        + np.sum(get_urb_suit(config.base_df)[individual == 3])
    )
    # maximize suitability
    f_suit = (allocate_suit - max_suit) / (min_suit - max_suit)

    # -------------------------spatial objective------------------------- #
    min_comp = 0
    max_comp = grid_size
    allocate_compact = scn.total_compactness()
    # maximize compactness
    f_spa = (allocate_compact - max_comp) / (min_comp - max_comp)

    # --------------------------constraints------------------------------ #
    # 1. Temperature: calculate temperature difference
    temp_slope = pd.Series(
        (
            config.TEMP_PER_AG, 
            config.TEMP_PER_CON, 
            config.TEMP_PER_URB, 
            config.TEMP_PER_WATER, 
            config.TEMP_PER_HERB
        ),
        index=np.arange(1, 6),
    )
    num_lu_diff = (
        pd.Series(individual).value_counts()
        - get_current_lu(config.base_df).value_counts()
    )
    temp_diff = num_lu_diff @ temp_slope  # dot product
    if temp_diff == 0:
        temp_constraint = 0
    else:
        temp_constraint = max([0, temp_diff - config.TEMP_TARGET]) ** 2

    # 2. Population: number of urban cells
    # old_urb_cell = (current_lu_sr == 3)
    urb_cell = np.sum(individual == 3)
    urb_cell_needed = int(np.ceil((config.PPL_GROWTH + config.PPL_CURRENT) / config.PPL_PER_URB))
    pop_constraint = max([0, urb_cell_needed - urb_cell]) ** 2
    
    # fitness value
    return (
        (f_conf**p) * (f_spa**p)
        + (f_suit**p) * (f_spa**p)
        + temp_constraint
        + pop_constraint,
    )


# -------------------------GA configurations---------------------------- #

try:
    del deap.creator.FitnessMin
except:
    pass

try:
    del deap.creator.Individual
except:
    pass

deap.creator.create("FitnessMin", deap.base.Fitness, weights=(-1.0,))
deap.creator.create("Individual", list, fitness=deap.creator.FitnessMin)

toolbox = deap.base.Toolbox()

toolbox.register("map", scoop.futures.map)

toolbox.register(
    "init_random_scn", 
    random_scn,
    df=config.base_df,
    landuse=np.random.choice(4, p=[0.4, 0.2, 0.2, 0.2]),
    lu_col=config.CURRENT_LU,
    n=config.INIT_SAMPLE_SIZE,
)

toolbox.register(
    "individual", 
    deap.tools.initRepeat, 
    deap.creator.Individual, 
    toolbox.init_random_scn,
    n=1  # toolbox.init_random_scn returns a list of size 1
)

toolbox.register(
    "population", 
    deap.tools.initRepeat, 
    list, 
    toolbox.individual
)
toolbox.register("evaluate", evaluate)

toolbox.register("mate", cx_grid, n_row=config.GRID_R, n_col=config.GRID_C, indpb=0.5)
toolbox.register(
    "mutate",
    mut_grid,
    n_row=config.GRID_R,
    n_col=config.GRID_C,
    lu_in=config.LU_INSUFFICIENT,
    lu_ex=config.LU_EXCESS,
    indpb=0.1,
)
toolbox.register("select", deap.tools.selTournament, tournsize=3)  # Selection


def main():
    pop = toolbox.population(n=config.POP_SIZE)
    
    hof = deap.tools.HallOfFame(1, similar=np.array_equal)
    hof.clear()
    # Evaluate the entire population
    fitnesses = list(toolbox.map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # base scenario
    base_scn = Scenario(get_current_lu(config.base_df).values.reshape(config.GRID_R, config.GRID_C))

    g = 0

    while g < config.GEN_NUM:
        g += 1
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals to avoid modifying the original
        # this uses the `copy.deepcopy()` function
        offspring = list(toolbox.map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if np.random.rand() < config.CXPB:
                toolbox.mate(child1[0], child2[0])
                # set water cells back to water
                child1[0][base_scn.water_indices_1d] = 4
                child2[0][base_scn.water_indices_1d] = 4
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if np.random.rand() < config.MUTPB:
                toolbox.mutate(mutant[0])
                # set water cells back to water
                mutant[0][base_scn.water_indices_1d] = 4
                del mutant.fitness.values

        # recalculate fitness for (crossed or mutated) individuals
        # i.e., those with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]

        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        pop[:] = offspring
        hof.update(offspring)

        fits = [ind.fitness.values[0] for ind in pop]

        if g % 10 == 0:
            print(f"gen {g}: {min(fits)}, {max(fits)}, {np.mean(fits)}")

    return hof[0]
