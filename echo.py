import argparse
import sys


def upper(text):
    return "".join([i.upper() for i in text])


def lower(text):
    return "".join([i.lower() for i in text])


def title(text):
    split = list(text)
    split[0] = split[0].upper()
    return "".join(split)


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
        return title(text)
    elif argument == 'u' or argument == 'upper':
        return upper(text)
    elif argument == 'l' or argument == 'lower':
        return lower(text)


parser = create_parser().parse_args()

if parser.title or parser.lower or parser.upper:
    for i in sys.argv:
        if i[0] == '-' and i[1] is not '-':
            string = list(i[1:])
            print convert(i, parser.text)
        elif i[0:2] == "--":
            string = i[2:]
            print convert(string, parser.text)

