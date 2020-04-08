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
first construction attempt
"""

""" setting up the list of nodes """
def TrussConstruction_Ciaran_v1_1():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,((130*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,(130*np.sqrt(3))*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,((650*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(5,((910*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(6,((1170*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(7,800*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(8,((1430*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,-500))
    NTble.addNode_to_table(node(9,0,130*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(10,((260*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(11,((520*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(12,((780*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(13,((1040*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(14,((1300*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(15,0,260*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(16,((130*np.sqrt(3))/3)*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(17,(130*np.sqrt(3))*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(18,((650*np.sqrt(3))/3)*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(19,((920*np.sqrt(3))/3)*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(20,((1170*np.sqrt(3))/3)*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
 
    """ setting up the list of elements """
    
    #create an empty truss
    Tr = truss(1)
    #add elements using addElementByNode
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)
    Tr.addElementByNode(NTble,3,4)
    Tr.addElementByNode(NTble,4,5)
    Tr.addElementByNode(NTble,5,6)
    Tr.addElementByNode(NTble,6,8)
    Tr.addElementByNode(NTble,9,2)
    Tr.addElementByNode(NTble,2,10)
    Tr.addElementByNode(NTble,10,3)
    Tr.addElementByNode(NTble,3,11)
    Tr.addElementByNode(NTble,11,4)
    Tr.addElementByNode(NTble,4,12)
    Tr.addElementByNode(NTble,12,5)
    Tr.addElementByNode(NTble,5,13)
    Tr.addElementByNode(NTble,13,6)
    Tr.addElementByNode(NTble,6,14)
    Tr.addElementByNode(NTble,14,8)
    Tr.addElementByNode(NTble,9,10)
    Tr.addElementByNode(NTble,10,11)
    Tr.addElementByNode(NTble,11,12)
    Tr.addElementByNode(NTble,12,13)
    Tr.addElementByNode(NTble,13,14)
    Tr.addElementByNode(NTble,9,16)
    Tr.addElementByNode(NTble,16,10)
    Tr.addElementByNode(NTble,10,17)
    Tr.addElementByNode(NTble,17,11)
    Tr.addElementByNode(NTble,11,18)
    Tr.addElementByNode(NTble,18,12)
    Tr.addElementByNode(NTble,12,19)
    Tr.addElementByNode(NTble,19,13)
    Tr.addElementByNode(NTble,13,20)
    Tr.addElementByNode(NTble,20,14)
    Tr.addElementByNode(NTble,15,16)
    Tr.addElementByNode(NTble,16,17)
    Tr.addElementByNode(NTble,17,18)
    Tr.addElementByNode(NTble,18,19)
    Tr.addElementByNode(NTble,19,20)
    
    return Tr


""" 
second construction attempt
"""

""" setting up the list of nodes """
def TrussConstruction_Ciaran_v1_2():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,((130*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,(130*np.sqrt(3))*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,((650*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(5,((910*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(6,((1170*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(7,800*10**-3,0,np.nan,np.nan,np.nan,-500))
    NTble.addNode_to_table(node(8,((1430*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(9,0,130*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(10,((260*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(11,((520*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(12,((780*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(13,((1040*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(14,((1300*np.sqrt(3))/3)*10**-3,130*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(15,0,260*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(16,((130*np.sqrt(3))/3)*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(17,(130*np.sqrt(3))*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(18,((650*np.sqrt(3))/3)*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(19,((920*np.sqrt(3))/3)*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(20,((1170*np.sqrt(3))/3)*10**-3,260*10**-3,np.nan,np.nan,np.nan,np.nan))
    
    """ setting up the list of elements """
    
    #create an empty truss
    Tr = truss(2)
    #add elements using addElementByNode
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)
    Tr.addElementByNode(NTble,3,4)
    Tr.addElementByNode(NTble,4,5)
    Tr.addElementByNode(NTble,5,6)
    Tr.addElementByNode(NTble,6,7)
    Tr.addElementByNode(NTble,9,2)
    Tr.addElementByNode(NTble,2,10)
    Tr.addElementByNode(NTble,10,3)
    Tr.addElementByNode(NTble,3,11)
    Tr.addElementByNode(NTble,11,4)
    Tr.addElementByNode(NTble,4,12)
    Tr.addElementByNode(NTble,12,5)
    Tr.addElementByNode(NTble,5,13)
    Tr.addElementByNode(NTble,13,6)
    Tr.addElementByNode(NTble,6,14)
    Tr.addElementByNode(NTble,14,7)
    Tr.addElementByNode(NTble,9,10)
    Tr.addElementByNode(NTble,10,11)
    Tr.addElementByNode(NTble,11,12)
    Tr.addElementByNode(NTble,12,13)
    Tr.addElementByNode(NTble,13,14)
    Tr.addElementByNode(NTble,9,16)
    Tr.addElementByNode(NTble,16,10)
    Tr.addElementByNode(NTble,10,17)
    Tr.addElementByNode(NTble,17,11)
    Tr.addElementByNode(NTble,11,18)
    Tr.addElementByNode(NTble,18,12)
    Tr.addElementByNode(NTble,12,19)
    Tr.addElementByNode(NTble,19,13)
    Tr.addElementByNode(NTble,13,20)
    Tr.addElementByNode(NTble,20,14)
    Tr.addElementByNode(NTble,15,16)
    Tr.addElementByNode(NTble,16,17)
    Tr.addElementByNode(NTble,17,18)
    Tr.addElementByNode(NTble,18,19)
    Tr.addElementByNode(NTble,19,20)
    
    return Tr


""" 
third construction attempt
"""

""" setting up the list of nodes """
def TrussConstruction_Ciaran_v2():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,160*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,480*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,800*10**-3,0,np.nan,np.nan,np.nan,-500))
    NTble.addNode_to_table(node(5,0,60*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(6,320*10**-3,60*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(7,640*10**-3,60*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(8,0,120*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(9,160*10**-3,120*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(10,480*10**-3,120*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(11,0,180*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(12,320*10**-3,180*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(13,0,240*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(14,160*10**-3,240*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(15,0,300*10**-3,0,0,np.nan,np.nan))
    
    """ setting up the list of elements """
    
    #create an empty truss
    Tr = truss(3)
    #add elements using addElementByNode
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)
    Tr.addElementByNode(NTble,3,4)
    Tr.addElementByNode(NTble,5,2)
    Tr.addElementByNode(NTble,2,6)
    Tr.addElementByNode(NTble,6,3)
    Tr.addElementByNode(NTble,3,7)
    Tr.addElementByNode(NTble,7,4)
    Tr.addElementByNode(NTble,5,6)
    Tr.addElementByNode(NTble,6,7)
    Tr.addElementByNode(NTble,5,9)
    Tr.addElementByNode(NTble,9,6)
    Tr.addElementByNode(NTble,6,10)
    Tr.addElementByNode(NTble,10,7)
    Tr.addElementByNode(NTble,8,9)
    Tr.addElementByNode(NTble,9,10)
    Tr.addElementByNode(NTble,11,9)
    Tr.addElementByNode(NTble,9,12)
    Tr.addElementByNode(NTble,12,10)
    Tr.addElementByNode(NTble,11,12)
    Tr.addElementByNode(NTble,11,14)
    Tr.addElementByNode(NTble,14,12)
    Tr.addElementByNode(NTble,13,14)
    Tr.addElementByNode(NTble,15,14)
    
    return Tr


""" 
fourth construction attempt
"""

""" setting up the list of nodes """
def TrussConstruction_Ciaran_v3():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,((280*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,((560*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,(280*np.sqrt(3))*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(5,((1120*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(6,800*10**-3,0,np.nan,np.nan,np.nan,-500))
    NTble.addNode_to_table(node(7,((1400*np.sqrt(3))/3)*10**-3,0,np.nan,np.nan,np.nan,-100)) 
    NTble.addNode_to_table(node(8,0,140*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(9,((140*np.sqrt(3))/3)*10**-3,140*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(10,(140*np.sqrt(3))*10**-3,140*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(11,((700*np.sqrt(3))/3)*10**-3,140*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(12,((980*np.sqrt(3))/3)*10**-3,140*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(13,((1260*np.sqrt(3))/3)*10**-3,140*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(14,0,280*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(15,((280*np.sqrt(3))/3)*10**-3,280*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(16,((560*np.sqrt(3))/3)*10**-3,280*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(17,(280*np.sqrt(3))*10**-3,280*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(18,((1120*np.sqrt(3))/3)*10**-3,280*10**-3,np.nan,np.nan,np.nan,np.nan))
 
    """ setting up the list of elements """
    
    #create an empty truss
    Tr = truss(4)
    #add elements using addElementByNode
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)
    Tr.addElementByNode(NTble,3,4)
    Tr.addElementByNode(NTble,4,5)
    Tr.addElementByNode(NTble,5,7)
    Tr.addElementByNode(NTble,1,9)
    Tr.addElementByNode(NTble,9,2)
    Tr.addElementByNode(NTble,2,10)
    Tr.addElementByNode(NTble,10,3)
    Tr.addElementByNode(NTble,3,11)
    Tr.addElementByNode(NTble,11,4)
    Tr.addElementByNode(NTble,4,12)
    Tr.addElementByNode(NTble,12,5)
    Tr.addElementByNode(NTble,5,13)
    Tr.addElementByNode(NTble,13,7)
    Tr.addElementByNode(NTble,8,9)
    Tr.addElementByNode(NTble,9,10)
    Tr.addElementByNode(NTble,10,11)
    Tr.addElementByNode(NTble,11,12)
    Tr.addElementByNode(NTble,12,13)
    Tr.addElementByNode(NTble,14,9)
    Tr.addElementByNode(NTble,9,15)
    Tr.addElementByNode(NTble,15,10)
    Tr.addElementByNode(NTble,10,16)
    Tr.addElementByNode(NTble,16,11)
    Tr.addElementByNode(NTble,11,17)
    Tr.addElementByNode(NTble,17,12)
    Tr.addElementByNode(NTble,12,18)
    Tr.addElementByNode(NTble,18,13)
    Tr.addElementByNode(NTble,14,15)
    Tr.addElementByNode(NTble,15,16)
    Tr.addElementByNode(NTble,16,17)
    Tr.addElementByNode(NTble,17,18)
    
    return Tr


""" 
fifth construction attempt
"""

""" setting up the list of nodes """
def TrussConstruction_Ciaran_v4():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,(100*np.sqrt(3))*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,(300*np.sqrt(3))*10**-3,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(4,(500*np.sqrt(3))*10**-3,0,np.nan,np.nan,np.nan,-500))
    NTble.addNode_to_table(node(5,0,300*10**-3,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(6,(200*np.sqrt(3))*10**-3,300*10**-3,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(7,(400*np.sqrt(3))*10**-3,300*10**-3,np.nan,np.nan,np.nan,np.nan)) 
    
    """ setting up the list of elements """
    
    #create an empty truss
    Tr = truss(5)
    #add elements using addElementByNode
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,2,3)
    Tr.addElementByNode(NTble,3,4)
    Tr.addElementByNode(NTble,5,2)
    Tr.addElementByNode(NTble,2,6)
    Tr.addElementByNode(NTble,6,3)
    Tr.addElementByNode(NTble,3,7)
    Tr.addElementByNode(NTble,7,4)
    Tr.addElementByNode(NTble,5,6)
    Tr.addElementByNode(NTble,6,7)
    Tr.addElementByNode(NTble,1,7)
   
    return Tr