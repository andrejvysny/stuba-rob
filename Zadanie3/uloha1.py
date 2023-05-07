import numpy as np
import matplotlib.pyplot as plt
import math

L = 0.2
R = 50
x = 0
y = 0

x_center = [x]
y_center = [y]
x_right = []
y_right = []
x_left = []
y_left = []

def calcWheels(x,y):
    x_left.append(x + math.cos(phi + math.pi/2)*(L/2))
    y_left.append(y + math.sin(phi + math.pi/2)*(L/2))

    x_right.append(x - math.cos(phi + math.pi/2)*(L/2))
    y_right.append(y - math.sin(phi + math.pi/2)*(L/2))

t_changes = np.array([0,5, 10,15,20])
Vl_changes = np.array([2,-2,1,2])
Vr_changes = np.array([2,1,1,-2])

dt = 0.01
Vl = 0
Vr = 0
phi = 0.0

calcWheels(0,0)

for t_current in np.arange(t_changes[0], t_changes[-1], dt):
    if np.isin(t_current, t_changes):
        index = np.where(t_changes == t_current)[0]
        Vl = Vl_changes[index][0]
        Vr = Vr_changes[index][0]

    Vt = (Vr+Vl)/2
    Wt = (Vr-Vl)/L
   
    phi = phi + Wt*dt # zmena uhla otočenia od osi X
    Vx = Vt*math.cos(phi) # zmena polohy x v čase t + dt
    Vy = Vt*math.sin(phi) # zmena polohy y v čase t + dt
    
    dX = Vx*dt
    dY = Vy*dt
    x += dX
    y += dY
    x_center.append(x)
    y_center.append(y)
    calcWheels(x,y)

plt.figure(figsize=(10,10))
plt.axis('equal')
plt.plot(x_center,y_center, c="gray",linewidth=2)
plt.plot(x_left,y_left,c="g",linewidth=1)
plt.plot(x_right,y_right,c="r",linewidth=1)
plt.show()
