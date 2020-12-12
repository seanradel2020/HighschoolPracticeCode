def main():
    print("This program generates computer usernames. \n")

#get the users first and last names
    first = input("Please enter your first name (All lowercase): ")
    last = input("Please enter your last name (All lowercase): ")

    #concatenate first initial with 7 chars of the last names
    uname = first[0] + last[:7]

    #output the username
    print("Your username is", uname)

main()
