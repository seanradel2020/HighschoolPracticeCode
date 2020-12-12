def main():
    print("Change Counter\n")

    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    nickles = eval(input("nickles: "))
    dimes = eval(input("dimes: "))
    pennies = eval(input("pennies: "))
    total=quarters*25+dimes*10+nickles+5+pennies
    print()
    print("The total value of the change is ${0}.{1:0>2} ".format(total//100,total%100))

main()
