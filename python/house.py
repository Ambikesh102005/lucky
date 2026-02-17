name = input("What's your name? ")

match name:
    case "Harry" | "hermione" | "Ron":
        print("Gryffindor")
    case "Dreco":
        print("Slytherin")
    case _:
        print("Who?")
