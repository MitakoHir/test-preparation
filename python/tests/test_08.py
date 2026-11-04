import unittest
from task_08 import customer_totals


class Tests(unittest.TestCase):
    def test_суммы_по_убыванию(self):
        orders = [
            {"customer": "Анна", "amount": 100, "status": "paid"},
            {"customer": "Борис", "amount": 300, "status": "paid"},
            {"customer": "Анна", "amount": 50.5, "status": "paid"},
        ]
        self.assertEqual(customer_totals(orders), [("Борис", 300), ("Анна", 150.5)])

    def test_отменённые_не_учитываются(self):
        orders = [
            {"customer": "Анна", "amount": 100, "status": "paid"},
            {"customer": "Анна", "amount": 900, "status": "cancelled"},
        ]
        self.assertEqual(customer_totals(orders), [("Анна", 100)])
