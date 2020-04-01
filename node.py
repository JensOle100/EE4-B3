# -*- coding: utf-8 -*-
"""
Author: Jef De Smet | jef.desmet@kuleuven.be
edit: Pieter Spaepen
Date: February 2020

#####JENS: Last Edit 01/04/2020


Class of nodes.
"""

"""
A node has 
    nodeNr  identifier of the node for future reference to the node, should be unique
    xPos    x position in global coordinate system
    yPos    y position in global coordinate system  
    X_disp  X displacement of the node, if the node is free to move in the X direction -> X_disp = np.nan
    Y_disp  Y displacement of the node, if the node is free to move in the y direction -> Y_disp = np.nan
    Fx      Force in the X direction on the node, if no force is applied in the X direction -> Fx = np.nan
    Fy      Force in the Y direction on the node, if no force is applied in the Y direction -> Fy = np.nan
    
student groups are free to add additional variables (e.g. to verify that node have an unique nodeNr)

"""

# Imports
import numpy as np

class node:
    
    
    # this section can be used to initialize variables that have to be altered everytime a node is created. 
    # e.g. list_of_nodeNr = []
    list_of_nodeNr = []  
    
    # initialization section of a new node    
    def __init__(self,nodeNr,xPos,yPos,X_disp = np.nan,Y_disp = np.nan,Fx = np.nan, Fy = np.nan):
        self.nodeNr = nodeNr
        self.xPos   = xPos
        self.yPos   = yPos
        
        self.xDisp  = X_disp    # it is important to set to nan if no boundary condition
        self.yDisp  = Y_disp    # it is important to set to nan if no boundary condition
        
        self.Fx     = Fx        # it is important to set to nan if no boundary condition
        self.Fy     = Fy        # it is important to set to nan if no boundary condition
        
        
        # here you could put code to be executed when you create a new node 
        # e.g. add the new nodeNr to the list_of_nodeNr you  created
        node.list_of_nodeNr.append(self.nodeNr)
        
    # create a method to print all information of the node    
    def print_details(self):
        # e.g. print("nodeNr = {}".format(self.nodeNr))
              
        print('Node -->', self.nodeNr, 
              'Position:',      '(' + str(self.xPos)    +',' + str(self.yPos)   + ')', 
              'Displacement:',  '(' + str(self.xDisp)   +',' + str(self.yDisp)  + ')', 
              'Force:',         '(' + str(self.Fx)      +',' + str(self.Fy)     + ')')
        

    @classmethod
    # this section can be used to act on the variables created in the top section 
    # e.g on the list_of_nodeNr
    # e.g. def verify_unique_nodeNr(cls)
    #          create code to verify if nodeNrs are uniqe and return/print the result
    #          tip use "np.unique"
    def verify_unique_nodeNr(cls):
        temp = np.unique(cls.list_of_nodeNr)
        if len(temp)==len(cls.list_of_nodeNr):
            print("ALL nodeNrs defined are unique. Used nodeNrs", *np.sort(cls.list_of_nodeNr),sep = "; ") #the * tells python to print all elements from the list
            return True
        else:
            print("! !! NOT all nodeNrs defined are unique. Used nodeNrs", *np.sort(cls.list_of_nodeNr),sep = "; ")
            return False


""" define a class of nodeTables, this can hold all nodes defined"""
class nodeTable:
      
    # initialization section of a new node  
    def __init__(self):
        self.nodeTable = []
        
    # create a method to add a node to the table
    def addNode_to_table(self,node2add):
        # use "append" to add node2add to tbl
        self.nodeTable.append(node2add)
        
    # create a methode to get a node by nodeNr
    def getNode_by_Nr(self,Nr):
        # go through the list of nodes and return the correct node
        # use break at an appropriate location
        
        for x in self.nodeTable:
            if x.nodeNr == Nr:
                return x
                break
            
            
###Jens: Deze functie hebben wij zelf toegevoegd.            
    def getHighestNodeNr(self):
        Nr = 0
        for node in self.nodeTable:
    
            if Nr < node.nodeNr:
                Nr = node.nodeNr
        return Nr




        """ the following section helps you to debug the code: 
            You can test your functions by altering the code below
            Do so for all the functions you create, investigate that everything behaves as expected
        """    
        
def testfunctionNode():
    NT=nodeTable()                                  #create a nodeTable
    n = node(0,1,2,np.nan,np.nan,np.nan,np.nan)     #create a node
    n.print_details()                               #print the information of a node
    NT.addNode_to_table(n)                          #add node to the nodetable
    n = node(2,3,4,np.nan,np.nan,np.nan,np.nan)     #create a second node (overwriting the values of the first node)
    NT.addNode_to_table(n)                          #add node to the nodeTable
    n.print_details()                               #print the information of this node
    print(*n.list_of_nodeNr, sep = ", ")            #print the list of the nodenumbers used
    n_retr = NT.getNode_by_Nr(2)                    #retrieve the node labeled "2"
    n_retr.print_details()                          #print the info of node labeled "2"
    n.verify_unique_nodeNr()                        #check if node numbers are unique
    del n                                           #delete node "n"
    n = node(3,3,4,np.nan,np.nan,np.nan,np.nan)     #create a new, third node called "3"
    n.verify_unique_nodeNr()                        #check if node numbers are unique: you will find that node numbers "0" "2" and "3" are used
    n_retr = NT.getNode_by_Nr(2)                    #retrieve the node labeled "2"
    n_retr.print_details()                          #node "2" still existed in the node table
    
    #Jens: extra functies zelf verzonnen
    
    print('The highest node nr in this table is', NT.getHighestNodeNr())


''' call the test function in case the file is being runned as "main file" ''' 
if __name__ == '__main__':
    testfunctionNode()
