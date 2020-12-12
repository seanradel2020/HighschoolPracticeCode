from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n,probA, probB)
    printSummary(winsA,winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print("players called 'a' and 'b'. The ability of each player is")
    print("indicated by  a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always ")
    print("has the first serve")

def getInputs():
    #return the three simulation parameters
    a = float(input("Waht is the prob. player A wins a serve?"))
    b = float(input("Waht is the prob. player B wins a serve?"))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    #simulates n games of racquetball betwen players whose
    #abilities are represented by the probability of winning a serve
    #returns final scores for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1

    return winsA, winsB


def simOneGame(probA, probB):
    #simulates a games of racquetball betwen players whose
    #abilities are represented by the probability of winning a serve
    #returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA +1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    #a and b represent scores for a racquetball game
    #returns True if the game is over, False otherwise
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    #Prints a summary of wins for each player
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

main()
