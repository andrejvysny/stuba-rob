import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

L1 = 203 # [mm]
L2 = 178 # [mm]
L3 = 178 # [mm]

ATheta = (-90,90)
BTheta = (-55,125)
CTheta = (0,150)

def Rx(angle):
    return np.array([
        [1,0,0,0],
        [0, math.cos(angle), -math.sin(angle), 0],
        [0, math.sin(angle), math.cos(angle),0],
        [0, 0, 0, 1],
    ])
def Ry(angle):
    return np.array([
        [math.cos(angle),0,math.sin(angle),0],
        [0, 1, 0, 0 ],
        [-math.sin(angle),0, math.cos(angle),0],
        [0, 0, 0, 1],
    ])
def Rz(angle):
    return np.array([
        [math.cos(angle),-math.sin(angle),0,0],
        [math.sin(angle), math.cos(angle),0,0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

def Tx(d):
    return np.array([
        [1,0,0,d],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1],
    ])
def Ty(d):
    return np.array([
        [1,0,0,0],
        [0,1,0,d],
        [0,0,1,0],
        [0,0,0,1],
    ])
def Tz(d):
    return np.array([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,d],
        [0,0,0,1],
    ])


def CalcPoints(angleZ,angleA,angleB):
    S = np.array([0,0,0,1]).reshape(-1,1)
    A = Rz(math.radians(90)-angleZ)@Tz(L1)@S
    B = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@S
    C = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@Ry(angleB)@Tz(L3)@S
    return np.array([S,A,B,C])

def printRobotArm(array, ax):
    S,A,B,C = array
    ax.plot([S[0], A[0], B[0], C[0]], [S[1], A[1], B[1], C[1]], [S[2], A[2], B[2], C[2]], 'k', linewidth=2, label='Robotic Arm')
    ax.scatter([S[0], A[0], B[0], C[0]], [S[1], A[1], B[1], C[1]], [S[2], A[2], B[2], C[2]], c=['r', 'b', 'g', 'blue'], s=[100, 50, 50,100], alpha=1)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)


x_horizontal = list()
y_horizontal = list()
step=2
for a in range(-90,91,step):
    S,A,B,C = CalcPoints(math.radians(a),math.radians(-55),math.radians(0))
    x_horizontal.append(C[0])
    y_horizontal.append(C[1])

for a in range(-90,91,step):
    S,A,B,C = CalcPoints(math.radians(a),math.radians(90),math.radians(0))
    x_horizontal.append(C[0])
    y_horizontal.append(C[1])


y_vertical = list()
z_vertical = list()
step=3

for b in range(-55,126,step):
       for c in range(0,151,step):
            S,A,B,C = CalcPoints(math.radians(0),math.radians(b),math.radians(c))
            y_vertical.append(C[1])
            z_vertical.append(C[2])



printRobotArm(CalcPoints(math.radians(0),math.radians(-45),math.radians(45)),ax)
ax.scatter(x_horizontal,y_horizontal,0, alpha=0.5)
ax.scatter(0,y_vertical,z_vertical, alpha=0.1)


# Set the axis limits
ax.set_xlim([-L2-L3-10, L2+L3+10])
ax.set_ylim([-L2-L3-10, L2+L3+10])
ax.set_zlim([L1-L2-L3 + 10, L1+L2+L3])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()


fig = plt.figure()
plt.scatter(x_horizontal,y_horizontal, s=1)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

fig = plt.figure()
plt.scatter(y_vertical,z_vertical, s=1)
plt.xlabel('Y axis')
plt.ylabel('Z axis')

plt.show()