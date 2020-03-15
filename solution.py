class Solution:
    def __init__(self, districts):
        self.districts = districts
        self.OF = districts[-1].value - districts[0].value