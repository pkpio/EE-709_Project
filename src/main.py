"""
Authors : Anurag Reddy,
          Praveen Kumar,
          Sharath
Created : 7th April, 2014
Project : ATP Generator
"""

from lev_parser import *

p = lev_parser()
nodes = p.parse('c17.lev')
print nodes[2].id
