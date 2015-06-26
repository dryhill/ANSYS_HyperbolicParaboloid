#1. 根据给定的控制点，求解抛物面方程
#抛物面方程 z=(x-c)^2/a^2-y^2/b^2+d
#控制点： 凹脊线左端点、中心点、右端点，凹脊线的拱脚
#母线方程 (x-c)/a±y/b=0
#平面菱形投影的交点
e=82.418
f=38.67
#----------------------------
#4个控制点
p=[
(-62.1, 0,  30), 
(0,     0,  15.8), 
(62.1,  0,  40), 
(0, 36.577, 7.5)
]

x1=p[0][0]
y1=p[0][1]
z1=p[0][2]

x2=p[1][0]
y2=p[1][1]
z2=p[1][2]

x3=p[2][0]
y3=p[2][1]
z3=p[2][2]

x4=p[3][0]
y4=p[3][1]
z4=p[3][2]

#a,b,c,d 四个未知数
a=0
b=0
c=0
d=0

#1.求c
ta=2*(z3-z1)*(x1-x2)-2*(z2-z1)*(x1-x3)
tb=(-1)*(z3-z1)*(x2*x2-x1*x1)+(z2-z1)*(x3*x3-x1*x1)
c=tb/ta
#求a
ta=z2-z1
tb=(x2-c)**2-(x1-c)**2
a=(tb/ta)**0.5
#求d
d=z1-((x1-c)/a)**2
#求b
ta=(c/a)**2+d-z4
tb=y4**2/ta
b=tb**0.5

print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)


#print('z1', (x1-c)**2/a**2-y1**2/b**2+d)
#print('z2', (x2-c)**2/a**2-y2**2/b**2+d)
#print('z3', (x3-c)**2/a**2-y3**2/b**2+d)
#print('z4', (x4-c)**2/a**2-y4**2/b**2+d)

#曲面方程
def fxy(x, y):
    ''' 曲面函数'''
    z=((x-c)/a)**2-(y/b)**2+d
    return(z)

def fby(x):
    '''边界函数'''
    y=f-x*f/e
    return(y)

def fbyN(x):
    '''边界函数'''
    y=f+x*f/e
    return(y)

def fbx(y):
    '''边界函数'''
    x=e-y*e/f
    return(x)

print('Corner Point')
print(e, 0, fxy(e, 0))
print(0, f, fxy(0, f))
#求和平面投影边界的交点
#y=f/e*x
#间隔3m，输出一个l/h,l^2/h
print('Y方向-拱')
print('x,   y,   zCenter,  Zbound,  dz,   2*y/dz-l/h')
for x in range(-63, 0, 3):
    y=fbyN(x)
    z=fxy(x, y)
    z0=fxy(x, 0)
    dz=z0-z
    print(round(x, 2), round(y, 2), round(z0, 2),  round(z, 2),  round(dz, 2),  round(2*y/dz, 2))

for x in range(0, int(e), 3):
    y=fby(x)
    z=fxy(x, y)
    z0=fxy(x, 0)
    dz=z0-z
    print(round(x, 2), round(y, 2), round(z0, 2),  round(z, 2),  round(dz, 2),  round(2*y/dz, 2))


print('4*y*y/dz-l^2/h',  round(4*y*y/dz, 2))

print('X方向-索')
print('x,   y,   zCenter,  Zbound,  dz,   2*x/dz-l/h')
for y in range(0, int(f), 3):
    x=fbx(y)
    z=fxy(x, y)
    z0=fxy(0, y)
    dz=z-z0
    print(round(x, 2), round(y, 2), round(z0, 2),  round(z, 2),  round(dz, 2),  round(2*x/dz, 2))
    
print('4*x*x/dz-l^2/h',  round(4*x*x/dz, 2))

#print(fxy(62.1, 0))
#print(fxy(0, 36.577))
