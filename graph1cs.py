from graphics import *

def main():
    win = GraphWin()
    p = Point(50,60)
    p.getX()
    p.getY()
    p.draw(win)
    p2 = Point(140,100)
    p2.draw(win)
    win.getMouse()
    win.close()


main()
