def main():
    celsius = eval(input("what is the celsius temperature"))
    fahrenheit = 9/5 *celsius +32
    print("The tempereature in fahrenheit is",fahrenheit,"degrees fahrenheit")

    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")

main()
