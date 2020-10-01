import numpy as np

#--------Enter your function here---------
def f(x):
    y = x*x
    return y

if __name__ == "__main__":
    #-----Enter your accuracy here-----
    accuracy = 0.01

    # lower bound
    a = 0

    # upper bound
    b = 2

    # current accuracy/length
    l = b-a

    # Golden ratio part 1:
