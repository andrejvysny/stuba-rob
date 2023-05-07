import numpy as np
import matplotlib.pyplot as plt
import math

a = float(input("Zadajte dlzku strany stvorca [m]:"))

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

for i in range(4):

    # Forward
    Vr = a / 1
    Vl = a / 1
    [dX,dY,phi] = calc(Vr,Vl,1,phi)
    x +=dX
    y +=dY
    x_center.append(x)
    y_center.append(y)
    calcWheels(x,y)
    
    # Rotate 90
    for dt in np.arange(0, 1.0, 0.01):
        Vr = (math.pi * L) / 4
        Vl = -Vr
        [dX,dY,phi] = calc(Vr,Vl,0.01,phi)
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


"""

Pre výpočet vzdialenosti, ktorú prejde každé koleso pri otáčaní robota o 90 stupňov za 1 sekundu v diferenciálne riadenom robote, musíme zvážiť vzdialenosť prejdenú po kruhovej trajektórii, ktorá zodpovedá štvrtine kruhu s polomerom rovným vzdialenosti medzi kolesami. Na výpočet vzdialenosti po kruhovej trajektórii používame vzorec:

scss
Copy code
vzdialenosť = (obvod * uhol) / 360
kde obvod je obvod kruhu a uhol je uhol (v stupňoch), ktorým sa kruh prejde.

V našom prípade chceme, aby sa robot otočil o 90 stupňov, čo zodpovedá štvrtine kruhu. Preto je uhol 90 stupňov alebo π/2 radianov. Obvod štvrťkruhu je (π x vzdialenosť medzi kolesami) / 2. Preto je vzdialenosť, ktorú prejde každé koleso pri otáčaní robota o 90 stupňov:

scss
Copy code
vzdialenosť = (π x vzdialenosť medzi kolesami) / 4
Pre výpočet tohto môžete použiť vyššie uvedený kód v Pythone.


"""
