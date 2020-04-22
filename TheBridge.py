
# -*- coding: utf-8 -*-
"""
defining a bridge 
@author: Pieter Spaepen


Jens: Last edited on 2020-04-04

"""


from node import node
from node import nodeTable
from truss import truss
import numpy as np


""" setting up the list of nodes """

def bridge_JensFinalV2():
    
    
    
    
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 2+16
    turnTrussUpsideDown = False

    #How long should the distance between the nodes on the bottom line be?
    Leng = 50*10**-3
    
    #Diagonal = the length of the elements connecting the top and bottom line of the truss.
    Diagonal = 40*10**-3
    Height = np.sqrt(Diagonal**2-(Leng/2)**2)
    
    #The number of the node where the load attaches
    ForceNodeNr = 17
    #Components of the force of the load    
    Fx = 0
    Fy = -80
   
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1, 101)
    
    #angle of the truss.
    angleTop = 0
    radTop = np.radians(angleTop)
    angleBottom = angleTop
    radBottom = np.radians(angleBottom)
# ===========================================================

    if turnTrussUpsideDown == True:
        inv = -1
    else:
        inv = 1

    ''' setting up the list of nodes '''
   # creating the bottom line of the triangled truss
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    for x in range(1, nodesQuantity):
        if x == ForceNodeNr:
            tempFx = Fx
            tempFy = Fy
        else:
            tempFx = np.nan
            tempFy = np.nan
            
        if x in LockNodeNrs:
            tempDispX = 0
            tempDispY = 0
        else:
            tempDispX = np.nan
            tempDispY = np.nan

        NTble.addNode_to_table(node(x,(x-1)*Leng*np.cos(radBottom),(x-1)*Leng*np.sin(radBottom),tempDispX,tempDispY,tempFx,tempFy))
    
    # creating the top line of the triangled truss
    for x in range(1, nodesQuantity-1):
        tempNr = 21+x
        
        if tempNr == ForceNodeNr:
            tempFx = Fx
            tempFy = Fy
        else:
            tempFx = np.nan
            tempFy = np.nan
            
        if tempNr in LockNodeNrs:
            tempDispX = 0
            tempDispY = 0
        else:
            tempDispX = np.nan
            tempDispY = np.nan

        NTble.addNode_to_table(node(tempNr,(x*Leng-Leng/2)*np.cos(radTop)-inv*Height*np.sin(radTop),inv*Height*np.cos(radTop)+(x*Leng-Leng/2)*np.sin(radTop),tempDispX,tempDispY,tempFx,tempFy))

   
    """ setting up the list of elements """   
    #create an empty truss
    Tr = truss(1)
    #add elements using addElementByNode
    
    for x in range(1, nodesQuantity-1):
        Tr.addElementByNode(NTble,x,x+1)
        
    for x in range(1, nodesQuantity-2):
        Tr.addElementByNode(NTble,21+x,22+x)
            
    for y in range(22, 22 + nodesQuantity - 2):
        Tr.addElementByNode(NTble,y-21,y)
        Tr.addElementByNode(NTble,y-20,y)
        
# === Manually add NODES below ===   

    NTble.addNode_to_table(node(101,0,0.375,0,0,np.nan,np.nan))
    
# === Manually add ELEMENTS below === 

    Tr.addElementByNode(NTble,101,37)
    
    #doubling
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)
    Tr.addElementByNode(NTble,3,4)
# === == == == ==  == == == == ===

    return Tr

