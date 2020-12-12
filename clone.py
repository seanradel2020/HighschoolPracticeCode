from graphics import *

def main():
    win = GraphWin('Shapes')
    leftEye = Circle(Point(80,50), 5)
    leftEye.setFill('yellow')
    leftEye.setOutline('red')
    leftEye.draw(win)
    rightEye = leftEye.clone()
    rightEye.move(20,0)
    rightEye.draw(win)
    win.getMouse()
    win.close()


main()
