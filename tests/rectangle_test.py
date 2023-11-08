from unittest import TestCase
from rectangle import area, perimeter

class RectangleTestCase(TestCase) :
    def test_area_positive(self):
        self.assertEqual(area(2, 2), 4)
        self.assertEqual(area(12.78, 23.45), 299.691)
        self.assertEqual(area(0, 9), 0)

    def test_area_negative(self):
        with self.assertRaises(TypeError) as e:
            area("f", 3)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            area([4,"f"], 'bimbimbombom')
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            area(-3, -4)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(2, 4), 12)
        self.assertEqual(perimeter(23.45, 2), 50.9)
        self.assertEqual(perimeter(0, 3), 6)

    def test_perimeter_negative(self):
        with self.assertRaises(TypeError) as e:
            perimeter("f", 3)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            perimeter([4,"f"], 'bimbimbombom')
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            perimeter(-3, -4)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])