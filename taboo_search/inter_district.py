def swap_clients(worst_district, best_district, distance_matrix, taboo_list, current_best_OF_ever):
    clients_apart_from_center_worst_district = [client for client in worst_district.clients if client.id != worst_district.center.id]
    clients_apart_from_center_best_district = [client for client in best_district.clients if client.id != best_district.center.id]
    ordered_clients_worst_district = order_client_list_by_distance_and_demand(clients_apart_from_center_worst_district, distance_matrix)
    ordered_clients_best_district = order_client_list_by_distance_and_demand(clients_apart_from_center_best_district, distance_matrix)
    current_difference = worst_district.value - best_district.value
    
    for tuple_worst_district in ordered_clients_worst_district:
        idx = worst_district.find_client_index(tuple_worst_district[0])
        selected_client_worst_district = worst_district.clients[idx]
        
        for tuple_best_district in ordered_clients_best_district:
            idx = best_district.find_client_index(tuple_best_district[0])
            selected_client_best_district = best_district.clients[idx]

            worst_district.clients.remove(selected_client_worst_district)
            worst_district.clients.append(selected_client_best_district)
            best_district.clients.remove(selected_client_best_district)
            best_district.clients.append(selected_client_worst_district)
            
            worst_district.calculate_value(distance_matrix)
            best_district.calculate_value(distance_matrix)

            candidate_value = abs(worst_district.value - best_district.value)
            is_taboo = False
            for taboo_swap in taboo_list.list:
                if (taboo_swap.client_1_id == tuple_worst_district[0] and taboo_swap.client_2_id == tuple_best_district[0]) or \
                    (taboo_swap.client_1_id == tuple_best_district[0] and taboo_swap.client_2_id == tuple_worst_district[0]):
                    is_taboo = True
                    break

            if candidate_value <= current_best_OF_ever or (not is_taboo and candidate_value <= current_difference):
                taboo_list.update_swap_list(tuple_worst_district[0], tuple_best_district[0])
                return worst_district, best_district, taboo_list, True
            else:
                worst_district.clients.remove(selected_client_best_district)
                worst_district.clients.append(selected_client_worst_district)
                best_district.clients.remove(selected_client_worst_district)
                best_district.clients.append(selected_client_best_district)
    return worst_district, best_district, taboo_list, False





def order_client_list_by_distance_and_demand(client_list, distance_matrix):
    ordered_list = dict()
    clients_length = len(client_list)
    for client in client_list:
        distance_to_other_clients = 0
        for cl in client_list:
            distance_to_other_clients += distance_matrix[client.id - 1][cl.id - 1]
        ordered_list[client.id] = client.demand + distance_to_other_clients / clients_length
    return sorted(ordered_list.items(), key=lambda x:x[1], reverse = True)