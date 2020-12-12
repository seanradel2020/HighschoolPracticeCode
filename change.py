def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    nickles = eval(input("nickles: "))
    dimes = eval(input("dimes: "))
    pennies = eval(input("pennies: "))
    total=quarters*.25+dimes*.10+nickles*.05+pennies*.01
    print()
    print("The total value of the change is ${0:0.2f} ".format(total))

main()
