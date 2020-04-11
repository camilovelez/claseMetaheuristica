def switch_center(district, distance_matrix, taboo_list):
    ordered_clients = order_client_list_by_distance(district.clients, distance_matrix)
    for client_tup in ordered_clients:
        is_taboo = False
        for taboo_element in taboo_list:
            if client_tup[0] == taboo_element.element_id:
                is_taboo = True
                break
        if not is_taboo or client_tup[1] < district.best_ever_average_distance:
            district.center = [client for client in district.clients if client.id == client_tup[0]][0]
            taboo_list.update_list(client_tup[0])
            if client_tup[1] < district.best_ever_average_distance:
                district.best_ever_average_distance = client_tup[1]
            return district, taboo_list
    return district, taboo_list



def order_client_list_by_distance(client_list, distance_matrix):
    ordered_list = dict()
    clients_length = len(client_list)
    for client in client_list:
        distance_to_other_clients = 0
        for cl in client_list:
            distance_to_other_clients += distance_matrix[client.id - 1][cl.id - 1]
        ordered_list[client.id] = distance_to_other_clients / clients_length
    return sorted(ordered_list.items(), key=lambda x:x[1])
        