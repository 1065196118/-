import matplotlib.pyplot as plt
#from Ipython.display import Image
from scipy import *
#import scipy.linalg as la
from scipy.special import jn,yn,jn_zeros,yn_zeros
#import numpy as np
n=0
x=0.0

print("J_%d(%f)=%f"%(n,x,jn(n,x)))
x=1.0
print("Y_%d(%f)=%f"%(n,x,yn(n,x)))
x=linspace(0,10,100)

fig,ax=plt.subplots()
for n in range(4):
    ax.plot(x,jn(n,x),label=r"$J_%d(x)$"%n)
ax.legend()
