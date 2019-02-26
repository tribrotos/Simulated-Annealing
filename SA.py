import math
import random
import numpy
from mpl_toolkits.mplot3d import  Axes3D
import matplotlib.pyplot as plt
import array

def inRandom():
    x1 = random.uniform(-10,10)
    x2 = random.uniform(-10,10)
    return x1,x2

def fungsi(x1,x2):
    return  -abs(math.sin(x1)*math.cos(x2)*math.exp(abs(1-math.sqrt(x1*x1+x2*x2)/3.14)))

def display(x1,x2,hasil):
    print("Pendinginan")
    print("X1 = "+str(x1))
    print("X2 = "+str(x2))
    print("Hasil = "+str(hasil))
    print("==============")

Tawal = 100
Takhir = 0.9
CR = 0.999
x1,x2 = inRandom()
currentState = fungsi(x1,x2)
BSF = currentState
xA = x1
xB = x2

solution = [BSF]
x1sol = array.array('f',[x1])
x2sol = array.array('f',[x2])

while (Tawal > Takhir):
    x1,x2 = inRandom()
    newState = fungsi(x1,x2)
    deltaE = newState - currentState
    if (deltaE < 0 ):
        currentState = newState
        BSF = newState

        display(x1,x2,newState)
        solution.append(BSF)
        x1sol.append(x1)
        x2sol.append(x2)
        xA,xB = x1,x2
    else:
        R = random.uniform(0,1)
        P = numpy.exp(-deltaE/Tawal)
        if (P > R):
            energi = newState
            BSF = newState
            solution.append(BSF)
            x1sol.append(x1)
            x2sol.append(x2)
            xA,xB = x1,x2
    Tawal = CR*Tawal

print("Hasil Terbaik")
print("X = "+str(xA))
print("Y = "+str(xB))
print("BSF = "+str(BSF))

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x1sol,x2sol,solution,c='r',marker='o')
# ax.set_xlabel('x1')
# ax.set_xlabel('x2')
# ax.set_xlabel('Hasil')
# plt.show()
