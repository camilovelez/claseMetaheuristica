# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:55:44 2020

@author: cvelezg10
"""
import sys
sys.path.append("..")
from client import Client
from district import District
from random import seed
from random import randint

# from utilities import distance_to_centers
import pathlib
import os

def greedy_selection(clients, center, distance_matrix, g, b):
    best_val = 99999999999
    best_index = -1
    for cl in clients:
        distance = distance_matrix[cl.id - 1][center.id - 1]
        value = distance * g + cl.demand * b
        if value < best_val:
            best_val = value
            best_index = clients.index(cl)
    return best_index, best_val


def assign_districts(clients, K, distance_matrix, g, b, selected_seed):
    districts = list()
    seed(selected_seed)
    
    for i in range(K):
        cl = clients[randint(0, K - 1)]
        district = District(i, cl, cl.demand * b)
        districts.append(district)
        clients.remove(cl)
        
    clients.sort(key=lambda cl: cl.demand)
    i = 0
    step = 1
    
    while len(clients) > 0:
        if i == -1:
            i = 0
            step = 1
        elif i == K:
            i = K - 1
            step = -1
            
        greedy_index, value = greedy_selection(clients, districts[i].center, distance_matrix, g, b)
        districts[i].clients.append(clients[greedy_index])
        districts[i].value += value
        del clients[greedy_index]
        
        i += step        
            
    for district in districts:
        district.value /= len(district.clients)
    
    districts.sort(key=lambda di: di.value)
    
    return districts



