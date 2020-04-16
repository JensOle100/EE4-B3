# -*- coding: utf-8 -*-

#####Jens: Last edit 01/04/2020

"""
Author: Jef De Smet | jef.desmet@kuleuven.be
edited: Pieter Spaepen
Date: February 2020
"""

import numpy as np
import matplotlib.pyplot as plt

from node import *
from element import *
from truss import *

# close all open figures
plt.close('all')


# step 1: call a file with a truss definition, make sure you import this file

usePreloaded = False
if usePreloaded:
    #this will load a set of variables to get you going without element, node & truss working
    from dummy import dummy
    Tr=dummy()
    
else: 
    #use this section to validate that your code can handle a truss input
    book_ex = False
    if book_ex:
        from book_example import book_example
        Tr = book_example()
    else:
        from TheBridge import bridge_JensFinalV2
        Tr = bridge_JensFinalV2()
        
#additional function added to be able to print matrices
def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

# step 2: generate empty/zero matrices, 
# the number of rows and columns is equal to 2*(highest node number used +1)

matrixDimension = (Tr.getHighestNodeNr() + 1)*2

K = np.zeros((matrixDimension, matrixDimension))
U = np.empty((matrixDimension, 1))

# set all values of the displacement matrix to nan
# use nan in order to be able to discriminate between 0 and no value
U[:] = np.nan
# for now we set all external forces to zero
F = np.zeros((matrixDimension, 1))


# step 3: boundary conditions for the positions
# cycle through the list of elements and set the boundary conditions of the node
for El in Tr.elementList:
    node1 = El.firstNode
    U[node1.nodeNr*2,0]=        node1.xDisp
    U[node1.nodeNr*2 + 1,0]=    node1.yDisp
    
    node2 = El.secondNode
    U[node2.nodeNr*2,0]=        node2.xDisp
    U[node2.nodeNr*2 + 1,0]=    node2.yDisp


# step 4: boundary conditions for the forces
# cycle through the list of elements and set the boundary conditions of the node
for El in Tr.elementList:
    # get the first node
    node1 = El.firstNode
    # if not Fx in node1 == nan use the value to be set in F
    # tip: use np.isnan
    if not np.isnan(node1.Fx):
        F[node1.nodeNr*2,0] = node1.Fx    
    # if not Fy in node1 == nan use the value to be set in F
    # tip: use np.isnan    
    if not np.isnan(node1.Fy) :
        F[node1.nodeNr*2 + 1,0] = node1.Fy
    # get the second node2 and repeat the process
    node2 = El.secondNode
    if not np.isnan(node2.Fx) :
        F[node2.nodeNr*2,0] = node2.Fx   
    if not np.isnan(node2.Fy):
        F[node2.nodeNr*2 + 1,0] = node2.Fy
     

# step 5: global stiffness matrix
# cycle through the elements and add the correct values to the stiffness matrix
for El in Tr.elementList:
    # step 5a: get local stiffens
    k = El.elementStiffness
    # step 5b: get element angle
    th = El.elementAngle
    # step 5c: get index ni and nj based on the node numbers


    # ni equals 2 times the node number of the first node
    # nj equals 2 times the node number of the second node
    # top left corner: [ni,ni]
    ni = 2 * El.firstNode.nodeNr
    nj = 2 * El.secondNode.nodeNr

    # step 5d: add all 16 elements to the matrix
    K[ni,ni]     =  K[ni,ni]     +  k*(np.cos(th))**2
    K[ni,ni+1]   =  K[ni,ni+1]   +  k*np.sin(th)*np.cos(th)
    K[ni+1,ni]   =  K[ni+1,ni]   +  k*np.sin(th)*np.cos(th)
    K[ni+1,ni+1] =  K[ni+1,ni+1] +  k*(np.sin(th))**2
    
    K[ni,nj]     =  K[ni,nj]     -  k*(np.cos(th))**2
    K[ni,nj+1]   =  K[ni,nj+1]   -  k*np.sin(th)*np.cos(th)
    K[ni+1,nj]   =  K[ni+1,nj]   -  k*np.sin(th)*np.cos(th)
    K[ni+1,nj+1] =  K[ni+1,nj+1] -  k*(np.sin(th))**2
    
    K[nj,ni]     =  K[nj,ni]     -  k*(np.cos(th))**2
    K[nj,ni+1]   =  K[nj,ni+1]   -  k*np.sin(th)*np.cos(th)
    K[nj+1,ni]   =  K[nj+1,ni]   -  k*np.sin(th)*np.cos(th)
    K[nj+1,ni+1] =  K[nj+1,ni+1] -  k*(np.sin(th))**2
    
    K[nj,nj]     =  K[nj,nj]     +  k*(np.cos(th))**2
    K[nj,nj+1]   =  K[nj,nj+1]   +  k*np.sin(th)*np.cos(th)
    K[nj+1,nj]   =  K[nj+1,nj]   +  k*np.sin(th)*np.cos(th)
    K[nj+1,nj+1] =  K[nj+1,nj+1] +  k*(np.sin(th))**2

 
# step 6 reduce the matrix to hold only rows/columns needed
# step 6a: create an empty array to hold all indices needed
keep = [];
# step 6b: for all rows of K verify that K[t] is a non empty row and that U[t] is not equal to zero
# if these conditions are met: keep this row
# verification of non empty row can be done summing the absolute values of a row
# if this sum is not equal to 0, non 0 elements are present in K
# use t running from 1 to len(K) to verify the conditions above
# tip: for t in range(0,len(K)):
# tip: to check against 0 use "!=0"
for t in range(0,len(K)):
    if np.count_nonzero(K[t]) != 0 and U[t]!=0:
        keep.append(t)

# step 6c: create a K_reduced & F _reduced , holding only the rows (&columns) to keep
# tip: use  np.ix_       
  
K_reduced = K[np.ix_(keep, keep)]
F_reduced = F[keep]

# step 7: calculate U_reduced
# tip: use numpy.linalg.solve
U_reduced = np.linalg.solve(K_reduced, F_reduced)

# step 8: use "keep" to copy the values of U_reduced to the correct location in U
# use t running from 1 to len(K) to index all variables
#tip: for t in range(0,len(keep)):
for t in range(0,len(keep)):
    U[keep[t]] = U_reduced[t]
    
# step 9: remove nan elements in U, set them to 0
# this step is needed in order to be able to calculate reaction forces    
index_nans = np.isnan(U)
U[index_nans] = 0
    
# step 10: calculate the reaction forces
# tip use the @ function for matrix multiplication
F_reaction = np.matmul(K, U) - F
 
# step 11: calculate the stress and buckling risk in all elements
# cycle through the list of elements and calculate the values
for El in Tr.elementList:
    El.setStress(U)
    El.setBuckleRisk()

#generate an empty figure to be used for plotting. 
h1=plt.figure(figsize = (20, 20), dpi=150)    
Tr.plotTruss(h1,U)

#EXTRA print commands to asses truss construction faster
print('Highest buckle risk:', Tr.get_HighestBuckleRisk(), '%')

print('surface area:',Tr.getTotalSurfaceArea('%'),'%')
print('surface area:',Tr.getTotalSurfaceArea(1), 'm^2')
Tr.print_MaxMinStress()

print('All node Nrs:',node.list_of_nodeNr)
Tr.print_ElementLength()

