def happy():
    print("Happy Birthday to You!")

def sing(person):
    happy()
    happy()
    print("Happy Birthday, Dear", person + ".")
    happy()

def main():
    sing("Fred")
    print()
    sing("Ralph")
    print()
    sing("monkey")

main()
