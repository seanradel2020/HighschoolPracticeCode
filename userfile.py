def main():
    print("This program creates a file of usernames from a. \nfile of names")

    #get the file names
    infileName = input("What are the names in?")
    outfileName = input("What file should the usernames go in?")

    infile = open(infileName, "r")
    outfile= open(outfileName, "w")

    #concatenate first initial with 7 chars of the last names
    for line in infile:
        first,last = line.split()

        uname = (first[0] + last[:7]).lower()

        print(uname, file = outfile)

    infile.close()
    outfile.close()

main()
