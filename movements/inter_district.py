import copy

def insert_client(original_district, other_districts, distance_matrix, taboo_list):
    clients_apart_from_center = [client for client in original_district.clients if client.id != original_district.center.id]
    ordered_clients = order_client_list_by_distance_and_demand(clients_apart_from_center, distance_matrix)
    
    for client_tup in ordered_clients:
        is_taboo = False
        for taboo_element in taboo_list:
            if client_tup[0] == taboo_element.element_id:
                is_taboo = True
                break
        copy_of_original_district = copy.deepcopy(original_district)
        idx = copy_of_original_district.find_client_index(client_tup[0])
        selected_client = copy_of_original_district.clients.pop(idx)
        value_copy_of_original_district = copy_of_original_district.calculate_value(distance_matrix)
        
        for other_district in other_districts:
            current_value = original_district.value + other_district.value
            copy_of_other_district = copy.deepcopy(other_district)
            copy_of_other_district.clients.append(selected_client)
            value_copy_of_other_district = copy_of_other_district.calculate_value(distance_matrix)
            does_it_worsen = value_copy_of_original_district + value_copy_of_other_district <= current_value

            if not does_it_worsen and not is_taboo:
                original_district.clients.remove(selected_client)
                other_district.clients.append(selected_client)
                taboo_list.update_list(selected_client.id)
                return original_district, other_districts, taboo_list
    return original_district, other_districts, taboo_list





def order_client_list_by_distance_and_demand(client_list, distance_matrix):
    ordered_list = dict()
    clients_length = len(client_list)
    for client in client_list:
        distance_to_other_clients = 0
        for cl in client_list:
            distance_to_other_clients += distance_matrix[client.id - 1][cl.id - 1]
        ordered_list[client.id] = client.demand + distance_to_other_clients / clients_length
    return sorted(ordered_list.items(), key=lambda x:x[1], reverse = True)