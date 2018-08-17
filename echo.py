import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', action='store_true',
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true',
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true',
                        help='convert text to titlecase')
    return parser


def convert(argument, text):
    if argument == 't' or argument == 'title':
        return text.title()
    elif argument == 'u' or argument == 'upper':
        return text.upper()
    elif argument == 'l' or argument == 'lower':
        return text.lower()


def main():
    parser = create_parser().parse_args()

    if parser.title or parser.lower or parser.upper:
        for i in sys.argv:
            if i[0] == '-' and i[1] is not '-':
                print convert(i[-1], parser.text)
            elif i[0:2] == "--":
                string = i[2:]
                print convert(string, parser.text)
    else:
        print parser.text


if __name__ == "__main__":
    main()
