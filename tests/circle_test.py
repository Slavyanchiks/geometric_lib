from unittest import TestCase
from circle import area, perimeter

class CircleTestCase(TestCase) :
    def test_area_positive(self):
        self.assertEqual(area(4), 50.26548245743669)
        self.assertEqual(area(12.78), 513.1113015625751)
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(TypeError) as e:
            area("f")
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            area(-3)
        self.assertEqual('Radius cannot be negative', e.exception.args[0])

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(4), 25.132741228718345)
        self.assertEqual(perimeter(23.45), 147.3406954533613)
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(TypeError) as e:
            perimeter("f")
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            perimeter([4,"f"])
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            perimeter(-3.556)
        self.assertEqual("Radius cannot be negative", e.exception.args[0])