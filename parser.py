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
      

#### Functions ####
def parseLineToNode(l):
    params = l.split(" ")
    n = node()
    n.id = int(params[0])
    n.gatetype = int(params[1])
    n.level = int(params[2])
    n.fanins = int(params[3])

    #cc0, cc1 end index
    cc0_end_index = n.fanins + 4;
    cc1_end_index = 2 * n.fanins + 4;
    n_fanouts_index = cc1_end_index;

    #Adding cc0, cc1 lists
    for i in range(4, cc0_end_index):
        n.cc0_input_order.append(int(params[i]))

    for i in range(cc0_end_index, cc1_end_index):
        n.cc1_input_order.append(int(params[i]))

    #fanouts value
    n.fanouts = int(params[n_fanouts_index])

    #co_output index
    co_end_index = n_fanouts_index + 1 + n.fanouts

    #Adding co_output list
    for i in range(n_fanouts_index + 1, co_end_index):
        n.co_output_order.append(int(params[i]))

    #Setting remaining params - co, po, cc0, cc1
    n.co = int(params[co_end_index])
    n.po = params[co_end_index + 1]
    n.cc0 = int(params[co_end_index + 2])
    n.cc1 = int(params[co_end_index + 3])
    
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
        nodes[i] = parseLineToNode(lines[i+2])
        print nodes[i].cc1

