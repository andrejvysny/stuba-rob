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
    Ax = Rz(math.radians(90)-angleZ)@Tz(L1)@Tx(100)@S
    Ay = Rz(math.radians(90)-angleZ)@Tz(L1)@Ty(100)@S
    Az = Rz(math.radians(90)-angleZ)@Tz(L1)@Tz(100)@S
    B = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@S
    Bx = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@Tx(100)@S
    By = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@Ty(100)@S
    Bz = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@Tz(100)@S
    C = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@Ry(angleB)@Tz(L3)@S
    Cx = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@Ry(angleB)@Tz(L3)@Tx(100)@S
    Cy = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@Ry(angleB)@Tz(L3)@Ty(100)@S
    Cz = Rz(math.radians(90)-angleZ)@Tz(L1)@Ry(angleA)@Tz(L2)@Ry(angleB)@Tz(L3)@Tz(100)@S
    return np.array([S,A,B,C,Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz])


def printRobotArm(S,A,B,C,Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz, ax):
    ax.plot([S[0], A[0], B[0], C[0]], [S[1], A[1], B[1], C[1]], [S[2], A[2], B[2], C[2]], 'k', linewidth=2, label='Robotic Arm')
    ax.scatter([S[0], A[0], B[0], C[0]], [S[1], A[1], B[1], C[1]], [S[2], A[2], B[2], C[2]], c="orange", s=[30, 10, 10,20], alpha=1)

    ax.plot([A[0],Ax[0]],[A[1],Ax[1]],[A[2],Ax[2]], color="red", linewidth=0.7)
    ax.plot([A[0],Ay[0]],[A[1],Ay[1]],[A[2],Ay[2]], color="green", linewidth=0.7)
    ax.plot([A[0],Az[0]],[A[1],Az[1]],[A[2],Az[2]], color="blue", linewidth=0.7)

    ax.plot([B[0],Bx[0]],[B[1],Bx[1]],[B[2],Bx[2]], color="red", linewidth=0.7)
    ax.plot([B[0],By[0]],[B[1],By[1]],[B[2],By[2]], color="green", linewidth=0.7)
    ax.plot([B[0],Bz[0]],[B[1],Bz[1]],[B[2],Bz[2]], color="blue", linewidth=0.7)

    ax.plot([C[0],Cx[0]],[C[1],Cx[1]],[C[2],Cx[2]], color="red", linewidth=0.7)
    ax.plot([C[0],Cy[0]],[C[1],Cy[1]],[C[2],Cy[2]], color="green", linewidth=0.7)
    ax.plot([C[0],Cz[0]],[C[1],Cz[1]],[C[2],Cz[2]], color="blue", linewidth=0.7)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

x_horizontal = list()
y_horizontal = list()
step=2
for a in range(-90,91,step):
    S,A,B,C,Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz = CalcPoints(math.radians(a),math.radians(-55),math.radians(0))
    x_horizontal.append(C[0])
    y_horizontal.append(C[1])

for a in range(-90,91,step):
    S,A,B,C,Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz = CalcPoints(math.radians(a),math.radians(90),math.radians(0))
    x_horizontal.append(C[0])
    y_horizontal.append(C[1])


y_vertical = list()
z_vertical = list()
step=3

for b in range(-55,126,step):
       for c in range(0,151,step):
            S,A,B,C,Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz = CalcPoints(math.radians(0),math.radians(b),math.radians(c))
            y_vertical.append(C[1])
            z_vertical.append(C[2])

angleZ,angleA,angleB = 80,65,70
S,A,B,C,Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz = CalcPoints(math.radians(angleZ),math.radians(angleA),math.radians(angleB))
printRobotArm(S,A,B,C,Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz,ax)
ax.scatter(x_horizontal,y_horizontal,0, alpha=0.5)
ax.scatter(0,y_vertical,z_vertical,color="grey", alpha=0.05)


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