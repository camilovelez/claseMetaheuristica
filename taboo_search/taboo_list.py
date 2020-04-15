from .taboo_client import Taboo_Client
from .taboo_swap import Taboo_Swap

class Taboo_List:

    
    def __init__(self, max_taboo_iterations):
        self.list = list()
        self.max_taboo_iterations = max_taboo_iterations

    def update_client_list(self, client_id):
        for taboo_client in self.list:
            if taboo_client.client_id == client_id:
                self.list.remove(taboo_client)
            else:
                taboo_client.substract_iteration()            

        self.list = [client for client in self.list if client.taboo_iterations > 0]

        self.list.append(Taboo_Client(client_id, self.max_taboo_iterations))

    def update_swap_list(self, client_1_id, client_2_id):
        for taboo_swap in self.list:
            if (taboo_swap.client_1_id == client_1_id and taboo_swap.client_2_id == client_2_id) or \
                (taboo_swap.client_1_id == client_2_id and taboo_swap.client_2_id == client_1_id):

                self.list.remove(taboo_swap)
            else:
                taboo_swap.substract_iteration()            

        self.list = [swap for swap in self.list if swap.taboo_iterations > 0]

        self.list.append(Taboo_Swap(client_1_id, client_2_id, self.max_taboo_iterations))


        

