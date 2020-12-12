def main():
    principal = eval(input("Input your starting amount ($):"))
    apr = eval(input("what is your annual percentage rate:"))
    year = 1
    for i in range(10):
        principal = principal * (1+apr)
        print("Your balance after year",year,"is",principal)
        year = year + 1

        for i in range(10):
            principal = principal * (1+apr)

    print("this is your balance after another 10 years", principal)

main()
