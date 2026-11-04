import unittest
from task_04 import rank_players


class Tests(unittest.TestCase):
    def test_сортирует_по_очкам_по_убыванию(self):
        self.assertEqual(rank_players([("Анна", 20), ("Борис", 30), ("Вера", 10)]), [("Борис", 30), ("Анна", 20), ("Вера", 10)])
