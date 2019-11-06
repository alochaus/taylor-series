#!/usr/bin/env python3

from graph import *
from sympy import Derivative, lambdify, factorial, sin, cos, tan, sec, csc, cot, acos, asin, atan, asec, acsc, acot
import matplotlib.pyplot as plt
import numpy as np
import taylor

derivatives = []

function = input("Enter a function:\nf(x) = ")
x0 = int(input("x0 = "))
degree = int(input("Enter the degree of the Taylor polynomial: "))

derivative = function
for i in range(0, degree):
    derivative = Derivative(derivative, x) 
    derivative = derivative.doit()
    derivatives.append(derivative)

x1 = np.linspace(-15,15,100)
y1 = lambdify(x, function, 'numpy')(x1)
if not hasattr(y1, '__len__'):
    k = y1
    y1 = np.array([])
    for i in range(0, len(x1)):
        y1 = np.append(y1, k)
plt.plot(x1, y1, label=function)
taylor_polynomial = taylor.formPolynomial(function, derivatives, degree, x0)
graph(taylor_polynomial, degree)
