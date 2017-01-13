from unittest import TestCase

from src.polynomial import Polynomial


class TestPolynomial(TestCase):
    p1 = None

    def setUp(self):
        self.p1 = Polynomial([5, 4, 3, 2, 1], 5)

    def test_representation_polynomial(self):
        representation = repr(self.p1)
        self.assertEqual('Polynomial([5, 4, 3, 2, 1], 5)', representation)
