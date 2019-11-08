#!/usr/bin/env python3

from graph import *
from sympy import Derivative, lambdify, factorial, sin, cos, tan, sec, csc, cot, acos, asin, atan, asec, acsc, acot
import matplotlib.pyplot as plt
import numpy as np
import taylor

derivatives = []
degrees = []

function = input("Enter a function:\nf(x) = ")
a = int(input("a = "))
while True:
    degrees.append(int(input("Enter the degree of the Taylor polynomial: "))) 
    if degrees[-1] == -1:
        degrees.pop()
        break

derivative = function
for i in range(0, max(degrees)):
    derivative = Derivative(derivative, x) 
    derivative = derivative.doit()
    derivatives.append(derivative)

for i in range(0, len(degrees)):
    graph(taylor.formPolynomial(function, derivatives, degrees[i], a), degrees[i])
graph(eval(function), string=function)
plt.gca().set_aspect('equal', adjustable='datalim')
plt.axes().grid()
plt.legend()
plt.show()
