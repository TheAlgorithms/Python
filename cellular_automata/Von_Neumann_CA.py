"""
Von Neumann CA with multi-state fading "heatmap" effect in the terminal.

Requirements: numpy

Rules:
 - Uses Von Neumann neighborhood (4 neighbors).
 - Alive cells follow BIRTH / SURVIVE rules.
 - Dead cells fade out gradually through colored stages.
"""

import numpy as np
import os
import time

# ---------- Configuration ----------
GRID_SIZE = (20, 40)     # (rows, cols)
PROB_ALIVE = 0.25        # initial alive probability
WRAP = True              # wrap edges (toroidal)
BIRTH = {3}              # birth neighbor counts
SURVIVE = {1, 2}         # survival neighbor counts
SLEEP_TIME = 0.1         # seconds between frames
MAX_AGE = 5              # how many steps before a cell fully disappears (0 = dead)
COLORS = {               # Characters & colors for different ages
    0: " ",                          # dead
    1: "\033[92m█\033[0m",           # bright green (newborn)
    2: "\033[93m█\033[0m",           # yellow
    3: "\033[91m█\033[0m",           # red
    4: "\033[31m░\033[0m",           # dim red fading
    5: "\033[90m·\033[0m",           # grey dust
}
# -----------------------------------

def make_initial_grid(shape, prob_alive, seed=None):
    rng = np.random.default_rng(seed)
    alive = (rng.random(shape) < prob_alive).astype(np.uint8)
    return alive.astype(np.uint8) # age 1 for alive, 0 for dead

def count_von_neumann_neighbors(alive_mask, wrap=True):
    """Count Von Neumann neighbors (4 directions)"""
    up     = np.roll(alive_mask, -1, axis=0)
    down   = np.roll(alive_mask,  1, axis=0)
    left   = np.roll(alive_mask, -1, axis=1)
    right  = np.roll(alive_mask,  1, axis=1)
    counts = up + down + left + right

    if not wrap:
        counts[ 0,  :] -= alive_mask[-1,  :]
        counts[-1,  :] -= alive_mask[ 0,  :]
        counts[ :,  0] -= alive_mask[ :, -1]
        counts[ :, -1] -= alive_mask[ :,  0]
        counts = np.clip(counts, 0, 4)

    return counts

def step(age_grid, birth=BIRTH, survive=SURVIVE, wrap=WRAP, max_age=MAX_AGE):
    alive_mask = age_grid > 0
    neighbor_counts = count_von_neumann_neighbors(alive_mask.astype(np.uint8), wrap=wrap)

    born_mask = (~alive_mask) & np.isin(neighbor_counts, list(birth))
    survive_mask = alive_mask & np.isin(neighbor_counts, list(survive))

    new_age_grid = age_grid.copy()

    # Alive cells that survive get age reset to 1 if born, else age increment
    new_age_grid[born_mask] = 1
    new_age_grid[survive_mask & alive_mask] = 1 # reset alive age for fresh color

    # Fade out dead cells
    fade_mask = (~born_mask) & (~survive_mask)
    new_age_grid[fade_mask & (new_age_grid > 0)] += 1
    new_age_grid[new_age_grid > max_age] = 0 # fully dead

    return new_age_grid

def display(age_grid):
    """Render grid with colors for each age stage"""
    os.system("cls" if os.name == "nt" else "clear")
    for row in age_grid:
        print("".join(COLORS.get(age, COLORS[MAX_AGE]) for age in row))

def main():
    grid = make_initial_grid(GRID_SIZE, prob_alive=PROB_ALIVE)

    try:
        while True:
            display(grid)
            grid = step(grid, birth=BIRTH, survive=SURVIVE, wrap=WRAP, max_age=MAX_AGE)
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
