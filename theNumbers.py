from graphics import *
import random

h = 1000
w = 800
def numbers2():
    screenBlack = Rectangle(Point(0,0),Point(1000,1000))
    #while(win.getMouse() == False):
    screenBlack.setFill("Black")
    screenBlack.draw(win)
    for i in range(10000000000):

        numbers2 = Text(Point(475,425),random.randint(0,9))

        numbers2.setFill("Red")
        numbers2.setSize(36)
        numbers2.setFace("helvetica")
        numbers2.setStyle("italic")
        numbers2.draw(win)
        numbers2.undraw()






def numbers():
    screenBlack = Rectangle(Point(0,0),Point(1000,1000))
    screenBlack.setFill("Black")
    screenBlack.draw(win)
    f = 0
    g = -5
    for i in range(100):
        f= 0
        g +=15

        for i in range(100):
            numbers1 = Text(Point(f,g),random.randint(0,9))
            numbers1.setFill("Red")
            numbers1.draw(win)
            f += 15




def errorScreen():

    colors = ["Black","White","Yellow","Cyan","Green","Pink","Red","Blue","Black"]
    #bar = Rectangle(Point(0,0), Point(125,400))
    #bar.setFill("green")
    #bar.setWidth(25)
    #bar.draw(win)
    a = 0
    b = 125
    d= 1000
    c = 875
    for i in range(8):
            bar = Rectangle(Point(a,0), Point(b,400))
            bar.setFill(colors[i])
            bar.draw(win)
            a+=125
            b+=125

    for i in range(8):
            bar = Rectangle(Point(d,400), Point(c,800))
            bar.setFill(colors[i])
            bar.draw(win)
            d-=125
            c-=125


win = GraphWin('The Numbers', 1000, 800)
errorScreen()
win.getMouse()

numbers()
win.getMouse()
numbers2()
win.getMouse()
win.close()
