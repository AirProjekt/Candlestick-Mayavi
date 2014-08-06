# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Rade\.spyder2\.temp.py
"""
# Create the data.
from numpy import pi, sin, cos, mgrid

u1, v1 = mgrid[0.0:pi:100j,0.0:2*pi:100j]
u2, v2 = mgrid[pi:2.0*pi:100j,0.0:2.0*pi:100j]
u, v = mgrid[0.0:2.0*pi:100j,0.0:8.0:100j]
u3, v3 = mgrid[3.0/2.0*pi:15.0/8.0*pi:100j,0.0:2*pi:100j]
u4, v4 = mgrid[pi/2.0:7.0/8.0*pi:100j,0.0:2*pi:100j]
u5, v5 = mgrid[0.0:1.0:100j,0.0:2.0*pi:100j]
t1 = mgrid[0.0:2.0*pi:100j]
u7, v7 = mgrid[0.5:1.0:100j,0.0:2.0*pi:100j]
u8, v8 = mgrid[0.0:1.0:100j,0.0:2.0*pi:100j]
u9, v9 = mgrid[-pi/2.0:pi/2.0:100j,0.0:2.0*pi:100j]
u10, v10 = mgrid[pi/2.0:3.0*pi/2.0:100j,0.0:2.0*pi:100j]
u11, v11 = mgrid[0.0:3.0*pi:100j,0.0:2.0*pi:100j]
u12, v12 = mgrid[0.0:1.0:100j,0.0:2.0*pi:100j]
u13, v13 = mgrid[0.0:1.0:100j,0.0:2.0*pi:100j]
u14, v14 = mgrid[0.0:1.0:100j,0.0:2.0*pi:100j]
u15, v15 = mgrid[0.0:8.0:100j,0.0:2.0*pi:100j]
#prvi model
x1 = 19+(13+3*cos(v1))*cos(u1)
y1 = 3*sin(v1)
z1 = 78+(13+3*cos(v1))*sin(u1);

x2 = 45+(13+3*cos(v2))*cos(u2)
y2 = 3*sin(v2)
z2 = 78+(13+3*cos(v2))*sin(u2);

x = 58+3*sin(u)
y = 3*cos(u)
z = 78+v

x3 = 58+(3+5*cos(u3))*sin(v3)
y3 = (3+5*cos(u3))*cos(v3)
z3 = 78+13+5*sin(u3)

x4 = 58+(14+6*cos(u4))*sin(v4)
y4 = (14+6*cos(u4))*cos(v4)
z4 = 78+13+5*sin(u4)

x5 = 58+6*u5*sin(v5)
y5 = 6*u5*cos(v5)
z5 = 78+18+0*u5

x6 = 58+6.5*cos(t1)
y6 = 6.5*sin(t1)
z6 = 78+18+0*t1

x7 = 58+14*u7*sin(v7)
y7 = 14*u7*cos(v7)
z7 = 78+18+0*u7

x8 = 58+((3+5*cos(15.0/8.0*pi))+(11+6*cos(7.0/8.0*pi)-5*cos(15.0/8.0*pi))*u8)*sin(v8)
y8 = ((3+5*cos(15.0/8.0*pi))+(11+6*cos(7.0/8.0*pi)-5*cos(15.0/8.0*pi))*u8)*cos(v8)
z8 = 78+(13+5*sin(15.0/8.0*pi))+(5*sin(7.0/8.0*pi)-5*sin(15.0/8.0*pi))*u8

x9 = (8+3*cos(u9))*sin(v9)
y9 = (8+3*cos(u9))*cos(v9)
z9 = 8+3*sin(u9)

x10 = (10+3*cos(u10))*sin(v10)
y10 = (10+3*cos(u10))*cos(v10)
z10 = 49+3*sin(u10)

x11 = (6+2*cos(u11))*sin(v11)
y11 = (6+2*cos(u11))*cos(v11)
z11 = 6.0/pi*u11 + 58

x12 = 8*sin(v12)
y12 = 8*cos(v12)
z12 = 11+29*u12

x13 = (8+2*u13)*sin(v13)
y13 = (8+2*u13)*cos(v13)
z13 = 40+6*u13

x14 = (8+2*u14)*sin(v14)
y14 = (8+2*u14)*cos(v14)
z14 = 58-6*u14

x15 = u15*sin(v15)
y15 = u15*cos(v15)
z15 = 5+0*u15

x16 = 1.2*u15*sin(v15)
y16 = 1.2*u15*cos(v15)
z16 = 76+0*u15

x17 = 1.2*u15*sin(v15)
y17 = 1.2*u15*cos(v15)
z17 = 78+0*u15

x18 = 9.6*sin(v15)
y18 = 9.6*cos(v15)
z18 = 76+0.25*u15

#drugi model
x1dr = (x1*cos(2.0*pi/5.0))-(y1*sin(2.0*pi/5.0))
y1dr = (x1*sin(2.0*pi/5.0))+(y1*cos(2.0*pi/5.0))
z1dr = 78+(13+3*cos(v1))*sin(u1);

x2dr = (x2*cos(2.0*pi/5.0))-(y2*sin(2.0*pi/5.0))
y2dr = (x2*sin(2.0*pi/5.0))+(y2*cos(2.0*pi/5.0))
z2dr = 78+(13+3*cos(v2))*sin(u2);

xdr = (x*cos(2.0*pi/5.0))-(y*sin(2.0*pi/5.0))
ydr = (x*sin(2.0*pi/5.0))+(y*cos(2.0*pi/5.0))
zdr = 78+v

x3dr = (x3*cos(2.0*pi/5.0))-(y3*sin(2.0*pi/5.0))
y3dr = (x3*sin(2.0*pi/5.0))+(y3*cos(2.0*pi/5.0))
z3dr = 78+13+5*sin(u3)

x4dr = (x4*cos(2.0*pi/5.0))-(y4*sin(2.0*pi/5.0))
y4dr = (x4*sin(2.0*pi/5.0))+(y4*cos(2.0*pi/5.0))
z4dr = 78+13+5*sin(u4)

x5dr = (x5*cos(2.0*pi/5.0))-(y5*sin(2.0*pi/5.0))
y5dr = (x5*sin(2.0*pi/5.0))+(y5*cos(2.0*pi/5.0))
z5dr = 78+18+0*u5

x6dr = (x6*cos(2.0*pi/5.0))-(y6*sin(2.0*pi/5.0))
y6dr = (x6*sin(2.0*pi/5.0))+(y6*cos(2.0*pi/5.0))
z6dr = 78+18+0*t1

x7dr = (x7*cos(2.0*pi/5.0))-(y7*sin(2.0*pi/5.0))
y7dr = (x7*sin(2.0*pi/5.0))+(y7*cos(2.0*pi/5.0))
z7dr = 78+18+0*u7

x8dr = (x8*cos(2.0*pi/5.0))-(y8*sin(2.0*pi/5.0))
y8dr = (x8*sin(2.0*pi/5.0))+(y8*cos(2.0*pi/5.0))
z8dr = 78+(13+5*sin(15.0/8.0*pi))+(5*sin(7.0/8.0*pi)-5*sin(15.0/8.0*pi))*u8

#treci model
x1tr = (x1*cos(2.0*pi/5.0*2.0))-(y1*sin(2.0*pi/5.0*2.0))
y1tr = (x1*sin(2.0*pi/5.0*2.0))+(y1*cos(2.0*pi/5.0*2.0))
z1tr = 78+(13+3*cos(v1))*sin(u1);

x2tr = (x2*cos(2.0*pi/5.0*2.0))-(y2*sin(2.0*pi/5.0*2.0))
y2tr = (x2*sin(2.0*pi/5.0*2.0))+(y2*cos(2.0*pi/5.0*2.0))
z2tr = 78+(13+3*cos(v2))*sin(u2);

xtr = (x*cos(2.0*pi/5.0*2.0))-(y*sin(2.0*pi/5.0*2.0))
ytr = (x*sin(2.0*pi/5.0*2.0))+(y*cos(2.0*pi/5.0*2.0))
ztr = 78+v

x3tr = (x3*cos(2.0*pi/5.0*2.0))-(y3*sin(2.0*pi/5.0*2.0))
y3tr = (x3*sin(2.0*pi/5.0*2.0))+(y3*cos(2.0*pi/5.0*2.0))
z3tr = 78+13+5*sin(u3)

x4tr = (x4*cos(2.0*pi/5.0*2.0))-(y4*sin(2.0*pi/5.0*2.0))
y4tr = (x4*sin(2.0*pi/5.0*2.0))+(y4*cos(2.0*pi/5.0*2.0))
z4tr = 78+13+5*sin(u4)

x5tr = (x5*cos(2.0*pi/5.0*2.0))-(y5*sin(2.0*pi/5.0*2.0))
y5tr = (x5*sin(2.0*pi/5.0*2.0))+(y5*cos(2.0*pi/5.0*2.0))
z5tr = 78+18+0*u5

x6tr = (x6*cos(2.0*pi/5.0*2.0))-(y6*sin(2.0*pi/5.0*2.0))
y6tr = (x6*sin(2.0*pi/5.0*2.0))+(y6*cos(2.0*pi/5.0*2.0))
z6tr = 78+18+0*t1

x7tr = (x7*cos(2.0*pi/5.0*2.0))-(y7*sin(2.0*pi/5.0*2.0))
y7tr = (x7*sin(2.0*pi/5.0*2.0))+(y7*cos(2.0*pi/5.0*2.0))
z7tr = 78+18+0*u7

x8tr = (x8*cos(2.0*pi/5.0*2.0))-(y8*sin(2.0*pi/5.0*2.0))
y8tr = (x8*sin(2.0*pi/5.0*2.0))+(y8*cos(2.0*pi/5.0*2.0))
z8tr = 78+(13+5*sin(15.0/8.0*pi))+(5*sin(7.0/8.0*pi)-5*sin(15.0/8.0*pi))*u8

#cetvrti model
x1cet = (x1*cos(2.0*pi/5.0*3.0))-(y1*sin(2.0*pi/5.0*3.0))
y1cet = (x1*sin(2.0*pi/5.0*3.0))+(y1*cos(2.0*pi/5.0*3.0))
z1cet = 78+(13+3*cos(v1))*sin(u1);

x2cet = (x2*cos(2.0*pi/5.0*3.0))-(y2*sin(2.0*pi/5.0*3.0))
y2cet = (x2*sin(2.0*pi/5.0*3.0))+(y2*cos(2.0*pi/5.0*3.0))
z2cet = 78+(13+3*cos(v2))*sin(u2);

xcet = (x*cos(2.0*pi/5.0*3.0))-(y*sin(2.0*pi/5.0*3.0))
ycet = (x*sin(2.0*pi/5.0*3.0))+(y*cos(2.0*pi/5.0*3.0))
zcet = 78+v

x3cet = (x3*cos(2.0*pi/5.0*3.0))-(y3*sin(2.0*pi/5.0*3.0))
y3cet = (x3*sin(2.0*pi/5.0*3.0))+(y3*cos(2.0*pi/5.0*3.0))
z3cet = 78+13+5*sin(u3)

x4cet = (x4*cos(2.0*pi/5.0*3.0))-(y4*sin(2.0*pi/5.0*3.0))
y4cet = (x4*sin(2.0*pi/5.0*3.0))+(y4*cos(2.0*pi/5.0*3.0))
z4cet = 78+13+5*sin(u4)

x5cet = (x5*cos(2.0*pi/5.0*3.0))-(y5*sin(2.0*pi/5.0*3.0))
y5cet = (x5*sin(2.0*pi/5.0*3.0))+(y5*cos(2.0*pi/5.0*3.0))
z5cet = 78+18+0*u5

x6cet = (x6*cos(2.0*pi/5.0*3.0))-(y6*sin(2.0*pi/5.0*3.0))
y6cet = (x6*sin(2.0*pi/5.0*3.0))+(y6*cos(2.0*pi/5.0*3.0))
z6cet = 78+18+0*t1

x7cet = (x7*cos(2.0*pi/5.0*3.0))-(y7*sin(2.0*pi/5.0*3.0))
y7cet = (x7*sin(2.0*pi/5.0*3.0))+(y7*cos(2.0*pi/5.0*3.0))
z7cet = 78+18+0*u7

x8cet = (x8*cos(2.0*pi/5.0*3.0))-(y8*sin(2.0*pi/5.0*3.0))
y8cet = (x8*sin(2.0*pi/5.0*3.0))+(y8*cos(2.0*pi/5.0*3.0))
z8cet = 78+(13+5*sin(15.0/8.0*pi))+(5*sin(7.0/8.0*pi)-5*sin(15.0/8.0*pi))*u8

#peti model
x1pet = (x1*cos(2.0*pi/5.0*4.0))-(y1*sin(2.0*pi/5.0*4.0))
y1pet = (x1*sin(2.0*pi/5.0*4.0))+(y1*cos(2.0*pi/5.0*4.0))
z1pet = 78+(13+3*cos(v1))*sin(u1);

x2pet = (x2*cos(2.0*pi/5.0*4.0))-(y2*sin(2.0*pi/5.0*4.0))
y2pet = (x2*sin(2.0*pi/5.0*4.0))+(y2*cos(2.0*pi/5.0*4.0))
z2pet = 78+(13+3*cos(v2))*sin(u2);

xpet = (x*cos(2.0*pi/5.0*4.0))-(y*sin(2.0*pi/5.0*4.0))
ypet = (x*sin(2.0*pi/5.0*4.0))+(y*cos(2.0*pi/5.0*4.0))
zpet = 78+v

x3pet = (x3*cos(2.0*pi/5.0*4.0))-(y3*sin(2.0*pi/5.0*4.0))
y3pet = (x3*sin(2.0*pi/5.0*4.0))+(y3*cos(2.0*pi/5.0*4.0))
z3pet = 78+13+5*sin(u3)

x4pet = (x4*cos(2.0*pi/5.0*4.0))-(y4*sin(2.0*pi/5.0*4.0))
y4pet = (x4*sin(2.0*pi/5.0*4.0))+(y4*cos(2.0*pi/5.0*4.0))
z4pet = 78+13+5*sin(u4)

x5pet = (x5*cos(2.0*pi/5.0*4.0))-(y5*sin(2.0*pi/5.0*4.0))
y5pet = (x5*sin(2.0*pi/5.0*4.0))+(y5*cos(2.0*pi/5.0*4.0))
z5pet = 78+18+0*u5

x6pet = (x6*cos(2.0*pi/5.0*4.0))-(y6*sin(2.0*pi/5.0*4.0))
y6pet = (x6*sin(2.0*pi/5.0*4.0))+(y6*cos(2.0*pi/5.0*4.0))
z6pet = 78+18+0*t1

x7pet = (x7*cos(2.0*pi/5.0*4.0))-(y7*sin(2.0*pi/5.0*4.0))
y7pet = (x7*sin(2.0*pi/5.0*4.0))+(y7*cos(2.0*pi/5.0*4.0))
z7pet = 78+18+0*u7

x8pet = (x8*cos(2.0*pi/5.0*4.0))-(y8*sin(2.0*pi/5.0*4.0))
y8pet = (x8*sin(2.0*pi/5.0*4.0))+(y8*cos(2.0*pi/5.0*4.0))
z8pet = 78+(13+5*sin(15.0/8.0*pi))+(5*sin(7.0/8.0*pi)-5*sin(15.0/8.0*pi))*u8
# View it.
from mayavi import mlab
s = mlab.mesh(x1, y1, z1,colormap = "autumn")
s = mlab.mesh(x2, y2, z2,colormap = "autumn")
s = mlab.mesh(x, y, z,colormap = "OrRd")
s = mlab.mesh(x3, y3, z3,colormap = "OrRd")
s = mlab.mesh(x4, y4, z4,colormap = "OrRd")
s = mlab.mesh(x5, y5, z5,colormap = "OrRd")
s = mlab.plot3d(x6, y6, z6, tube_radius=1)
s = mlab.mesh(x7, y7, z7,colormap = "PuOr")
s = mlab.mesh(x8, y8, z8,colormap = "OrRd")
s = mlab.mesh(x9, y9, z9,colormap = "bone")
s = mlab.mesh(x10, y10, z10,colormap = "bone")
s = mlab.mesh(x11, y11, z11,colormap = "bone")
s = mlab.mesh(x12, y12, z12,colormap = "bone")
s = mlab.mesh(x13, y13, z13,colormap = "bone")
s = mlab.mesh(x14, y14, z14,colormap = "bone")
s = mlab.mesh(x15, y15, z15,colormap = "Blues")
s = mlab.mesh(x16, y16, z16,colormap = "Blues")
s = mlab.mesh(x17, y17, z17,colormap = "Blues")
s = mlab.mesh(x18, y18, z18,colormap = "YlGnBu")
#Pregled drugog
s = mlab.mesh(x1dr, y1dr, z1dr,colormap = "autumn")
s = mlab.mesh(x2dr, y2dr, z2dr,colormap = "autumn")
s = mlab.mesh(xdr, ydr, zdr,colormap = "OrRd")
s = mlab.mesh(x3dr, y3dr, z3dr,colormap = "OrRd")
s = mlab.mesh(x4dr, y4dr, z4dr,colormap = "OrRd")
s = mlab.mesh(x5dr, y5dr, z5dr,colormap = "OrRd")
s = mlab.plot3d(x6dr, y6dr, z6dr, tube_radius=1)
s = mlab.mesh(x7dr, y7dr, z7dr,colormap = "PuOr")
s = mlab.mesh(x8dr, y8dr, z8dr,colormap = "OrRd")
#Pregled treceg
s = mlab.mesh(x1tr, y1tr, z1tr,colormap = "autumn")
s = mlab.mesh(x2tr, y2tr, z2tr,colormap = "autumn")
s = mlab.mesh(xtr, ytr, ztr,colormap = "OrRd")
s = mlab.mesh(x3tr, y3tr, z3tr,colormap = "OrRd")
s = mlab.mesh(x4tr, y4tr, z4tr,colormap = "OrRd")
s = mlab.mesh(x5tr, y5tr, z5tr,colormap = "OrRd")
s = mlab.plot3d(x6tr, y6tr, z6tr, tube_radius=1)
s = mlab.mesh(x7tr, y7tr, z7tr,colormap = "PuOr")
s = mlab.mesh(x8tr, y8tr, z8tr,colormap = "OrRd")
#Pregled cetvrtog
s = mlab.mesh(x1cet, y1cet, z1cet,colormap = "autumn")
s = mlab.mesh(x2cet, y2cet, z2cet,colormap = "autumn")
s = mlab.mesh(xcet, ycet, zcet,colormap = "OrRd")
s = mlab.mesh(x3cet, y3cet, z3cet,colormap = "OrRd")
s = mlab.mesh(x4cet, y4cet, z4cet,colormap = "OrRd")
s = mlab.mesh(x5cet, y5cet, z5cet,colormap = "OrRd")
s = mlab.plot3d(x6cet, y6cet, z6cet, tube_radius=1)
s = mlab.mesh(x7cet, y7cet, z7cet,colormap = "PuOr")
s = mlab.mesh(x8cet, y8cet, z8cet,colormap = "OrRd")
#Pregled petog
s = mlab.mesh(x1pet, y1pet, z1pet,colormap = "autumn")
s = mlab.mesh(x2pet, y2pet, z2pet,colormap = "autumn")
s = mlab.mesh(xpet, ypet, zpet,colormap = "OrRd")
s = mlab.mesh(x3pet, y3pet, z3pet,colormap = "OrRd")
s = mlab.mesh(x4pet, y4pet, z4pet,colormap = "OrRd")
s = mlab.mesh(x5pet, y5pet, z5pet,colormap = "OrRd")
s = mlab.plot3d(x6pet, y6pet, z6pet, tube_radius=1)
s = mlab.mesh(x7pet, y7pet, z7pet,colormap = "PuOr")
s = mlab.mesh(x8pet, y8pet, z8pet,colormap = "OrRd")

mlab.show()
