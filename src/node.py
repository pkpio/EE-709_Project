"""
Authors : Anurag Reddy,
          Praveen Kumar,
          Sharath
Created : 7th April, 2014
Project : ATP Generator
"""

class node:
    def __init__(self):
        self.id = 0
        self.gatetype = 1
        self.level = 0
        self.fanins = 0
        self.cc0_input_order = []
        self.cc1_input_order = []
        self.fanouts = 0
        self.co_output_order = []
        self.co = 0
        self.po = ";"
        self.cc0 = 0
        self.cc1 = 0
