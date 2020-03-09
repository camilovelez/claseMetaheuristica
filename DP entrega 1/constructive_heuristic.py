# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:55:44 2020

@author: cvelezg10
"""

from client import Client
from district import District
from random import seed
from random import randint


def greedy_selection(clients, center, g, b):
    best_val = 99999999999
    best_index = -1
    for cl in clients:
        distance = ((cl.longitude - center.longitude) ** 2 + (cl.latitude - center.latitude) ** 2) ** 0.5
        value = distance * g + cl.demand * b
        if value < best_val:
            best_val = value
            best_index = clients.index(cl)
    return best_index, best_val


def constructive_heuristic(clients, K, g, b):
    districts = list()
    seed(0)
    
    for i in range(K):
        cl = clients[randint(0, K - 1)]
        districts[i].center = cl
        districts[i].clients.append(cl)
        districts[i].value += cl.demand * b
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
            
        greedy_index, value = greedy_selection(clients, districts[i].center, g, b)
        districts[i].clients.append(clients[greedy_index])
        districts[i].value += value
        del clients[greedy_index]
        
        i += step        
            
    for district in districts:
        district.value /= len(district.clients)
    
    districts.sort(key=lambda di: di.value)
    
    return districts



