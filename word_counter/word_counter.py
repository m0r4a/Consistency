def main():

    text_file = input("Enter the name of the text file: ")

    try:
        file = open(text_file, "r")
        text = file.read()
        words = text.split(" ")

        print("Word count:", len(words))

    except FileNotFoundError:
        print("Please enter a valid name")


main()
