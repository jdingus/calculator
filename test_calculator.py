import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 5), -4)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 4), -8)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

    def test_square_root(self):
        self.assertAlmostEqual(self.calc.square_root(9), 3)
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    def test_percentage(self):
        self.assertEqual(self.calc.percentage(50, 200), 100)
        self.assertEqual(self.calc.percentage(25, 80), 20)

    def test_clear(self):
        self.calc.add(5, 3)
        self.calc.clear()
        self.assertEqual(self.calc.memory, 0)

if __name__ == '__main__':
    unittest.main()
