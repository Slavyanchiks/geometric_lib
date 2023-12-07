from unittest import TestCase
from rectangle import area, perimeter

class RectangleTestCase(TestCase) :
    def test_area_positive_int(self):
        self.assertEqual(area(2, 2), 4)

    def test_area_positive_bigint(self):
        self.assertEqual(area(4563746545, 66578), 303845117473010)

    def test_area_positive_zero(self):
        self.assertEqual(area(0, 9), 0)
        self.assertEqual(area(3.567, 0), 0)

    def test_area_positive_float(self):
        self.assertEqual(area(2.3, 5.6), 12.88)

    def test_area_positive_bigfloat(self):
        self.assertEqual(area(2343.5745485, 67.657457), 158560.29424143318)

    def test_area_negative_type_error(self):
        with self.assertRaises(TypeError) as e:
            area("f", 3)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            area([4,"f"], 'bimbimbombom')
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

    def test_area_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            area(-3, -4)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])

    def test_perimeter_positive_int(self):
        self.assertEqual(perimeter(2, 4), 12)

    def test_perimeter_positive_bigint(self):
        self.assertEqual(perimeter(23829372392, 2383827382), 52426399548)

    def test_perimeter_positive_zero(self):
        self.assertEqual(perimeter(0, 3), 6)
        self.assertEqual(perimeter(3.56, 0), 7.12)

    def test_perimeter_positive_float(self):
        self.assertEqual(perimeter(2.56, 4.44), 14.0)

    def test_perimeter_positive_bigfloat(self):
        self.assertEqual(perimeter(2348549.68574845845, 67594.4546238464), 4832288.280744609)

    def test_perimeter_negative_type_error(self):
        with self.assertRaises(TypeError) as e:
            perimeter("f", 3)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            perimeter([4,"f"], 'bimbimbombom')
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

    def test_perimeter_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            perimeter(-3, -4)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])