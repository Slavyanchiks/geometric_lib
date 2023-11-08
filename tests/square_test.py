from unittest import TestCase
from square import area, perimeter

class SquareTestCase(TestCase) :
    def test_area_positive(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(12.78), 163.3284)
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(TypeError) as e:
            area("f")
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            area(-3)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(23.45), 93.8)
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(TypeError) as e:
            perimeter("f")
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            perimeter([4,"f"])
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            perimeter(-4)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])