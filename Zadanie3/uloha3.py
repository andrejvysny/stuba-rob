import numpy as np
import matplotlib.pyplot as plt
import math

L = 0.2
R = 0.05

x = 0
y = 0

x_center = [x]
y_center = [y]

x_right = []
y_right = []

x_left = []
y_left = []


dt = 0.01
Vl = 0
Vr = 0
phi = 0.0



def calcWheels(x,y):
    x_left.append(x + math.cos(phi + math.pi/2)*(L/2))
    y_left.append(y + math.sin(phi + math.pi/2)*(L/2))

    x_right.append(x - math.cos(phi + math.pi/2)*(L/2))
    y_right.append(y - math.sin(phi + math.pi/2)*(L/2))


def calc(Vr,Vl,dt,phi):
    Vt = (Vr+Vl)/2
    Wt = (Vr-Vl)/L
    phi = phi + Wt*dt # zmena uhla otočenia od osi X
    
    Vx = Vt*math.cos(phi) # zmena polohy x v čase t + dt
    Vy = Vt*math.sin(phi) # zmena polohy y v čase t + dt
    
    dX = Vx*dt
    dY = Vy*dt
    return [dX,dY,phi]



calcWheels(0,0)


R1 = float(input("Polomer R1: "))
a = float(input("Strana a:"))
R2 = float(input("Polomer R2:"))



for dt in np.arange(0, 1.0, 0.01):
    Vt = (math.pi*float(R1))/100
    Wt = Vt/R1
    Vr = (2*Vt+L*Wt)/2
    Vl = (2*Vt-L*Wt)/2
    phi = phi + Wt*dt # zmena uhla otočenia od osi X 
    Vx = Vt*math.cos(phi) # zmena polohy x v čase t + dt
    Vy = Vt*math.sin(phi) # zmena polohy y v čase t + dt     
    dX = Vx*dt
    dY = Vy*dt
    x +=dX
    y +=dY
    x_center.append(x)
    y_center.append(y)
    calcWheels(x,y)


Vr = a / 1
Vl = a / 1
[dX,dY,phi] = calc(Vr,Vl,1,phi)
x +=dX
y +=dY
x_center.append(x)
y_center.append(y)
calcWheels(x,y)


for dt in np.arange(0, 1.0, 0.01):
    
    Vt = (math.pi*float(R2))/100
    Wt = -Vt/R2
    Vr = (2*Vt+L*Wt)/2
    Vl = (2*Vt-L*Wt)/2
    phi = phi + Wt*dt # zmena uhla otočenia od osi X  
    Vx = Vt*math.cos(phi) # zmena polohy x v čase t + dt
    Vy = Vt*math.sin(phi) # zmena polohy y v čase t + dt 
    dX = Vx*dt
    dY = Vy*dt
    x +=dX
    y +=dY
    x_center.append(x)
    y_center.append(y)
    calcWheels(x,y)
   
plt.figure(figsize=(10,10))
plt.axis('equal')
plt.plot(x_center,y_center, c="gray")
plt.plot(x_left,y_left,c="b")
plt.plot(x_right,y_right,c="r")
plt.show()
