def main():
    print("This program converts a sequence of Unicode numbers into \n the string of the text that it represents. \n ")

    #get the message to enconde
    inString = input("Please enter the Unicode-encoded message: ")

    #loop through each substring and build Unicode message
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr) #convert digits to a number
        chars.append(chr(codeNum))

    message = "".join(chars)
    print("\nThe decoded message is: ", message)
main()
