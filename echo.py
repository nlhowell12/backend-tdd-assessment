import argparse


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


def main():
    parser = create_parser().parse_args()

    if parser.title:
        print parser.text.title()
    elif parser.lower:
        print parser.text.lower()
    elif parser.upper:
        print parser.text.upper()
    else:
        print parser.text


if __name__ == "__main__":
    main()
