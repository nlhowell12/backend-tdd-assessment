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
    if argument == 't':
        return title(text)
    elif argument == 'u':
        return upper(text)
    elif argument == 'l':
        return lower(text)


parser = create_parser().parse_args()

for i in sys.argv:
    if i[0] == '-':
        string = list(i[1:])
        for i in string:
            print convert(i, parser.text)

           
