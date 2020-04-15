import pathlib
import os

from constructive.constructive_heuristic import assign_districts
from utilities import read_instance, distance_matrix, MapVisualiser
from solution import Solution
from taboo_search.search_manager import run_search
from client import Client

if __name__ == "__main__":
    relative_path = pathlib.Path(__file__).parent.absolute()
    clients = read_instance(os.path.join(relative_path, 'instances', 'instance_large.txt'))
    distance_matrix = distance_matrix(clients)
    
    aa = Client(1,2,2,10)
    b = Client(2,20,32,10)
    c = Client(3,200,562,10)
    d = Client(4,27,62,10)
    e = Client(5,26,24,10)
    
    client_list = list()
    client_list.append(aa)
    client_list.append(b)
    client_list.append(c)
    client_list.append(d)
    client_list.append(e)

    ordered_list = dict()
    clients_length = len(client_list)
    for client in client_list:
        distance_to_other_clients = 0
        for cl in client_list:
            distance_to_other_clients += distance_matrix[client.id - 1][cl.id - 1]
        ordered_list[client.id] = client.demand + distance_to_other_clients / clients_length
    a= sorted(ordered_list.items(), key=lambda x:x[1], reverse = True)
    
    K = 30
    g = 150
    b = 0
    rnd_seed = 0
    districts = assign_districts(clients, K, distance_matrix, g, b, rnd_seed)  
    for district in districts:
        district.best_ever_average_distance = district.value
        
    print(districts[-1].value - districts[0].value)
    districts, best_OF_ever = run_search(districts,distance_matrix, 50, 10, 10)
    districts.sort(key=lambda di: di.value)
    print(districts[-1].value - districts[0].value)
    solution = Solution(districts)
    mp_v = MapVisualiser()
    mp_v.draw_cluster(solution)
    print(solution.OF)