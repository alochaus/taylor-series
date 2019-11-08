from sympy import Symbol, lambdify
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')

def graph(function, degree=0, string = ""):
    xvals = np.arange(-100,100,0.01)
    yvals = lambdify(x, function, 'numpy')(xvals)
    if not hasattr(yvals, '__len__'):
        k = yvals
        yvals = np.array([])
        for i in range(0, len(xvals)):
            yvals = np.append(yvals, k)

    if string == "":
        string = "Taylor polynomial (degree " + str(degree) +")"

    plt.ylim(-15, 15)
    plt.xlim(-20, 20)
    plt.plot(xvals, yvals, label=string)
