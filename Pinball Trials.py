#Colby McBride
from Myro import *
from Graphics import *
from math import *
from random import *


#HELPER FUNCTIONS
def intersect(c, r, x, v):
    vec = (c[0] - x[0], c[1] - x[1])
    vecDot = vec[0]*v[0] + vec[1]*v[1]
    D = vecDot**2 - (vec[0]**2 + vec[1]**2) + r**2
    if vecDot <= 0 or D <= 0:
        return -1
    else:
        return vecDot - sqrt(D)

def reflect(c, x, v):
    vec = (c[0] - x[0], c[1] - x[1])
    vecDot = vec[0]*v[0] + vec[1]*v[1]
    foo = (vecDot * 2) /(vec[0]**2 + vec[1]**2)
    bar = (vec[0]*foo, vec[1]*foo)
    w = (v[0] - bar[0], v[1] - bar[1])
    return w

def pinball(start):
#DRAWING
    WINSIZE = 500
    mid = WINSIZE/2
    s = 6
    r = 1
    
    point1 = Point(mid+s/2,mid + ((s*sqrt(3))/6))
    point2 = Point(mid-s/2,mid + ((s*sqrt(3))/6))
    point3 = Point(mid, mid - ((s*sqrt(3))/3))
    circle1 = Circle(point1, r)
    circle2 = Circle(point2, r)
    circle3 = Circle(point3, r)

    
    cen = Point(mid,mid)
    ball = Circle(cen, s/100)

    hitNum = 0
    

    # INITIAL VALS
    theta = radians(start)
    v = (cos(theta), sin(theta))
    x = (ball.getX() - mid, mid - ball.getY())
    cList = [(circle1.getX() -mid, mid - circle1.getY()),(circle2.getX() -mid, mid - circle2.getY()),(circle3.getX() -mid, mid - circle3.getY())]
    circleCount = -1
    for c in cList:
        t = -1
        tVal = intersect(c, r, x,v)
        circleCount+=1
        if tVal != -1:
            t = tVal
            break
    
    
    tempC = (cList[circleCount])
    cList.remove(cList[circleCount])
    
    # INITIAL DRAW
    num=1
    newX = (t*v[0], t*v[1])
    for index in range(num):
        ball.move(newX[0]/num, -newX[1]/num)

    if t != -1:
        hitNum += 1

    
    
    # LOOP DRAW
    while t != -1:
        t=-1
        x = (ball.getX() - mid, mid - ball.getY())
        v = reflect(tempC, x,v)
        circleCount = -1
        for c in cList:
            tVal = intersect(c, r, x,v)
            if tVal != -1 and (tVal<t or t==-1):
                t = tVal
                circleCount = cList.index(c)
        if t != -1:
            for index in range(num):
                ball.move(t*v[0]/num, -t*v[1]/num)


            hitNum +=1

            cList.append(tempC)
            tempC = (cList[circleCount])
            cList.remove(cList[circleCount])


    return(hitNum)





#Systematic method:
aList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for b in range(720000):
    if 70<(b/20)<110 or 190<(b/20)<230 or 310<(b/20)<350:
        spot = pinball(b/20)
        aList[spot] = aList[spot]  + 1
    else:
        aList[0] = aList[0] + 1
print(aList)

#Random method:
## bigList = []
## aList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
## for b in range(7200):
##     input = random() * 1000
##     if 70<(input%360)<110 or 190<(input%360)<230 or 310<(input%360)<350:
##         spot = pinball(input)
##         aList[spot] = aList[spot]  + 1
##         if spot >=4:
##             bigList.append((b,spot,input%360))
##     else:
##         aList[0] = aList[0] + 1
## print(aList)
## print(bigList)