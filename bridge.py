#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:12:03 2020

@author: robbemeyer
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
    NTble.addNode_to_table(node(9,800*10**-3,0,np.nan,np.nan,np.nan,-40))
    NTble.addNode_to_table(node(10,0,100*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(11,100*10**-3,100*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(12,200*10**-3,100*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(13,300*10**-3,100*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(14,400*10**-3,100*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(15,500*10**-3,100*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(16,600*10**-3,100*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(17,700*10**-3,100*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(18,0,300*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(19,175*10**-3,250*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(20,350*10**-3,200*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(21,525*10**-3,150*10**-3,np.nan,np.nan,np.nan,np.nan))
    
    

    
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
    Tr.addElementByNode(NTble,21,17)
    Tr.addElementByNode(NTble,10,2)
    Tr.addElementByNode(NTble,11,2)
    Tr.addElementByNode(NTble,2,12)
    Tr.addElementByNode(NTble,12,3)
    Tr.addElementByNode(NTble,12,4)
    Tr.addElementByNode(NTble,13,4)
    Tr.addElementByNode(NTble,13,5)
    Tr.addElementByNode(NTble,14,5)
    Tr.addElementByNode(NTble,15,5)
    Tr.addElementByNode(NTble,15,6)
    Tr.addElementByNode(NTble,15,7)
    Tr.addElementByNode(NTble,16,7)
    Tr.addElementByNode(NTble,7,17)
    Tr.addElementByNode(NTble,17,8)
    Tr.addElementByNode(NTble,17,9)
   
    
    return Tr