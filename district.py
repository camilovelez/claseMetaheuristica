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
    
    
