from pyeda.boolalg.boolfunc import var
from pyeda.inter import *
from functools import reduce


def create_node(num):
	# Converts a number into binary then to an array of 5 bits
    binary = ('{0:05b}'.format(num))
    str2arr = []
    for elem in binary:
        str2arr.append(elem)
    return [int(intList) for intList in str2arr]

def create_edge(i, j):
	# takes two numbers converts to binary array then appends it to a new list
    # [0, 1, 1, 0, 0, 0, 1, 0, 1, 1]
    i = create_node(i)
    exp1 = create_bool_express('x', i)
    j = create_node(j)
    exp2 = create_bool_express('y', j)
    #return [item for elem in formula for item in elem]
    return exp1 & exp2
    # logic_not(x1) logic_and logic(x2)....

def create_bool_express(name, inputArr):
    # name : x, y, z and inpurArr: an array of 1 and 0s
    logic_exp = bddvars(name, 5) 
    logic_exp = [var if n else ~var for var, n in zip(logic_exp, inputArr)]# var return a unique var instance
    return reduce(lambda x, y: x & y, logic_exp) # returns expression not diagram

def bdd():
    # creating a bdd tree to match the requirements given in the assignment
    n = 0
    for i in range(0, 32): # 32 nodes
	    for j in range(0, 32):
		    if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32:
			    if n != 0:
				    f = create_bool_express(i, j) | f # | OR
			    else: 
				    f = create_bool_express(i, j)
				    n = 1
    return expr2bdd(f)
