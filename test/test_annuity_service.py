import unittest

from src.service.annuityService import get_annuity_mortgage


class TestAnnuityService(unittest.TestCase):
    def test_happy_path(self):
        actual = get_annuity_mortgage(amount=2000000, first_pay=200000, duration=5, interest_rate=11)
        expected = 39136.36
        self.assertEqual(expected, round(actual, 2))

    def test_float_interest(self):
        actual = get_annuity_mortgage(amount=2000000, first_pay=200000, duration=5, interest_rate=10.5)
        expected = 38689.02
        self.assertEqual(expected, round(actual, 2))

    def test_no_first_pay(self):
        actual = get_annuity_mortgage(amount=2000000, first_pay=0, duration=5, interest_rate=11)
        expected = 43484.85
        self.assertEqual(expected, round(actual, 2))

    def test_no_amount(self):
        actual = get_annuity_mortgage(amount=0, first_pay=0, duration=5, interest_rate=11)
        expected = 0
        self.assertEqual(expected, round(actual, 2))


if __name__ == '__main__':
    unittest.main()
