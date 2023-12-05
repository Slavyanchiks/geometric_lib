from unittest import TestCase
from circle import area, perimeter

class CircleTestCase(TestCase) :
    def test_area_positive_normal(self):
        self.assertEqual(area(4), 50.26548245743669)
        self.assertEqual(area(12.78), 513.1113015625751)

    def test_area_positive_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_bigvalues(self):
        self.assertEqual(area(738478394), 1.7132686167652877e+18)
        self.assertEqual(area(127547.8885675867), 51108886604.471275)

    def test_area_negative_type_error(self):
        with self.assertRaises(TypeError) as e:
            area("f")
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

    def test_area_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            area(-3)
        self.assertEqual('Radius cannot be negative', e.exception.args[0])

    def test_perimeter_positive_normal(self):
        self.assertEqual(perimeter(4), 25.132741228718345)
        self.assertEqual(perimeter(23.45), 147.3406954533613)

    def test_perimeter_positive_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_bigvalues(self):
        self.assertEqual(perimeter(2329384293283), 14635953166330.65)
        self.assertEqual(perimeter(394384394.4844), 2477990232.8052998)

    def test_perimeter_negative_type_error(self):
        with self.assertRaises(TypeError) as e:
            perimeter("f")
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            perimeter([4,"f"])
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

    def test_perimeter_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            perimeter(-3.556)
        self.assertEqual("Radius cannot be negative", e.exception.args[0])