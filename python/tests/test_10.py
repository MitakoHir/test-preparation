import unittest
from task_10 import drop_cancelled, average_check


class Tests(unittest.TestCase):
    def test_убирает_отменённый_заказ(self):
        orders = [{"status": "paid"}, {"status": "cancelled"}, {"status": "paid"}]
        self.assertEqual(drop_cancelled(orders), [{"status": "paid"}, {"status": "paid"}])

    def test_средний_чек(self):
        self.assertEqual(average_check([{"amount": 100}, {"amount": 200}]), 150)

    def test_средний_чек_пустого_списка(self):
        self.assertEqual(average_check([]), 0)
