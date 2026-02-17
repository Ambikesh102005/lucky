def get_words(filename):
    with open("address.txt", "r") as file:
        return file.read().lower().split()


def save_counts(counts):
    with open("counts.csv", "w") as file:
        file.write("Word,Count\n")
        for word, count in counts.items():
            file.write(f"{word},{count}\n")


def main():
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]
    counts = {word: lowercase_words.count(word) for word in words}
    save_counts(counts)


main()
