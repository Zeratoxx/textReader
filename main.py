from textReader import TextReader


def main():
    reader = TextReader("inputText.txt")
    while reader.has_next_line():
        print(reader.get_next_line(), end="")


if __name__ == '__main__':
    main()
