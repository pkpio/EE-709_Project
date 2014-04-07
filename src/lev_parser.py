"""
Authors : Anurag Reddy,
          Praveen Kumar,
          Sharath
Created : 7th April, 2014
Project : ATP Generator
"""
from node import *

class lev_parser:
    def __init__(self):
        pass

    def parse(self, lev_file):
        #Read .lev file into an array of lines
        f = open(lev_file)
        lines = f.readlines()
        f.close()
        
        #find nodes count
        nodecount = int(lines[0]) - 1

        #Make a list of nodes
        nodes = [ node() for i in range(nodecount)]

        #Parse nodes
        if(len(lines) < nodecount + 2):
            print 'Invalid file format. Expecting ',nodecount + 2,' lines.'
        else:
            for i in range(nodecount):
                nodes[i] = self.parseLineToNode(lines[i+2])

        return nodes        
    
    def parseLineToNode(self, line):
        params = line.split(" ")
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
