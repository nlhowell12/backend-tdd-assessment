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
        """'-u' or '--upper' should convert text to uppercase"""
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '-u']).upper)
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '--upper']).upper)

    def test_lower(self):
        """'-l' or '--lower' should convert text to lowercase"""
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '-l']).lower)
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '--lower']).lower)

    def test_title(self):
        """'-t' or '--title' should convert text to titlecase"""
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '-t']).title)
        self.assertTrue(
            echo.create_parser().parse_args(['hello', '--title']).title)

    def test_all(self):
        """Multiple arguments should resolve in order of usage (-t, -l, -u)"""
        test = subprocess.Popen(
            ["python", "./echo.py", "-utl", 'hello'],
            stdout=subprocess.PIPE).communicate()
        self.assertEqual(test[0].split(), ["Hello"])
        test = subprocess.Popen(
            ["python", "./echo.py", "-ul", 'hello'],
            stdout=subprocess.PIPE).communicate()
        self.assertEqual(test[0].split(), ["hello"])

    def test_none(self):
        """No arguments should return the original unaltered text"""
        process = subprocess.Popen(
            ["python", "./echo.py", 'hello'],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout.split(), ['hello'])


if __name__ == '__main__':
    unittest.main()
