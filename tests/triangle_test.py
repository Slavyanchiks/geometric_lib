from unittest import TestCase
from triangle import area, perimeter

class RectangleTestCase(TestCase) :
    def test_area_positive(self):
        self.assertEqual(area(2, 2), 2)
        self.assertEqual(area(12.78, 2), 12.78)
        self.assertEqual(area(0, 9), 0)

    def test_area_negative(self):
        with self.assertRaises(TypeError) as e:
            area("f", 3)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            area([4,"f"], 'bimbimbombom')
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            area(-3.5, 78)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(2, 4.6, 7.904), 14.504)
        self.assertEqual(perimeter(23.45, 2, 0), 25.45)
        self.assertEqual(perimeter(0, 3, 0), 3)

    def test_perimeter_negative(self):
        with self.assertRaises(TypeError) as e:
            perimeter("f", 3, 4.6)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            perimeter([4,"f"], 'bimbimbombom', -5)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            perimeter(-3, 8.9, 345)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])