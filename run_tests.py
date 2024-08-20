import unittest
import sys
from termcolor import colored

class ColoredTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write(colored('OK', 'green'))
        self.stream.writeln()

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.write(colored('ERROR', 'red'))
        self.stream.writeln()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write(colored('FAIL', 'red'))
        self.stream.writeln()

if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = '.'
    suite = loader.discover(start_dir, pattern='test_*.py')

    runner = unittest.TextTestRunner(resultclass=ColoredTextTestResult, verbosity=2)
    result = runner.run(suite)

    sys.exit(not result.wasSuccessful())
