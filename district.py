# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:51:39 2020

@author: cvelezg10
"""

class District:


    def __init__(self, id, center, value):
        self.id = id
        self.clients = list()
        self.clients.append(center)
        self.center = center
        self.value = value
        self.best_ever_average_distance = 99999999
        self.best_ever_value = 99999999

    def calculate_average_distance(self, distance_matrix):
        distance = 0
        for client in self.clients:
            distance += distance_matrix[client.id - 1][self.center.id - 1]
        return distance / len(self.clients)

    def calculate_value(self, distance_matrix):
        value = 0
        for client in self.clients:
            value += distance_matrix[client.id - 1][self.center.id - 1] + client.demand
        return value / len(self.clients)
    
    def find_client_index(self, target_id):
        index = -1
        for idx, client in enumerate(self.clients):
            if client.id == target_id:
                index = idx
        return index