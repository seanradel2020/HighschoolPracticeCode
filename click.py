from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p=win.getMouse()
        print("you clicked at:", p.getX(), p.getY())

    input("Press <Enter> to close.")

main()
