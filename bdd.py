#from pyeda.inter import *

def create_var(num):
	# Converts a number into binary then to an array of 5 bits
    binary = ('{0:05b}'.format(num))
    str2arr = []
    for elem in binary:
        str2arr.append(elem)
    return [int(intList) for intList in str2arr]

def create_bool_formula(i, j):
	# takes to numbers converts to binary array then appends it to a new list
	ex1 = var_expression('x', create_var(i))
	ex2 = var_expression('y', create_var(j))
	return ex1 & ex2
