from sympy import factorial, sin, cos, tan, sec, csc, cot, acos, asin, atan, asec, acsc, acot
from graph import x

def formPolynomial(function, derivatives, degree, x0):
    polynomial = 0
    for i in range(0, degree+1):
        if i == 0:
            try:
                polynomial += eval(function).subs(x, x0)
            except:
                polynomial = eval(function)
        else:
            try:
                derivatives[i-1] = derivatives[i-1].subs(x, x0)
            except:
                derivatives[i-1] = derivatives[i-1]
            polynomial += (derivatives[i-1] * (x-x0)**i)/factorial(i)
    return polynomial
