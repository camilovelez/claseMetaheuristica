class Taboo_Element:

    def __init__(self, element_id, taboo_iterations):
        self.element_id = element_id
        self.taboo_iterations = taboo_iterations

    def substract_iteration(self):
        self.taboo_iterations -= 1