# -*- coding: utf-8 -*-
"""
Author: Jef De Smet | jef.desmet@kuleuven.be
edited: Pieter Spaepen
Date: February 2020

Class of elements.
"""

"""
An element has at least 
    elementNr          elementNr used as identifier of this element, must be chosen unique
    firstNode          the starting node
    secondNode         the ending node
    elementLength      the length of the element, to be calculated
    elementArea        A
    elementEmodulus    E
    elementStiffnes    the k value of the element 
    elementInertia     I
    elementAngle       angle of the element in the world frame
    elementStress      will hold the calculated resulting stress
    elementBuckleRisk  will hold the calculated risk of buckling

two node instances attached to it, an elementNr, an elementLenght, an elementStiffness and elementAngle.
Extra features could be added.
"""

# Imports
import numpy as np

# select the example to plot,  This should be altered in your code
book_ex = False
if book_ex:
    A = 8                                       #value from textbook example
    E = 1.9*10**6                               #value from textbook example
    I = 1                                       #random variable
    Scale_Mpa = 1                               #use 1 as the scale, no conversion to MPa
else:
    #default values to be used when creating an element
    plateThickness = 3*10**-3                   #[m] plate thickness
    elementWidth = 7*10**-3                     #[m] width of the element
    A = (plateThickness)*(elementWidth)         #[m²] Surface area of cross section of the elements
    E = 3*10**9                                 #[Pa] E modulus of MDF
    I = ((elementWidth)*(plateThickness)**3)/12 #[m^4] Second moment of inertia, m4
    Scale_Mpa = 10**6                           #can be used to convert plots to Mpa



class element:

    # this section can be used to initialize variables that have to be altered every time a node is created. 
    # e.g. list_of_elementNrs = []
    list_of_elementNrs = []

    def __init__(self,elementNr,firstNode,secondNode):
        # if elementNr is 0 and element.list_of_elemenNrs is not empty-> assign next free elementNr
        if elementNr == 0 and len(self.list_of_elementNrs) != 0:
#            self.elementNr = elementNr + 1
            self.elementNr = max(self.list_of_elementNrs) + 1 
        else:

            self.elementNr = elementNr + 1
        self.firstNode = firstNode
        self.secondNode = secondNode
        #calculate teh length of the element
        self.elementLength = np.sqrt((firstNode.xPos - secondNode.xPos)**2 + (firstNode.yPos - secondNode.yPos)**2)
        self.elementArea = A
        self.elementEmodulus =E
        #calculate the element stiffness (pdf p150)
        self.elementStiffness = (self.elementArea*self.elementEmodulus) / self.elementLength
        self.elementInertia = I
        #calculate the angle of the element, use np.arctan2 to obtain a correct angle
        
        self.elementAngle = np.arctan2(secondNode.yPos -firstNode.yPos , secondNode.xPos - firstNode.xPos)
        self.stressScale = Scale_Mpa
        
        #set the stress and buckling risk to nan 
        self.elementStress = np.nan
        self.elementBuckleRisk = np.nan
        
        # here your could things to do when you create a new element 
        # e.g. add the new elementNr to the list_of_elementNrs
        element.list_of_elementNrs.append(self.elementNr)
        
    # create a method to print all information of an element
    def print_details(self,details):
        #e.g. print("elementNr = {}".format(self.elementNr))
        print("   elementNr = {}".format(self.elementNr))

        
        print("   firstNode = {}".format(self.firstNode.nodeNr))
        if details:
            self.firstNode.print_details()
            
        print("   secondNode = {}".format(self.secondNode.nodeNr))
        if details:
            self.secondNode.print_details()
            
        print("   elementAngle = {}".format(self.elementAngle/(np.pi)*180))
        
    # create a method to change the Emodulus to some value
    def setEmodulus(self,value):
        #add code here to change the E modulus (don't forget to also set the new elementStiffness)
        self.elementEmodulus = value
        self.elementStiffness =  (self.elementArea*self.elementEmodulus) / self.elementLength

    # create a method to change the Inertia to some value
    def setInertia(self,value):
        #add code here to change the E modulus
        self.elementInertia = value
        
        
    # create a method to calculate the stress based on the global displacement matrix
    def setStress(self,U):
        # U is the global displacement matrix with all the global displacement results
        # in order to access the current information out of U you will have to use the node nrs
        # step 1: select the relevant global displacements
        # U_relevant = ...
        U_relevant = [U[2*(self.firstNode.nodeNr),0],U[(2*(self.firstNode.nodeNr))+1,0],U[(2*(self.secondNode.nodeNr)),0],U[(2*(self.secondNode.nodeNr))+1,0]]
        # step 2: T^-1 matrix to local displacements, (pdf p162)
        # create T_inv based on the information of the element
        # T_inv = ...
        T_inv = [[np.cos(self.elementAngle),np.sin(self.elementAngle),0,0], \
                 [-np.sin(self.elementAngle),np.cos(self.elementAngle),0,0], \
                 [0,0,np.cos(self.elementAngle),np.sin(self.elementAngle)], \
                 [0,0,-np.sin(self.elementAngle),np.cos(self.elementAngle)]]
        # step 3: calculate the local displacements 
        # tip: use np.matmul in order to do the correct 
        # u = ....
        u = np.matmul(T_inv, U_relevant, out=None)
        # step 4: calculate the stress using u[0] and u[2]
        # self.elementStress = 
        self.elementStress = (self.elementEmodulus)*((u[0] - u[2])/(self.elementLength))

     # create a method to calculate the buckling risk of the element   
    def setBuckleRisk(self):       
       k = 1  #coefficient of euler formula
       # step 1: check if the elementStress is > 0  -> compression of the element
       # else the element is in tension and the risk is set to 0
       if self.elementStress > 0:
           # step 2: calculate the maximum Buckling force using Euler formula
           k = 1  #coefficient of euler formula
           Fcrit = ((np.pi**2) * self.elementEmodulus * self.elementInertia)/(k * self.elementLength)**2
           # step 3: calculate the current force based on Stress and Area
           Fcur = self.elementStress*self.elementArea
           # step 4: the buckling risk is the (current force)/(critical force)*100
           self.elementBuckleRisk = (Fcur)/(Fcrit)*100
       else:
          self.elementBuckleRisk = 0

    @classmethod
     # this section can be used to act on the variables created in the top section 
    # e.g on the list_of_elementNrs
    # e.g. def verify_unique_elementNr(cls)
    #          create code to verify if elementNrs are unique and return/print the result
    #          tip use "unique"
    def verify_unique_elementNr(cls):
        boolean = True
        for x in cls.list_of_elementNrs:
            count = 0
            for y in cls.list_of_elementNrs:
                if x == y:
                    count = count + 1
                    if count == 2:
                        boolean = False
        print("Is unique element? : ")
        print(boolean)
        
     
""" the following section helps you to debug the code: 
You can test your functions by altering the code below
Do so for all the functions you create, investigate that everything behaves as expected
""" 
def testfunctionElement():
    """ create some hardcode values to test the code of this file"""
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
    n1=node(1,0,0,np.nan,np.nan,np.nan,np.nan)              #node 1 of the textbook example
    n2=node(2,3*12,0,np.nan,np.nan,np.nan,np.nan)           #node 2 of the textbook example (feet to inch = *12)
    n5=node(5,6*12,3*12,np.nan,np.nan,np.nan,np.nan)        #node 2 of the textbook example (feet to inch = *12)
    #class nodeTable:
    #    def __init__(self,n1,n2):
    #        self.nodeTable = [n1,n2]       
    #NT = nodeTable(n1,n2)                                   #create a node table cuold be used for testing additional functions
    #enter example of U: length(U) = 2*(highest_node_nr +1), values from the textbook example
    U = np.array([[0], [0], [0], [0],[-0.00355], [-0.01026], [0], [0], [0.0018], [-0.0114], [0.0024], [-0.0195]])            
    """ we now have a nodeTable and nodes we can use for further testing of the code"""
    test_element=element(0,n2,n5)
    test_element.print_details(False)       #printing with True will not work (why?)
    test_element.setStress(U)
    test_element.print_details(False)       #the value of the stress should now be 86.81
    test_element.setBuckleRisk()
    test_element.print_details(False)       #the value of the BucklerRisk should now be 9.6%

    test_element.verify_unique_elementNr()  #test this section of the code   

''' call the testfunction in case the file is being runned as "main file" ''' 
if __name__ == '__main__':
    testfunctionElement()
