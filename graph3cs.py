from graphics import *

def main():
    print("This program plots the growth of a 10-year Investment")

    principal = eval(input("Input your starting amount ($):"))
    apr = eval(input("what is your annual percentage rate:"))

    win = GraphWin("Investment Growth Chart", 640,480)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1,0), '0.0k').draw(win)
    Text(Point(-1,2500), '2.5k').draw(win)
    Text(Point(-1,5000), '5.0k').draw(win)
    Text(Point(-1,7500), '7.5k').draw(win)
    Text(Point(-1,10000), '10.0k').draw(win)

    #height = principal * 0.02
    bar = Rectangle(Point(0,0), Point(1,principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        principal = principal * (1+apr)
        #x11 = year * 25 + 40
        #height = principal * 0.02
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)







    win.getMouse()
    win.close()


main()
