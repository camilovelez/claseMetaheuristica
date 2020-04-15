import copy

from .taboo_list import Taboo_List
from .intra_district import switch_center
from .inter_district import swap_clients

def run_search(districts, distance_matrix, max_iterations, center_taboo_iterations, swap_taboo_iterations):
    client_taboo_list = Taboo_List(center_taboo_iterations)
    swap_taboo_list = Taboo_List(swap_taboo_iterations)
    best_OF_ever = districts[-1].value - districts[0].value
    best_districts_so_far = copy.deepcopy(districts)

    for i in range(max_iterations):
        
        while True:
            worst_district_id = districts[-1].id
            best_district_id = districts[0].id

            districts[-1], client_taboo_list = switch_center(districts[-1], distance_matrix, client_taboo_list)
            districts[0], client_taboo_list = switch_center(districts[0], distance_matrix, client_taboo_list)
            districts.sort(key=lambda di: di.value)
            best_OF_ever, best_districts_so_far = compare_solution(districts, best_OF_ever, best_districts_so_far)

            if worst_district_id == districts[-1].id and best_district_id == districts[0].id:
                break
        
        something_changed = True
        while something_changed:
            districts[-1], districts[0], swap_taboo_list, something_changed = swap_clients(districts[-1], districts[0], distance_matrix, swap_taboo_list, best_OF_ever)
            districts.sort(key=lambda di: di.value)
            best_OF_ever, best_districts_so_far = compare_solution(districts, best_OF_ever, best_districts_so_far)
    return best_districts_so_far, best_OF_ever
            

def compare_solution(districts, best_OF_ever, best_districts_so_far):
    current_OF = districts[-1].value - districts[0].value
    if current_OF < best_OF_ever:
        best_OF_ever = current_OF
        best_districts_so_far = copy.deepcopy(districts)
    return best_OF_ever, best_districts_so_far


