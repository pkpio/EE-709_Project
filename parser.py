"""
Authors : Anurag Reddy,
          Praveen Kumar,
          Sharath
Created : 7th April, 2014
Project : ATP Generator
"""

#Data type definitions
class node:
    def __init__(self):
        self.id = 0
        self.gatetype = 1
        self.fanins = 0
        self.cc0_input_order = []
        self.cc1_input_order = []
        self.fanouts = 0
        self.co_output_order = []
        self.co = 0
        self.po = ";"
        self.cc0 = 0
        self.cc1 = 0
      

#### Functions ####
def parseLineToNode(l, n):
    print l[1]
    return n


#Read .lev file into an array of lines
f = open('c17.lev')
lines = f.readlines()
f.close()

#Parse nodes count
global nodecount
nodecount = int(lines[0]) - 1

#Parse nodes
if(len(lines) < nodecount + 2):
    print 'Invalid file format. Expecting ',nodecount + 2,' lines.'
else:
    global nodes
    nodes = [ node() for i in range(nodecount)]

    for i in range(nodecount):
        nodes[i] = parseLineToNode(lines[i+2], nodes[i])

