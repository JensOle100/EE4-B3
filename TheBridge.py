
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
def bridge_150cm():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 5

    #How long should the distance between the nodes on the bottom line be?
    Leng = 280*10**-3
    
    #Distance between top and bottom line
    Height =  np.sqrt(Leng**2-(Leng/2)**2)
    
    #The number of the node where the load attaches
    ForceNodeNr = 101
    
    #Components of the force of the load    
    Fx = 0
    Fy = -60
    
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1)
    
    #angle of the truss.
    angle = 30
    th = np.radians(angle)
# ===========================================================


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

        NTble.addNode_to_table(node(x,(x-1)*Leng*np.cos(th),(x-1)*Leng*np.sin(th),tempDispX,tempDispY,tempFx,tempFy))
    
    
    # creating the top line of the triangled truss
    for x in range(1, nodesQuantity-1):
        tempNr = 21+x
        
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

        NTble.addNode_to_table(node(tempNr,(x*Leng-Leng/2)*np.cos(th)-Height*np.sin(th),Height*np.cos(th)+(x*Leng-Leng/2)*np.sin(th),tempDispX,tempDispY,tempFx,tempFy))    

   
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
    NTble.addNode_to_table(node(101,0.8,0.6,np.nan,np.nan,Fx,Fy))


# === Manually add ELEMENTS below ===   
    Tr.addElementByNode(NTble,101,4)
    Tr.addElementByNode(NTble,101,24)

    Tr.addElementByNode(NTble,22,23)
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)
# === == == == ==  == == == == ===
        
    return Tr