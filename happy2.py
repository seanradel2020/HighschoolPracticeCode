def happy():
    return "Happy Birthday to you!\n"
def verseFor(person):
    lyrics = happy()*2+"Happy Birthday, dear "+person+".\n"+happy()
    return lyrics
def main():
    for person in ["Sean", "Jake", "Jack", "Magnus", "Donkey Kong"]:
        print(verseFor(person))

main()
