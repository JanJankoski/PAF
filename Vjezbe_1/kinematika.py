import numpy as np
import matplotlib.pyplot as plt

# F = m*a
# a = F/m
# v = a*t
# x = 

def jednoliko_gibanje(F, m):
    x = []
    v = []
    a = []
    
    for t in range(1, 11):
        a.append(F/m)
        v.append(a[t-1]*t)
        x.append((a[t-1]*t*t)/2)

    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], x)
    plt.show()
    
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], v)
    plt.show()
    
    plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], a)
    plt.show()
