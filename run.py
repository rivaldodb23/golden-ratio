import numpy as np
import math

#--------Enter your function here---------
def f(x):
    y = x*x
    return y

# ----- Helper function for print ------
def out(i ,a, x1, x2, b, fx1, fx2):
    print("Step ", "\ta = ", a, "\tx1 = ", x1, "\tx2 = ", x2, "\t", "\tb = ", b, "\tf(x1) = ", f(x1), "\tf(x2) = ", f(x2))

if __name__ == "__main__":
    # golden rario
    psi = 0.5*(1+math.sqrt(5))
    print("Golden ratio is ", psi)

    # is min/max
    isMin = True

    #-----Enter your accuracy here-----
    accuracy = 0.001

    # lower bound
    a = 0

    # upper bound
    b = 2

    # current accuracy/length
    curr_acc = b-a

    # Golden ratio part 1:
    x1 = b - (1/psi) * curr_acc
    x2 = a + (1/psi) * curr_acc

    i = 3
    while (curr_acc > accuracy):
        if (isMin) :
            if f(x1) < f(x2):
                b = x2
                x2 = x1
                x1 = b - (1/psi) * (b-a)
                curr_acc = b - x1
            else:
                a = x1
                x1 = x2
                x2 = a + (1/psi) * (b-a)
                curr_acc = x2 - a
        else :
            if f(x1) >= f(x2):
                b = x2
                x2 = x1
                x1 = b - (1/psi) * (b-a)
                curr_acc = b - x1
            else:
                a = x1
                x1 = x2
                x2 = a + (1/psi) * (b-a)
                curr_acc = x2 - a
        
        out(i ,a, x1, x2, b, f(x1), f(x2))
        i = i + 1