def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message")

    #get the message to econde

    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes: ")

    #loop through the message and print out the Unicode values for ch in message:
    for ch in message:
        print(ord(ch), end=" ")

    print()
main()
