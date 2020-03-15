import pathlib
import os
from constructive_heuristic import assign_districts

import sys
sys.path.append("..")
from utilities import read_instance, distance_matrix, MapVisualiser
from solution import Solution

if __name__ == "__main__":
    relative_path = pathlib.Path(__file__).parent.absolute()
    clients = read_instance(os.path.join(relative_path, 'instances', 'instance_small.txt'))
    distance_matrix = distance_matrix(clients)
#    K = int(len(clients) /10)
    K = 6
    g = 150
    b = 3
    rnd_seed = 0
    districts = assign_districts(clients, K, distance_matrix, g, b, rnd_seed)  
    solution = Solution(districts)
    mp_v = MapVisualiser()
    mp_v.draw_cluster(solution)
    print(solution.OF)