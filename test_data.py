import unittest
from data import get_total_cost
from data import get_report

class TestData(unittest.TestCase):
    def test_get_total_cost_returns_accurate_cost(self):
        data_set = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        total_cost = get_total_cost(data_set)
        self.assertEqual(total_cost, 15)

        data_set = []
        total_cost = get_total_cost(data_set)
        self.assertEqual(total_cost, 0)

    def test_get_report_returns_correct_string(self):
        data_set = [(1.00, 'rent'), (2.01, 'groceries'), (3.02, 'gas')]
        self.assertEqual(get_report(data_set),
        'Total cost of all items: $6.03\n' +
        'Expense: rent Price: $1.0 Percent of total cost: 16.58%\n' +
        'Expense: groceries Price: $2.01 Percent of total cost: 33.33%\n' +
        'Expense: gas Price: $3.02 Percent of total cost: 50.08%\n')

if __name__ == '__main__':
    unittest.main()