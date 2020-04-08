# -*- coding: utf-8 -*-
"""
defining a bridge 
@author: Stijn Peeters
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
    NTble.addNode_to_table(node(9,800*10**-3,0,np.nan,np.nan,np.nan,-20))
    NTble.addNode_to_table(node(10,50*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(11,150*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(12,250*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(13,350*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(14,450*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(15,550*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(16,650*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(17,750*10**-3,np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(18,100*10**-3,2*np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(19,200*10**-3,2*np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(20,300*10**-3,2*np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(21,400*10**-3,2*np.sqrt(100**2-50**2)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(22,0,100*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(23,0,200*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(24,0,300*10**-3,0,0,np.nan,np.nan))
    

    
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
    Tr.addElementByNode(NTble,10,11)
    Tr.addElementByNode(NTble,11,12)
    Tr.addElementByNode(NTble,12,13)
    Tr.addElementByNode(NTble,13,14)
    Tr.addElementByNode(NTble,14,15)
    Tr.addElementByNode(NTble,15,16)
    Tr.addElementByNode(NTble,16,17)
    Tr.addElementByNode(NTble,18,19)
    Tr.addElementByNode(NTble,19,20)
    Tr.addElementByNode(NTble,20,21)
    Tr.addElementByNode(NTble,1,10)
    Tr.addElementByNode(NTble,2,10)
    Tr.addElementByNode(NTble,2,11)
    Tr.addElementByNode(NTble,3,11)
    Tr.addElementByNode(NTble,3,12)
    Tr.addElementByNode(NTble,4,12)
    Tr.addElementByNode(NTble,4,13)
    Tr.addElementByNode(NTble,5,13)
    Tr.addElementByNode(NTble,5,14)
    Tr.addElementByNode(NTble,6,14)
    Tr.addElementByNode(NTble,6,15)
    Tr.addElementByNode(NTble,7,15)
    Tr.addElementByNode(NTble,7,16)
    Tr.addElementByNode(NTble,8,16)
    Tr.addElementByNode(NTble,8,17)
    Tr.addElementByNode(NTble,9,17)
    Tr.addElementByNode(NTble,3,11)
    Tr.addElementByNode(NTble,10,18)
    Tr.addElementByNode(NTble,11,18)
    Tr.addElementByNode(NTble,11,19)
    Tr.addElementByNode(NTble,12,19)
    Tr.addElementByNode(NTble,12,20)
    Tr.addElementByNode(NTble,13,20)
    Tr.addElementByNode(NTble,13,21)
    Tr.addElementByNode(NTble,14,21)
    Tr.addElementByNode(NTble,10,22)
    Tr.addElementByNode(NTble,10,23)
    Tr.addElementByNode(NTble,18,23)
    Tr.addElementByNode(NTble,18,24)
    
    return Tr
