#Colby McBride
from Myro import *
from Graphics import *
from math import *


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

#DRAWING
WINSIZE = 700
win = Window("Pinball", WINSIZE, WINSIZE)
win.mode = "manual"
mid = WINSIZE/2
s = 600
r = 100

vertLine = Line((mid, 0),(mid, WINSIZE))
horLine = Line((0,mid),(WINSIZE, mid))
vertLine.draw(win)
horLine.draw(win)

point1 = Point(mid+s/2,mid + ((s*sqrt(3))/6))
point2 = Point(mid-s/2,mid + ((s*sqrt(3))/6))
point3 = Point(mid, mid - ((s*sqrt(3))/3))
circle1 = Circle(point1, r)
circle2 = Circle(point2, r)
circle3 = Circle(point3, r)
grey = makeColor(150,150,150)
circle1.draw(win)
circle1.fill = grey
circle1.outline = grey
circle2.draw(win)
circle2.fill = grey
circle2.outline = grey
circle3.draw(win)
circle3.fill = grey
circle3.outline = grey

cen = Point(mid,mid)
ball = Circle(cen, s/100)
ball.draw(win)
black = makeColor(0,0,0)
ball.fill = black

text = Text((WINSIZE-150,WINSIZE-50), "Number of hits: ")
text.setFill(black)
text.draw(win)
hitNum = 0
hits = Text((WINSIZE-50,WINSIZE-50), "{}".format(hitNum))
hits.setFill(black)
hits.draw(win)

win.update()

# INITIAL VALS
theta = radians(eval(input("Launch Angle (degrees): ")))
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

# INITIAL MOVEMENT
num=20
newX = (t*v[0], t*v[1])
for index in range(num):
    ball.move(newX[0]/num, -newX[1]/num)
    wait(.02)
    win.update()

if t != -1:
    hits.undraw()
    hitNum += 1
    hits = Text((WINSIZE-50,WINSIZE-50), "{}".format(hitNum))
    hits.setFill(black)
    hits.draw(win)
    win.update()


# LOOP BOUNCES
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
            wait(.02)
            win.update()

        hits.undraw()
        hitNum +=1
        hits = Text((WINSIZE-50,WINSIZE-50), "{}".format(hitNum))
        hits.setFill(black)
        hits.draw(win)
        win.update()

        cList.append(tempC)
        tempC = (cList[circleCount])
        cList.remove(cList[circleCount])

# BOUNCE OFF THE SCREEN AT END
while ball.getX()<WINSIZE and ball.getX()>0 and ball.getY()<WINSIZE and ball.getY()>0:
             ball.move(8*v[0], -8*v[1])
             wait(0.02)
             win.update()

print(hitNum)