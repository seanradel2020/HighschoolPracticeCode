def main():
    n = int(input("How many numbers do you have?"))
    total = 0.0

    for i in range(n):

        number = int(input("Enter your number: "))
        total = total + number

    print("your average is... ", total/n)

main()
