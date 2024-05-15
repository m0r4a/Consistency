import re


def main():
    text = open_readme()
    print(text[11])


def open_readme():
    with open('../README.md', 'r') as file:
        return file.readlines()


main()
