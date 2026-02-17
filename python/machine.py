emoticon = "^.^"


def main():
    global emoticon
    say("is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
