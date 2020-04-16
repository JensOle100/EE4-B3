# -*- coding: utf-8 -*-
"""
Author: Jef De Smet | jef.desmet@kuleuven.be
edited: Pieter Spaepen
Date: February 2020

Class of trusses.
"""

"""
A truss instance contains all elements and nodes of your bridge and has a trussNr.
"""

# Imports
import numpy as np
#from element import element
#import node as node
import matplotlib.pyplot as plt
from matplotlib import cm 


''' incase this file is run as main file, create  classes needed for testing'''
#hardcoding the values
if __name__ =='__main__':
    class node:
        def __init__(self,nodeNr,xPos,yPos,X_disp,Y_disp,Fx,Fy):
            self.nodeNr = nodeNr
            self.xPos = xPos
            self.yPos = yPos      
            self.xDisp = X_disp  # it is important to set to nan if no boundary condition
            self.yDisp = Y_disp  # it is important to set to nan if no boundary condition
        
            self.Fx = Fx         # it is important to set to nan if no boundary condition
            self.Fy = Fy         # it is important to set to nan if no boundary condition
            # here your could things to do when you create a new node 
            # e.g. add the new nodeNr to the list_of_nodeNr you ever created
    class nodeTable:
        def __init__(self,n1,n2):
            self.nodeTable = [n1,n2]   
        def getNode_by_Nr(self,nr):
            if nr == 1:
                return self.nodeTable[0]
            elif nr == 2:
                return self.nodeTable[1]        
    class element:
        def __init__(self,elementNr,firstNode,secondNode):
            self.elementNr = 0
            self.firstNode = firstNode
            self.secondNode = secondNode
            #calculate teh length of the element
            self.elementLenght = 51
            self.elementArea = 8
            self.elementEmodulus = 1.9*10**6
            #calculate the element stiffness (pdf p150)
            self.elementStiffness = 298556
            self.elementInertia = 1
            #calculate the angle of the element, use np.arctan2 to obtain a correct angle
            self.elementAngle = 45/180*np.pi
            self.stressScale = 1
            #set the stress and buckling risk to nan 
            self.elementStress = np.nan
            self.elementBuckleRisk = np.nan
    """ done creating hard coded values for testing"""
    print('file called as main')
else:
     #the file is not being called as main file
    from element import element
 



class truss:


    def __init__(self,trussNr): # Build a Python list with elements
        self.trussNr = trussNr
        self.elementList = []
        
    # create a method to add existing element to the list    
    def addExistingElement(self,element):
        self.elementList.append(element)
        # use the "append" to add an element to the elementList    
        
        
    # create a method to  add a new element to the list using node numbers
    def addElementByNode(self,nodeTable,nodeNr1,nodeNr2):
        # noteTable: list holding all nodes defined
        # nodeNr1 & nodeNr2 
        # based on nodeNumbers create an element
        # step 1: get the 2 nodes
        Node1 = nodeTable.getNode_by_Nr(nodeNr1)
        Node2 = nodeTable.getNode_by_Nr(nodeNr2)
        #step 2: create an element using the element class
        # remember that setting the first variable to 0 will assign a free elementNr
        element2add = element(0,Node1,Node2)
        # step 3: add the element to the elementList using "append"
        self.elementList.append(element2add)
       
    # create a method to get the highest node number used in this truss
    def getHighestNodeNr(self):
        nodesUsed = []
        for e in self.elementList:
            nodesUsed.append(e.firstNode.nodeNr)
            nodesUsed.append(e.secondNode.nodeNr)
            #append the first node nr (tip: use append)
            #append the second node nr (tip: use append)
            
        # step 2: return the maximum value of the list of node numbers used 
        # tip use max
        return (max(nodesUsed))
    
    # create a method to return total surface area of all elements in the truss
    def getTotalSurfaceArea(self,Unit):
    #get the total surface area of all the elements in the truss
        totalSurfaceArea = 0
        for Elem in self.elementList:
    #add the surface to the totalSurfaceArea (*2 want de brug heeft twee symmetrische vlakken)
            totalSurfaceArea += (Elem.elementLength + 0.02)*0.02*2
        if Unit == '%':
            return totalSurfaceArea/(0.6*0.3) *100
        else:
            return totalSurfaceArea
        
    #EXTRA function to print the highest and lowest force.
    def print_MaxMinStress(self):
        
        stresses = []
        for Elem in self.elementList:
            stresses.append(Elem.elementStress)
            
        print('Highest  stress:', max(stresses)/10**6, 'Mpa')
        print('Lowest   stress:', min(stresses)/10**6, 'Mpa')
        
    def get_HighestBuckleRisk(self):
       
        bucklerisks = []
        for Elem in self.elementList:
            bucklerisks.append(Elem.elementBuckleRisk)
            
        return max(bucklerisks)
    
    def print_ElementLength(self):
        lengths = []
        for Elem in self.elementList:
            lengths.append(round(Elem.elementLength,3))
           
        lengthsReduced = list(set(lengths))
        
        for x in lengthsReduced:
            print('Length',x , 'm is used', lengths.count(x), 'times.')
         
              
    # create a method to print all information of an element
    def print_details(self,detailElement,detailNode):
        #e.g. print("elementNr = {}".format(self.elementListementNr)) 
        print("trussNr = {}".format(self.trussNr))
        print(*self.elementList)
        #cycle to through the elements to plot the info
        if detailElement:
            for el in self.elementList:
                el.print_details(detailNode)
                #print the element information, pass the detail for printing the node info
                
                
    # a method to print the result
    def plotTruss(self,h1,U):
        # h1: reference to a figure
        # U global displacement matrix
        """ create a plot form this graph """
        plt.figure(h1.number)
        plt.subplot(2,1,1)
        sc = 10
        for t in range(0,len(self.elementList)):
            # Plot original bridge
            x1 = self.elementList[t].firstNode.xPos
            y1 = self.elementList[t].firstNode.yPos
            x2 = self.elementList[t].secondNode.xPos
            y2 = self.elementList[t].secondNode.yPos
            plt.plot([x1,x2],[y1,y2],'k')

            # Plot the nodes for the deformed bridge
            xd1 = self.elementList[t].firstNode.xPos + sc*U[2*(self.elementList[t].firstNode.nodeNr),0]
            yd1 = self.elementList[t].firstNode.yPos + sc*U[2*(self.elementList[t].firstNode.nodeNr)+1,0] 
            plt.plot(xd1,yd1,'r.')
            # Not clean code, some nodes are being written twice
            xd1 = self.elementList[t].secondNode.xPos + sc*U[2*(self.elementList[t].secondNode.nodeNr),0]
            yd1 = self.elementList[t].secondNode.yPos + sc*U[2*(self.elementList[t].secondNode.nodeNr)+1,0]
            plt.plot(xd1,yd1,'r.')
            # Plot relevent node numbers above each truss.
            # Adapt font size and space before text to fit size of figure you want.
            tt=plt.text(x1,y1,"      ElNr: {0:}, node:  {1:}-{2:}".format(self.elementList[t].elementNr,self.elementList[t].firstNode.nodeNr,self.elementList[t].secondNode.nodeNr),fontsize=11,rotation=(np.arctan2((y2-y1),(x2-x1)))/3.14*180,rotation_mode='anchor',color='grey')
        plt.axis('equal')  
        plt.ylabel('metres')  
        plt.xlabel('metres') 
        plt.title('Unloaded Bridge with Displaced Points')
        #plt.show()
             
        #plt.figure(2)
        plt.subplot(2,1,2)
        #add second plot with colors for stress
        sc = 10  #scale to plot movement
        stressLimit = -19*10**6
        #first find the range of stresses
        stresses = np.zeros(len(self.elementList))
        for t in range(0,len(self.elementList)):
            stresses[t] = (self.elementList[t].elementStress)
        sress_range = (np.max(stresses)-np.min(stresses))*1.2
        
        line_list=[]
        color_list=[]

        for t in range(0,len(self.elementList)):
            # Plot trusses of deformed bridge, colour-coded to show stresses.
            x1 = self.elementList[t].firstNode.xPos + sc*U[2*(self.elementList[t].firstNode.nodeNr),0]
            y1 = self.elementList[t].firstNode.yPos + sc*U[2*(self.elementList[t].firstNode.nodeNr)+1,0] 
            x2 = self.elementList[t].secondNode.xPos + sc*U[2*(self.elementList[t].secondNode.nodeNr),0]
            y2 = self.elementList[t].secondNode.yPos + sc*U[2*(self.elementList[t].secondNode.nodeNr)+1,0]
            
            line_list.append([[x1,x2],[y1,y2]])
            color_list.append(((self.elementList[t].elementStress-np.min(stresses)*1.2)/sress_range))
            if self.elementList[t].elementStress <= stressLimit or self.elementList[t].elementBuckleRisk >=100:
                lineStyle = ':'
            else:
                lineStyle = '-'
            
            plt.plot([x1,x2],[y1,y2],c=cm.RdYlGn(color_list[-1]),lw=3,ls=lineStyle)
            # Adapt font size and space before text to fit size of figure you want.
            tt=plt.text(x1,y1,"        El: {2}: {0:1.3f}Mpa br{1:3.0f}\n ".format(self.elementList[t].elementStress/self.elementList[t].stressScale,self.elementList[t].elementBuckleRisk,self.elementList[t].elementNr),fontsize=6,rotation=(np.arctan2((y2-y1),(x2-x1)))/3.14*180,rotation_mode='anchor',color='grey')
            tt.set_bbox(dict(facecolor='white', alpha=0.5,edgecolor='none'))

        plt.axis('equal')
        plt.ylabel('metres')  
        plt.xlabel('metres') 
        plt.title('Loaded Bridge with Colour-Coded Stresses')
        plt.show()



""" the following section helps you to debug the code: 
You can test your functions by altering the code below
Do so for all the functions you create, investigate that everything behaves as expected
""" 
def testfunctionTruss():
    """ define variables """
    n1=node(1,0,0,np.nan,np.nan,np.nan,np.nan)              #node 1 of the textbook example
    n2=node(2,3*12,0,np.nan,np.nan,np.nan,np.nan)           #node 2 of the textbook example (feet to inch = *12)
    n5=node(5,6*12,3*12,np.nan,np.nan,np.nan,np.nan)        #node 2 of the textbook example (feet to inch = *12)
    NT = nodeTable(n1,n2)
    #enter example of U: length(U) = 2*(highest_node_nr +1), values from the textbook example
    U = np.array([[0], [0], [0], [0],[-0.00355], [-0.01026], [0], [0], [0.0018], [-0.0114], [0.0024], [-0.0195]])  
    elementExample = element(0,n2,n5)
    """ start testing the code """
    T = truss(1)
    T.addExistingElement(elementExample)
    T.addElementByNode(NT,1,2)
    T.print_details(False,False)
    f=plt.figure()
    T.plotTruss(f,U)
    
''' call the testfunction in case the file is being runned as "main file" '''    
if __name__ == '__main__':    
    testfunctionTruss() 
