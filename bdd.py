# Setenay Guner
# 11543877

from pyeda.boolalg.boolfunc import var
from pyeda.inter import *
from functools import reduce
from math import sqrt
from itertools import count, islice

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

# 3.1 

def bdd():
    # creating a bdd tree to match the requirements given in the assignment
    n = 0
    for i in range(0, 32): # 32 nodes
	    for j in range(0, 32):
		    if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32:
			    if n != 0:
				    f = create_edge(i, j) | f # | OR
			    else: 
				    f = create_edge(i, j)
				    n = 1
    return expr2bdd(f)


def bdd_even():
    # creating a bdd for EVEN
    n = 0
    for i in range(0, 32):
	    for j in range(0, 32):
		    if (j % 2) == 0: # checking y1....y5 if even
			    if n != 0:
				    f = create_edge(i, j) | f # | OR
			    else: 
				    f = create_edge(i, j)
				    n = 1
    return expr2bdd(f)

def is_prime(n):
    return n>2 and all( n% i for i in islice(count(2), int(sqrt(n)-1)))

def bdd_prime():
    # creating a bdd for PRIME
    n = 0
    for i in range(0, 32):
	    for j in range(0, 32):
		    if is_prime(i): # checking i1...i5 if prime
			    if n != 0:
				    f = create_edge(i, j) | f # | OR
			    else: 
				    f = create_edge(i, j)
				    n = 1
    return expr2bdd(f)

# 3.2 RR

def RR (bdd1, bdd2):
    # it takes two bdd and returns the composition 
    x = bddvars('x', 5)
    y = bddvars('y', 5)
    z = bddvars('z', 5)
    for i in range(0,5): #since it is x[0] & x[2]...x[4] for unsg bit rep. 
        bdd1 = bdd1.compose({x[i] : z[i]}) # compose(mapping): returns a bool func after substituting a subset
        bdd2 = bdd2.compose({z[i] : y[i]})
    bdd = bdd1 & bdd2
    return bdd.smoothing(z)

# 3.3 RR2*

def RRstar(rr):
    # used the algorithm that was given in class
    H = rr # H = R
    while True:
        r = H # H' = H
        H = r | RR(rr, r) # H = H' v (H' o R)
        if H is r: #until H = H'
            return H # return H

def main():
    x = bddvars('x', 5)
    y = bddvars('y', 5)
    # 3.4
    bdd1 = bdd()
    prime = bdd_prime()
    even = bdd_even()
    RR = RRstar(bdd1)
    RR_prime = RRstar(prime)
    RR_even = RRstar(even)
    # 3.5?
    test1 = RR.smoothing(x).smoothing(y)
    test2 = RR_prime.smoothing(x).smoothing(y)
    test3 = RR_even.smoothing(x).smoothing(y)
    test1 = test1.equivalent(True) # test1 before returns the existential quantification operator and we see if it is true here
    test2 = test2.equivalent(True)
    test3 = test3.equivalent(True)

if __name__ == "__main__":
    main()