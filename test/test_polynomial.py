from unittest import TestCase

from src.polynomial import Polynomial


class TestPolynomial(TestCase):
    p1 = None
    p2 = None
    p3 = None

    def setUp(self):
        self.p1 = Polynomial([5, 4, 3, 2, 1], 5)
        self.p2 = Polynomial([1], None)
        self.p3 = Polynomial([1, 0, 0, -5, 8], 10)

    def test_representation_polynomial(self):
        self.assertEqual('Polynomial([5, 4, 3, 2, 1], 5)', repr(self.p1))
        self.assertEqual('Polynomial([1], None)', repr(self.p2))
        self.assertEqual('Polynomial([1, 0, 0, -5, 8], 10)', repr(self.p3))

    def test_string_polynomial(self):
        self.assertEqual('x^4 + 2x^3 + 3x^2 + 4x + 5', str(self.p1))
        self.assertEqual('1', str(self.p2))
        self.assertEqual('8x^4 - 5x^3 + 1', str(self.p3))

    def test_degree_of_polynomial(self):
        self.assertEqual(4, len(self.p1))
        self.assertEqual(0, len(self.p2))

    def test_value_of_polynomial(self):
        self.assertEqual(975, abs(self.p1))
        self.assertEqual(1, abs(self.p2))
        self.assertEqual(75001, abs(self.p3))

    def test_adding(self):
        p4 = self.p1 + self.p2
        self.assertEqual('x^4 + 2x^3 + 3x^2 + 4x + 6', str(p4))

        p5 = self.p1 + self.p3
        self.assertEqual('9x^4 - 3x^3 + 3x^2 + 4x + 6', str(p5))

    def test_multiple_with_scalar(self):
        p4 = self.p1 * 2
        self.assertEqual('2x^4 + 4x^3 + 6x^2 + 8x + 10', str(p4))

        p5 = self.p2 * 2
        self.assertEqual('2', str(p5))

    def test_subtracting(self):
        p4 = self.p1 - self.p2
        self.assertEqual('x^4 + 2x^3 + 3x^2 + 4x + 4', str(p4))

        p5 = self.p1 - self.p3
        self.assertEqual('-7x^4 + 7x^3 + 3x^2 + 4x + 4', str(p5))
