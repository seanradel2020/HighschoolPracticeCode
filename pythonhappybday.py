from random import randrange
#Random letters for _____ ________ (Happy Birthday)
#Print every random word string
#stop when the random string == happy Birthday

def main():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",
    "x","y","z"]


    #ad = letters[randrange(0,27)]
    i = 0
    jam = ""

    while i != 13:
        ad = letters[randrange(0,26)]
        jam= jam + ad
        while i == 4:
            bb = " "
            jam = jam + bb
            break



        i = i+1
        if i == 13 and jam != "happy birthday":
            print(jam)
            i = 0
            jam = ""
        if i == 13 and jam == "happy birthday":
            print(jam)
            print("happy birthday aidan!!!")
            break

    #print(ad)

main()
