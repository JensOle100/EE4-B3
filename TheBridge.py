# -*- coding: utf-8 -*-
"""


@author: Pieter Spaepen
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
    NTble.addNode_to_table(node(2,100*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,200*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,300*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(5,400*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(6,500*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(7,600*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(8,700*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(9,800*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(10,900*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(11,1000*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(12,1100*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(13,1200*10**-3,0,np.nan,0,np.nan,np.nan))
    
    
    
    
    #NTble.addNode_to_table(node(11,1000*10**-3,0,np.nan,0,np.nan,np.nan))
    
    
    
    NTble.addNode_to_table(node(22,(100-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(23,(200-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(24,(300-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(25,(400-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(26,(500-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(27,(600-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(28,(700-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(29,(800-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,100))
    NTble.addNode_to_table(node(30,(900-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,100))
    NTble.addNode_to_table(node(31,(1000-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(32,(1100-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(33,(1200-50)*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    
    
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
    Tr.addElementByNode(NTble,11,12)
    Tr.addElementByNode(NTble,12,13)
    
    Tr.addElementByNode(NTble,22,23)
    Tr.addElementByNode(NTble,23,24)
    Tr.addElementByNode(NTble,24,25)
    Tr.addElementByNode(NTble,25,26)
    Tr.addElementByNode(NTble,26,27)
    Tr.addElementByNode(NTble,27,28)
    Tr.addElementByNode(NTble,28,29)
    Tr.addElementByNode(NTble,29,30)
    Tr.addElementByNode(NTble,30,31)
    Tr.addElementByNode(NTble,31,32)
    Tr.addElementByNode(NTble,32,33)
    
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
    
    Tr.addElementByNode(NTble,11,32)
    Tr.addElementByNode(NTble,32,12)
    Tr.addElementByNode(NTble,12,33)
    Tr.addElementByNode(NTble,33,13)
    
    return Tr
