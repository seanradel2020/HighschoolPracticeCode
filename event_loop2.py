from graphics import *

def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")

def handleClick(pt, win):
    #entry for user to type in
    entry = Entry(pt, 10)
    entry.draw(win)

    #go modal: loop until user types <enter> getKey
    while True:
        key = win.getKey()
        if key == "Return":
            break
    #undraw the entry and create and draw Text0
    entry.undraw()
    typed = entry.getText()
    Text(pt,typed).draw(win)

    #clear
    win.checkMouse()


def main():
    win = GraphWin("Color Window", 500,500)

    #event loop: handle key presses until user presses the "q" key
    while True:
        key = win.getKey()
        if key == "q":
            break
        if key:
            handleKey(key, win)
        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)


    win.close()

main()
