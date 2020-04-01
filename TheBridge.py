# -*- coding: utf-8 -*-
"""


@author: Stijn
"""

# -*- coding: utf-8 -*-
"""
defining a bridge 

@author: Pieter Spaepen
"""
from node import node
from node import nodeTable
from truss import truss
import numpy as np


""" 
first bridge attempt
"""

""" setting up the list of nodes """
def bridge_150cm():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,150*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,300*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,450*10**-3,0,np.nan,np.nan,np.nan,-20))
    NTble.addNode_to_table(node(5,600*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(6,750*10**-3,0,np.nan,np.nan,np.nan,0))
    NTble.addNode_to_table(node(7,900*10**-3,0,np.nan,np.nan,np.nan,-20))
    NTble.addNode_to_table(node(8,1050*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(9,1200*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(10,1350*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(11,1500*10**-3,0,np.nan,0,np.nan,np.nan))
    NTble.addNode_to_table(node(22,(150-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(23,(300-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(24,(450-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(25,(600-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(26,(750-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(27,(900-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(28,(1050-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(29,(1200-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(30,(1350-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(31,(1500-75)*10**-3,np.sqrt(150**2-75**2)*10**-3,np.nan,np.nan,np.nan,np.nan))

    
    
    """ setting up the list of elements """
    
    #create an empty truss
    Tr = truss(1)
    #add elements using addElementByNode
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)
    Tr.addElementByNode(NTble,3,4)
    Tr.addElementByNode(NTble,4,5)
    Tr.addElementByNode(NTble,5,6)
    Tr.addElementByNode(NTble,6,7)
    Tr.addElementByNode(NTble,7,8)
    Tr.addElementByNode(NTble,8,9)
    Tr.addElementByNode(NTble,9,10)
    Tr.addElementByNode(NTble,10,11)
    Tr.addElementByNode(NTble,22,23)
    Tr.addElementByNode(NTble,23,24)
    Tr.addElementByNode(NTble,24,25)
    Tr.addElementByNode(NTble,25,26)
    Tr.addElementByNode(NTble,26,27)
    Tr.addElementByNode(NTble,27,28)
    Tr.addElementByNode(NTble,28,29)
    Tr.addElementByNode(NTble,29,30)
    Tr.addElementByNode(NTble,30,31)
    Tr.addElementByNode(NTble,1,22)
    Tr.addElementByNode(NTble,22,2)
    Tr.addElementByNode(NTble,2,23)
    Tr.addElementByNode(NTble,23,3)
    Tr.addElementByNode(NTble,3,24)
    Tr.addElementByNode(NTble,24,4)
    Tr.addElementByNode(NTble,4,25)
    Tr.addElementByNode(NTble,25,5)
    Tr.addElementByNode(NTble,5,26)
    Tr.addElementByNode(NTble,26,6)
    Tr.addElementByNode(NTble,6,27)
    Tr.addElementByNode(NTble,27,7)
    Tr.addElementByNode(NTble,7,28)
    Tr.addElementByNode(NTble,28,8)
    Tr.addElementByNode(NTble,8,29)
    Tr.addElementByNode(NTble,29,9)
    Tr.addElementByNode(NTble,9,30)
    Tr.addElementByNode(NTble,30,10)
    Tr.addElementByNode(NTble,10,31)
    Tr.addElementByNode(NTble,31,11)
    
    return Tr
