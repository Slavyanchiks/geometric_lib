from unittest import TestCase
from rectangle import area, perimeter


class RectangleTestCase(TestCase) :
    def test_area(self):
        self.assertEqual(area(2, 2), 4)