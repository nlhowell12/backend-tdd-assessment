import subprocess
import unittest
import echo


class TestEcho(unittest.TestCase):

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        self.assertEqual(echo.upper('hello'), 'HELLO')
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '-u']).upper)
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '--upper']).upper)

    def test_lower(self):
        self.assertEqual(echo.lower('Hello'), 'hello')
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '-l']).lower)
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '--lower']).lower)

    def test_title(self):
        self.assertEqual(echo.title('hello'), 'Hello')
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '-t']).title)
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '--title']).title)

    def test_all(self):
        test = subprocess.Popen(
            ["python", "./echo.py", "-utl", 'hello'],
            stdout=subprocess.PIPE).communicate()
        self.assertEqual(test, ["HELLO", "Hello", "hello"])

    def test_none(self):
        process = subprocess.Popen(
            ["python", "./echo.py", 'hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        print stdout
        self.assertEqual(stdout.split()[0], 'hello')


if __name__ == '__main__':
    unittest.main()
