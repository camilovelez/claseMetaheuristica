from taboo_element import Taboo_Element

class Taboo_List:

    
    def __init__(self, max_taboo_iterations):
        self.list = list()
        self.max_taboo_iterations = max_taboo_iterations

    def update_list(self, element_id):
        for taboo_element in self.list:
            if taboo_element.element_id == element_id:
                self.list.remove(taboo_element)
                break
            
        for taboo_elem in self.list:
            taboo_elem.substract_iteration()

        self.list = [elem for elem in self.list if elem.taboo_iterations > 0]

        self.list.append(Taboo_Element(element_id, self.max_taboo_iterations))


        

