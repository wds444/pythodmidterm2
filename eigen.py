import turtle
from random import randint


myWin = turtle.Screen()
myPoints = [[-200,-100],[0,200],[200,-100]]
#easy shorthands
a=myPoints[0]
b=myPoints[1]
c=myPoints[2]

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def getRandPoint():#extreme values clipped so point is more probable to lie in triangle
    return [randint(-100,100),randint(-100,100)]

def plotPoint(p):
    turtle.goto(p)
    turtle.dot()

def getRandVert():
    r=randint(0,2)
    if r==0:
        return a
    elif r==1:
        return b
    else:
        return c




turtle.up()
p=getRandPoint()
turtle.speed(0)


for i in range(0,3000):
    p=getMid(p,getRandVert())
    plotPoint(p)
    #enable to see counter
   #print(i)



    #Take 3 points in a plane to form a triangle, you need not draw it.
  #  Randomly select any point inside the triangle and consider that your current position.
   # Randomly select any one of the 3 vertex points.
    #Move half the distance from your current position to the selected vertex.
    #Plot the current position.
    #Repeat from step 3.



myWin.exitonclick()
