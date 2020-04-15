class Taboo_Client:

    def __init__(self, client_id, taboo_iterations):
        self.client_id = client_id
        self.taboo_iterations = taboo_iterations

    def substract_iteration(self):
        self.taboo_iterations -= 1