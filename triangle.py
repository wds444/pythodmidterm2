import turtle
def drawTriangle(points,color,turtle):
    turtle.up()
    turtle.goto(points[0][0],points[0][1])
    turtle.down()
    turtle.goto(points[1][0],points[1][1])
    turtle.goto(points[2][0],points[2][1])
    turtle.goto(points[0][0],points[0][1])
def midpoint(p1,p2):
    return  [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
def serp(points,degree,turtle):
    drawTriangle(points,"",turtle)
    if degree>0:
        newpoints1=[points[0],midpoint(points[0],points[1]),midpoint(points[0],points[2])]
        serp(newpoints1,degree-1,turtle)
        newpoints2=[points[1],midpoint(points[1],points[0]),midpoint(points[1],points[2])]
        serp(newpoints2,degree-1,turtle)
        newpoints3=[points[2],midpoint(points[2],points[0]),midpoint(points[2],points[1])]
        serp(newpoints3,degree-1,turtle)

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
myPoints = [[-200,-100],[0,200],[200,-100]]
#drawTriangle(myPoints,"blue",myTurtle)
serp(myPoints,5,myTurtle)

myWin.exitonclick()
