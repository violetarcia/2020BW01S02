import sys


def spanish():
    print("Hola, mundo")

def english():
    print("Hello")


def main():
    if sys.argv[1] == "s":
        spanish()
    else:
        english()


if __name__ == "__main__":
    main()

