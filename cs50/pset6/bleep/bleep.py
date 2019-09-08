from sys import argv


def main():
    # Check correct usage
    if len(argv) != 2:
        print("Usage: python bleep.py PATH_TO_FILE")
        quit(1)

    # Load word list
    arg = argv[1]
    bad_words = None

    with open(arg) as f:
        bad_words = [word[:-1] for word in f]

    # Ask user for input
    s = input("What message would you like to censor?\n")
    for w in s.split():
        if w.lower() in bad_words:
            s = s.replace(w, "*" * len(w))
    print(s)
    quit(0)


if __name__ == "__main__":
    main()
