import pathlib
import os
from constructive.constructive_heuristic import assign_districts

from utilities import read_instance, distance_matrix, MapVisualiser
from solution import Solution
from taboo_list import Taboo_List
from taboo_element import Taboo_Element


if __name__ == "__main__":
    relative_path = pathlib.Path(__file__).parent.absolute()
    clients = read_instance(os.path.join(relative_path, 'instances', 'instance_small.txt'))
    distance_matrix = distance_matrix(clients)
#    clienta = Client(2, 2, 2, 2)
#    clientb = Client(3, 2, 2, 2)
#    clientc = Client(4, 2, 2, 2)
#    clientd = Client(5, 2, 2, 2)
#    districta = District(1, clientc, 3)
#    districta.clients.append(clienta)
#    districta.clients.append(clientb)
#    districta.clients.append(clientd)
#    districtb = copy.deepcopy(districta)
#    aa = districtb.clients.pop(-1)
#    for client in districta.clients:
#        print(client.id, " gggg")
#    for client in districtb.clients:
#        print(client.id, " ffff")
#        
#    print(aa.id)
#    
##    K = int(len(clients) /10)
#    taboo_list = Taboo_List(5)
#    taboo_list.list.append(Taboo_Element(3,5))
#    taboo_list.list.append(Taboo_Element(4,5))
#    taboo_list.list.append(Taboo_Element(6,5))
#    taboo_list.list.append(Taboo_Element(7,5))
#    for elem in taboo_list.list:
#        if elem.element_id == 4:
#            taboo_list.list.remove(elem)
#             
#    
#    for elem in taboo_list.list:
#        print(elem.element_id)
# #    taboo_list.list = [elem for elem in taboo_list.list if elem.element_id > 4]
#     for elem in taboo_list.list:
#         print(elem.taboo_iterations)
    
#     s = dict()
#     s[0] = 100
#     s[2] = 4500
#     s[3] = 10
#     s[1] = 800
    
#     s = sorted(s.items(), key=lambda x:x[1])
    
    K = 6
    g = 150
    b = 3
    rnd_seed = 0
    districts = assign_districts(clients, K, distance_matrix, g, b, rnd_seed)  
    for district in districts:
        district.best_ever_average_distance = district.calculate_average_distance(distance_matrix)

    solution = Solution(districts)
    mp_v = MapVisualiser()
    mp_v.draw_cluster(solution)
    print(solution.OF)