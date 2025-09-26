import unittest
from data import get_total_cost
from data import get_report

class TestData(unittest.TestCase):
    def test_get_total_cost(self):
        data_set = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        total_cost = get_total_cost(data_set)
        self.assertEqual(total_cost, 15)

        data_set = []
        total_cost = get_total_cost(data_set)
        self.assertEqual(total_cost, 0)

    def test_get_report(self):
        pass

if __name__ == '__main__':
    unittest.main()