from unittest import TestCase
from triangle import area, perimeter

class TriangleTestCase(TestCase) :
    def test_area_positive_int(self):
        self.assertEqual(area(2, 2), 2)

    def test_area_positive_float(self):
        self.assertEqual(area(12.78, 2.4), 15.335999999999999)

    def test_area_positive_zero(self):
        self.assertEqual(area(0, 9), 0)
        self.assertEqual(area(4.54, 0), 0)

    def test_area_positive_bigint(self):
        self.assertEqual(area(182817328323723823, 238273723527323), 2.1780282772505404e+31)

    def test_area_positive_bigfloat(self):
        self.assertEqual(area(28372.85784983, 9793873.999999999999), 138940097400.57297)

    def test_area_positive_mixedtypes(self):
        self.assertEqual(area(2, 3.54), 3.54)
        self.assertEqual(area(38473438.6756956, 8), 153893754.7027824)

    def test_area_negative_type_error(self):
        with self.assertRaises(TypeError) as e:
            area("f", 3)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            area([4,"f"], 'bimbimbombom')
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

    def test_area_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            area(-3.5, 78)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])

    def test_perimeter_positive_int(self):
        self.assertEqual(perimeter(2, 4, 9), 15)

    def test_perimeter_positive_float(self):
        self.assertEqual(perimeter(3.4, 8.9895, 4.356), 16.7455)

    def test_perimeter_positive_zero(self):
        self.assertEqual(perimeter(2, 4, 0), 6)
        self.assertEqual(perimeter(4.5, 0, 3.5), 8)
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(0, 0, 34.6), 34.6)

    def test_perimeter_positive_bigint(self):
        self.assertEqual(perimeter(22632737236237, 37348236874325, 234589248528354), 294570222638916)

    def test_perimeter_positive_bigfloat(self):
        self.assertEqual(perimeter(3487364.8745585747, 9.433434343477, 47343743493.87878787878787), 47347230868.186775)

    def test_perimeter_positive_mixedtypes(self):
        self.assertEqual(perimeter(2, 45466.565656565656, 574875485475495), 574875485520963.6)
        self.assertEqual(perimeter(898654.7736, 7, 8.4), 898670.1736)

    def test_perimeter_negative_type_error(self):
        with self.assertRaises(TypeError) as e:
            perimeter("f", 3, 4.6)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            perimeter([4,"f"], 'bimbimbombom', -5)
        self.assertEqual('Arguments should be int or float type', e.exception.args[0])

    def test_perimeter_negative_value_error(self):
        with self.assertRaises(ValueError) as e:
            perimeter(-3, 8.9, 345)
        self.assertEqual("Sides' length cannot be negative", e.exception.args[0])