import pathlib
import os

from constructive.constructive_heuristic import assign_districts
from utilities import read_instance, distance_matrix, MapVisualiser
from solution import Solution
from taboo_search.search_manager import run_search

if __name__ == "__main__":
    relative_path = pathlib.Path(__file__).parent.absolute()
    clients = read_instance(os.path.join(relative_path, 'instances', 'instance_small.txt'))
    distance_matrix = distance_matrix(clients)
    K = 6
    g = 150
    b = 3
    rnd_seed = 0
    
    districts = assign_districts(clients, K, distance_matrix, g, b, rnd_seed)  
    for district in districts:
        district.best_ever_average_distance = district.value
        
    print("solucion constructivo %s" %(districts[-1].value - districts[0].value))
    iterClientes = 5
    iterSwap = 25
    districts, best_OF_ever = run_search(districts,distance_matrix, 50, iterClientes, iterSwap)
    districts.sort(key=lambda di: di.value)
    solution = Solution(districts)
    mp_v = MapVisualiser()
    mp_v.draw_cluster(solution)
    print("solucion TS clientes %s, swap %s, FO %s" %(iterClientes, iterSwap, solution.OF))