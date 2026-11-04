import unittest
from task_09 import Cart


class Tests(unittest.TestCase):
    def test_сумма_корзины(self):
        cart = Cart()
        cart.add("a", 100, 2)
        cart.add("b", 50)
        self.assertEqual(cart.total(), 250)

    def test_позиции_отсортированы(self):
        cart = Cart()
        cart.add("b", 50)
        cart.add("a", 100, 2)
        self.assertEqual(cart.positions(), [("a", 2), ("b", 1)])

    def test_удаление_части_товара(self):
        cart = Cart()
        cart.add("a", 100, 3)
        cart.remove("a", 2)
        self.assertEqual(cart.positions(), [("a", 1)])

    def test_нельзя_удалить_товар_которого_нет(self):
        with self.assertRaises(ValueError):
            Cart().remove("a")
