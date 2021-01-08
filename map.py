import numpy as np
import random
import sys
import matplotlib.pyplot as plt
from matplotlib import cm

#in this function the value 3 informs that we already changed the main value 
def add_value_first_case(A,i,j):
    value = np.random.randint(3)
    if value == 0:
       A[i][j][1] = 3 
       A[i][j][2] = 3 
    if value == 1:
       A[i][j][0] = 3 
       A[i][j][2] = 3 
    if value == 2:
       A[i][j][0] = 3 
       A[i][j][1] = 3 

def add_value_general_case(A,i,j):

    value = 4

    case01 = [0,1]
    case12 = [1,2]

    #here we everify the case
    data_0 = 0
    data_1 = 0
    data_2 = 0
    for k in range(3):
        if A[i][j][k] == 0:
           data_0 = 1
        if A[i][j][k] == 1:
           data_1 = 1
        if A[i][j][k] == 2:
           data_2 = 1

    if(data_0 == 1 and data_1 == 1 and data_2 == 0):
        value  = random.choice(case01)
        if value == 0:
            A[i][j][1] = 3 
            A[i][j][2] = 3 
        else:
            A[i][j][0] = 3 
            A[i][j][2] = 3 
    elif(data_0 == 0 and data_1 == 1 and data_2 == 1):
        value = random.choice(case12)    
        if value == 1:
            A[i][j][0] = 3 
            A[i][j][2] = 3 
        else:
            A[i][j][0] = 3 
            A[i][j][1] = 3  
    elif(data_0 == 1 and data_1 == 1 and data_2 == 1):
        value = np.random.randint(3)
        if value == 0:
            A[i][j][1] = 3 
            A[i][j][2] = 3 
        if value == 1:
            A[i][j][0] = 3 
            A[i][j][2] = 3 
        if value == 2:
            A[i][j][0] = 3 
            A[i][j][1] = 3 
 
def remove_0(A,i,j):
    A[i][j][0] = 3

def remove_1(A,i,j):
    A[i][j][1] = 3

def remove_2(A,i,j):
    A[i][j][2] = 3

#this function tells the adjacency rules, i.e,
#--if A[i][j] = 0, then the neighbourhoods must be 0 or 1
#--if A[i][j] = 1, then the neighbourhoods can be 0, 1 or 2
#--if A[i][j] = 2, then the neighbourhoods must be 1 or 2
def inform_neighbourhood_first_case(A,i,j):
    for k in range(3):
        if A[i][j][k] == 0:
           remove_2(A,i+1,j)
           remove_2(A,i,j+1)
        if A[i][j][k] == 2:
           remove_0(A,i+1,j)
           remove_0(A,i,j+1)

def inform_neighbourhood_general_case(A,i,j, size_num):
    for k in range(3):
        if A[i][j][k] == 0:
           if(i<size_num-1):
               remove_2(A,i+1,j)
           if(j<size_num-1):    
               remove_2(A,i,j+1)
        if A[i][j][k] == 2:
           if(i<size_num-1):
               remove_0(A,i+1,j)
           if(j<size_num-1):
               remove_0(A,i,j+1)

def main_change(A, i, j, size_num):
    
    #first time
    if (i==0 and j==0):
        add_value_first_case(A,i,j)
        inform_neighbourhood_first_case(A,i,j)
    else:
        add_value_general_case(A,i,j)
        inform_neighbourhood_general_case(A,i,j, size_num)

#function find_value returns the state from the entry A[i][j][.]
def find_value(A,i,j):
    for k in range(3):
        if A[i][j][k] == 0:
           return A[i][j][k]
        if A[i][j][k] == 1:
           return A[i][j][k]
        if A[i][j][k] == 2:
           return A[i][j][k]

#this function takes the states from A to a 2d numpy array B 
def states_selector(A,B, size_num):

    for j in range(size_num):
        for i in range(size_num):
            B[i][j] = find_value(A,i,j)


#here it is taken as input from the user the size 'size_num'
#in the command line
size_num = int(sys.argv[1])
A = np.zeros((size_num,size_num,3))
B = np.zeros((size_num,size_num))

#here we create the matrix with superposition states 
for k in range(3):    
    for j in range(size_num):
        for i in range(size_num):
            A[i][j][k] = k

#here we make the main changes as a function \phi:A->B to a new matrix B   
for j in range(size_num):
    for i in range(size_num):
        main_change(A, i, j, size_num)

#this function takes the states from A to a 2d numpy array B 
states_selector(A,B, size_num)

#below is a print if we want to see the map values
#print(B)

plt.imshow(B, cmap = cm.jet)
plt.show()
