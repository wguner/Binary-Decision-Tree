from pyeda.inter import *

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
    j = create_node(j)
    formula = []
    formula.append(i)
    formula.append(j)
    return [item for elem in formula for item in elem]
