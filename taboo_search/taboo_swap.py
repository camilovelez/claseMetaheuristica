class Taboo_Swap:

    def __init__(self, client_1_id, client_2_id, taboo_iterations):
        self.client_1_id = client_1_id
        self.client_2_id = client_2_id
        self.taboo_iterations = taboo_iterations

    def substract_iteration(self):
        self.taboo_iterations -= 1