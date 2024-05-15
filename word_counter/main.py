def main():

    text_file = input("Enter the name of the text file: ")

    text = open_text(text_file)

    print("Word count:", word_count(text))


def open_text(text_file_name):

    try:
        if len(text_file_name.split(".")) > 1:
            text = open(text_file_name, "r")

        else:
            text = open(text_file_name + ".txt", "r")

    except FileNotFoundError:
        print("Select a valid .txt please")
        exit(1)

    return text


def word_count(file_name):
    text = file_name.read()
    return len(text.split(" "))


main()
