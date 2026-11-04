import unittest
from task_05 import Wallet


class Tests(unittest.TestCase):
    def test_новый_кошелёк_пуст(self):
        self.assertEqual(Wallet().balance(), 0)

    def test_пополнение_и_снятие(self):
        wallet = Wallet()
        wallet.deposit(100)
        wallet.withdraw(30)
        self.assertEqual(wallet.balance(), 70)

    def test_нельзя_снять_больше_чем_есть(self):
        wallet = Wallet()
        wallet.deposit(100)
        with self.assertRaises(ValueError):
            wallet.withdraw(200)
