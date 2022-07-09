from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy as np
import argparse

# Select difference mode to view path finding results
MODES = ["Phase1","Phase2"]

# Create a 10x10 map using a 2D-list
# Any value smaller or equal to 0 describes an obstacle. Any number bigger than 0 describes[] the weight of a field that can be walked on.
size = (10,10)
matrix = np.ones(size)
# Create a list of tuples for storing the location of obstacles
obstacles = []

# Function to genrate a number of random coordinates that are not occupied by any obstacles, start or end coordinates
def generate_random_coordinates(num_random_cords):
    random_cords = []
    not_in_occupied_cord = True
    occupied_cords = obstacles + [(0,0),(9,9)]

    while len(random_cords)!=num_random_cords:
        x = np.random.randint(0,10)
        y = np.random.randint(0,10)
        not_in_occupied_cord = all([1 if (x,y)!=occupied_cord else 0 for occupied_cord in occupied_cords])
        if not_in_occupied_cord:
            random_cords.append((x,y))

    return random_cords

def print_shortest_path(mode):
    ########################################
    ############### Phase 1 ################
    ########################################
    if mode == "Phase1":
        obstacles = [(9,7),(8,7),(6,7),(6,8)]

    ########################################
    ############### Phase 2 ################
    ########################################
    elif mode == "Phase2":
        obstacles = generate_random_coordinates(20) + [(9,7),(8,7),(6,7),(6,8)]
    
    for o in obstacles:
        matrix[o] = 0

    # Create a new grid from this map representation
    # This will create Node instances for every element of our map. It will also set the size of the map.
    grid = Grid(matrix=matrix)

    # Define the start (top-left) and endpoint (bottom-right) from the map
    start = grid.node(0, 0)
    end = grid.node(9, 9)

    # Use A* algorithm to find the shortest path from start to end
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)

    if path!=[]:   
        print(f'Path: {path}')
        print(f'Number of Steps: {runs-1}')
    else:
        print("Unable to reach delivery point!")
    # print(grid.grid_str(path=path, start=start, end=end))   # Print the map with the path drawn on it




def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', nargs=1, type=str, help='Running mode. Must be one of the following modes: {}'.format(MODES))
    
    args = parser.parse_args()
    mode = args.mode[0]
    
    return args, mode

if __name__ == '__main__':
    args, mode = parse_args() # get argument from the command line

    # select mode
    print(f'selected mode: {mode}')
    if mode == "Phase1":
        print_shortest_path(mode)
    elif mode == "Phase2":
        print_shortest_path(mode)
    else:
        print("Usage: Must be one of the following modes: {}".format(MODES))
        exit(1)