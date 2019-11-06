from sympy import Symbol, lambdify
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')

def graph(function, degree):
    xvals = np.linspace(-15,15,100)
    yvals = lambdify(x, function, 'numpy')(xvals)
    if not hasattr(yvals, '__len__'):
        k = yvals
        yvals = np.array([])
        for i in range(0, len(xvals)):
            yvals = np.append(yvals, k)
    plt.plot(xvals, yvals, label="Taylor polynomial (degree " + str(degree) +")")
    plt.axes().grid()
    plt.legend()
    plt.show()
