from unittest import TestCase
from square import area, perimeter

class SquareTestCase(TestCase) :
    def test_area_positive_normal(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(12.78), 163.3284)

    def test_area_positive_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_bigvalues(self):
        self.assertEqual(area(23726.9999999999999), 562970529.0)
        self.assertEqual(area(38484382378437), 1481047687049752285082562969)

    def test_area_negative_type_error(self):
        with self.assertRaises(TypeError) as e:
            area("f")
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

    def test_area_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            area(-3)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])

    def test_perimeter_positive_normal(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(23.45), 93.8)

    def test_perimeter_positive_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_bigvalues(self):
        self.assertEqual(perimeter(463434934739493), 1853739738957972)
        self.assertEqual(perimeter(8475857.54857845745), 33903430.19431383)
    def test_perimeter_negative_type_error(self):
        with self.assertRaises(TypeError) as e:
            perimeter("f")
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            perimeter([4,"f"])
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

    def test_perimeter_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            perimeter(-4)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])