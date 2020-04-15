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
First bridge attempt
"""

""" setting up the list of nodes """
def bridge_v1():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,20*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,40*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,60*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(5,80*10**-3,0,np.nan,np.nan,np.nan,-40))
    NTble.addNode_to_table(node(6,60*10**-3,0.25*30*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(7,40*10**-3,0.5*30*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(8,20*10**-3,0.75*30*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(9,0,30*10**-3,0,0,np.nan,np.nan))
    
 
    
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
    Tr.addElementByNode(NTble,1,8)
    Tr.addElementByNode(NTble,2,8)
    Tr.addElementByNode(NTble,3,8)
    Tr.addElementByNode(NTble,3,7)
    Tr.addElementByNode(NTble,3,6)
    Tr.addElementByNode(NTble,4,6)
  
    return Tr

""" 
Second bridge attempt
"""

""" setting up the list of nodes """
def bridge_v2():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,20*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,40*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,60*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(5,80*10**-3,0,np.nan,np.nan,np.nan,-40))
    NTble.addNode_to_table(node(6,60*10**-3,0.25*30*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(7,40*10**-3,0.5*30*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(8,20*10**-3,0.75*30*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(9,0,30*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(10,0,16*10**-3,0,0,np.nan,np.nan))
    
 
    
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
    Tr.addElementByNode(NTble,1,8)
    Tr.addElementByNode(NTble,2,8)
    Tr.addElementByNode(NTble,3,8)
    Tr.addElementByNode(NTble,3,7)
    Tr.addElementByNode(NTble,3,6)
    Tr.addElementByNode(NTble,4,6)
    Tr.addElementByNode(NTble,10,5)
      
    return Tr

""" 
Third bridge attempt
"""

""" setting up the list of nodes """
def bridge_v3():
    """ setting up the list of nodes """
       # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,14*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,20*10**-3,14*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,40*10**-3,14*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,60*10**-3,14*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(5,80*10**-3,14*10**-3,np.nan,np.nan,np.nan,-40))
    NTble.addNode_to_table(node(6,60*10**-3,(0.25*14+14)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(7,40*10**-3,(0.5*14+14)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(8,20*10**-3,(0.75*14+14)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(9,0,28*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(10,60*10**-3,(0.75*14)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(11,40*10**-3,(0.5*14)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(12,20*10**-3,(0.25*14)*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(13,0,0,0,0,np.nan,np.nan))
 
    
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
    Tr.addElementByNode(NTble,1,8)
    Tr.addElementByNode(NTble,2,8)
    Tr.addElementByNode(NTble,3,8)
    Tr.addElementByNode(NTble,3,7)
    Tr.addElementByNode(NTble,3,6)
    Tr.addElementByNode(NTble,4,6)
    Tr.addElementByNode(NTble,5,10)
    Tr.addElementByNode(NTble,10,11)
    Tr.addElementByNode(NTble,11,12)
    Tr.addElementByNode(NTble,12,13)
    Tr.addElementByNode(NTble,4,10)
    Tr.addElementByNode(NTble,3,10)
    Tr.addElementByNode(NTble,3,11)
    Tr.addElementByNode(NTble,3,12)
    Tr.addElementByNode(NTble,2,12)
    Tr.addElementByNode(NTble,1,12)
    
    
  
    return Tr

""" 
Fourth bridge attempt
"""

""" setting up the list of nodes """
def bridge_v4():
    """ setting up the list of nodes """
       # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,16*10**-3,10*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,32*10**-3,20*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,48*10**-3,30*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(5,64*10**-3,40*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(6,80*10**-3,50*10**-3,np.nan,np.nan,np.nan,-40))
    NTble.addNode_to_table(node(7,40*10**-3,40*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(8,0,30*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(9,0,20*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(10,0,10*10**-3,0,0,np.nan,np.nan))

    
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
    Tr.addElementByNode(NTble,2,10)
    Tr.addElementByNode(NTble,2,9)
    Tr.addElementByNode(NTble,3,9)
    Tr.addElementByNode(NTble,4,9)
    Tr.addElementByNode(NTble,4,8)
    Tr.addElementByNode(NTble,4,7)
    Tr.addElementByNode(NTble,5,7)
  
    
  
    return Tr



""" 
Jens bridge attempt
"""

def bridge_JensFinalV1():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 2+12
    turnTrussUpsideDown = False

    #How long should the distance between the nodes on the bottom line be?
    Leng = 69*10**-3
    
    #Distance between top and bottom line
    Height =  np.sqrt(Leng**2-(Leng/2)**2)
    
    #The number of the node where the load attaches
    ForceNodeNr = 13
    #Components of the force of the load    
    Fx = 0
    Fy = -40
   
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1, 101)
    
    #angle of the truss.
    angleTop = -10
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
    NTble.addNode_to_table(node(101,0,Height,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(102,0,0.3,0,0,np.nan,np.nan))
    
# === Manually add ELEMENTS below === 

    Tr.addElementByNode(NTble,102,33)
    
    #doubling
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)

# === == == == ==  == == == == ===

    return Tr


