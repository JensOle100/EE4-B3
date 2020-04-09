
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
def bridge_1():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 8
    turnTrussUpsideDown = False

    #How long should the distance between the nodes on the bottom line be?
    Leng = 150*10**-3
    
    #Distance between top and bottom line
    Height =  np.sqrt(Leng**2-(Leng/2)**2)

    
    #The number of the node where the load attaches
    ForceNodeNr = 7
    
    #Components of the force of the load    
    Fx = 0
    Fy = -5    
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1)
    
    #angle of the truss.
    angleTop = 30
    radTop = np.radians(angleTop)
    
    angleBottom = 30
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
    NTble.addNode_to_table(node(101,0,0.3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(102,0.15*np.cos(np.radians(30)),0.15*np.sin(np.radians(30))+0.3,np.nan,np.nan,np.nan,np.nan))

# === Manually add ELEMENTS below ===   
    Tr.addElementByNode(NTble,101,23)
    Tr.addElementByNode(NTble,102,23)
    Tr.addElementByNode(NTble,102,24)
    Tr.addElementByNode(NTble,102,101)
# === == == == ==  == == == == ===
        
    return Tr

def bridge_2():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 2+6
    turnTrussUpsideDown = True

    #How long should the distance between the nodes on the bottom line be?
    Leng = 140*10**-3
    
    #Distance between top and bottom line
    Height =  np.sqrt(Leng**2-(Leng/2)**2)
    
    #The number of the node where the load attaches
    ForceNodeNr = 7
    
    #Components of the force of the load    
    Fx = 0
    Fy = -11
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1, 101)
    
    #angle of the truss.
    angleTop = 27
    radTop = np.radians(angleTop)
    
    angleBottom = angleTop
    radBottom = np.radians(angleBottom)
    
    # #same values but for the additional structure on top.
    # Leng2 = 280*10**-3
    # Height2 = np.sqrt(Leng2**2-(Leng2/2)**2)
    # nodesQuantityTop = 2+2
    # angleExtra = 30
    # radExtra = np.radians(angleExtra)
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
    
    # #creating the second top truss line. (now the actual top)    
    # for x in range(1, nodesQuantityTop-1):
    #     tempNr = x
        
    #     if tempNr == ForceNodeNr:
    #         tempFx = Fx
    #         tempFy = Fy
    #     else:
    #         tempFx = np.nan
    #         tempFy = np.nan
            
    #     if tempNr in LockNodeNrs:
    #         tempDispX = 0
    #         tempDispY = 0
    #     else:
    #         tempDispX = np.nan
    #         tempDispY = np.nan

    #     NTble.addNode_to_table(node(tempNr+100,(x*Leng2-Leng2/2)*np.cos(radExtra)-Height2*np.sin(radExtra),Height2*np.cos(radExtra)+(x*Leng2-Leng2/2)*np.sin(radExtra),tempDispX,tempDispY,tempFx,tempFy))

   
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
    NTble.addNode_to_table(node(101,0,0.3,0,0,np.nan,np.nan))

#    NTble.addNode_to_table(node(101,0,0.3,0,0,np.nan,np.nan))

# === Manually add ELEMENTS below === 
    Tr.addElementByNode(NTble,101,4)
    
    Tr.addElementByNode(NTble,24,25)
  
    # Tr.addElementByNode(NTble,101,3)
    # Tr.addElementByNode(NTble,102,3)
    # Tr.addElementByNode(NTble,102,5)
    # Tr.addElementByNode(NTble,101,102)


# === == == == ==  == == == == ===
        
    return Tr

def bridge_3():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 2+6
    turnTrussUpsideDown = True

    #How long should the distance between the nodes on the bottom line be?
    Leng = 150*10**-3
    
    #Distance between top and bottom line
    Height =  np.sqrt(Leng**2-(Leng/2)**2)
    
    #The number of the node where the load attaches
    ForceNodeNr =201   
    #Components of the force of the load    
    Fx = 0
    Fy = -10
   
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1, 101)
    
    #angle of the truss.
    angleTop = 30
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
    NTble.addNode_to_table(node(101,0,0.3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(201,0.8,0.35,np.nan,np.nan,Fx,Fy))
    
    
# === Manually add ELEMENTS below === 
    Tr.addElementByNode(NTble,101,4)
    
    Tr.addElementByNode(NTble,201,7)
    Tr.addElementByNode(NTble,201,27)
    
    #doubling
    Tr.addElementByNode(NTble,23,24)
    Tr.addElementByNode(NTble,24,25)
    Tr.addElementByNode(NTble,25,26)

# === == == == ==  == == == == ===
        
    return Tr

def bridge_4():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 2+7
    turnTrussUpsideDown = True

    #How long should the distance between the nodes on the bottom line be?
    Leng = 120*10**-3
    
    #Distance between top and bottom line
    Height =  np.sqrt(Leng**2-(Leng/2)**2)
    
    #The number of the node where the load attaches
    ForceNodeNr =201   
    #Components of the force of the load    
    Fx = 0
    Fy = -15
   
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1, 101)
    
    #angle of the truss.
    angleTop = 30
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
    NTble.addNode_to_table(node(101,0,0.3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(201,0.8,0.35,np.nan,np.nan,Fx,Fy))
    
    
# === Manually add ELEMENTS below === 
    Tr.addElementByNode(NTble,101,5)
    
    Tr.addElementByNode(NTble,201,8)
    Tr.addElementByNode(NTble,201,28)
    
    #doubling
    Tr.addElementByNode(NTble,24,25)
    Tr.addElementByNode(NTble,25,26)
    Tr.addElementByNode(NTble,26,27)
# === == == == ==  == == == == ===

    return Tr

def bridge_5():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 2+8
    turnTrussUpsideDown = True

    #How long should the distance between the nodes on the bottom line be?
    Leng = 100*10**-3
    
    #Distance between top and bottom line
    Height =  np.sqrt(Leng**2-(Leng/2)**2)
    
    #The number of the node where the load attaches
    ForceNodeNr =201   
    #Components of the force of the load    
    Fx = 0
    Fy = -20
   
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1, 101)
    
    #angle of the truss.
    angleTop = 30
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
    NTble.addNode_to_table(node(101,0,0.3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(201,0.8,0.35,np.nan,np.nan,Fx,Fy))
    
    
# === Manually add ELEMENTS below === 
    Tr.addElementByNode(NTble,101,6)
    
    Tr.addElementByNode(NTble,201,9)
    Tr.addElementByNode(NTble,201,29)
    
    #doubling
    Tr.addElementByNode(NTble,6,7)
    Tr.addElementByNode(NTble,24,25)
    Tr.addElementByNode(NTble,25,26)
    Tr.addElementByNode(NTble,26,27)
    Tr.addElementByNode(NTble,27,28)
# === == == == ==  == == == == ===

    return Tr

def bridge_6():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()

# =====================INPUTS===============================
    #How many nodes on the bottom line of the truss?
    nodesQuantity = 2+8
    turnTrussUpsideDown = True

    #How long should the distance between the nodes on the bottom line be?
    Leng = 100*10**-3
    
    #Distance between top and bottom line
    Height =  np.sqrt(Leng**2-(Leng/2)**2)
    
    #The number of the node where the load attaches
    ForceNodeNr =201   
    #Components of the force of the load    
    Fx = 0
    Fy = -20
   
    #Number of the nodes that cannot move. (attached to the mounting)
    LockNodeNrs = (0, 1, 101)
    
    #angle of the truss.
    angleTop = 30
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
    NTble.addNode_to_table(node(101,0,0.3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(201,0.8,0.35,np.nan,np.nan,Fx,Fy))
    
    
# === Manually add ELEMENTS below === 
    Tr.addElementByNode(NTble,101,6)
    
    Tr.addElementByNode(NTble,201,9)
    Tr.addElementByNode(NTble,201,29)
    
    #doubling
    Tr.addElementByNode(NTble,6,7)
    Tr.addElementByNode(NTble,24,25)
    Tr.addElementByNode(NTble,25,26)
    Tr.addElementByNode(NTble,26,27)
    Tr.addElementByNode(NTble,27,28)
# === == == == ==  == == == == ===

    return Tr
