import sys

def french():
    print("Bonjour")

def english():
    print("Hello")


def main():
    if sys.argv[1] == "f":
        french()
    else:
        english()


if __name__ == "__main__":
    main()

