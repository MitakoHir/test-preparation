import unittest
from task_06 import Gradebook


class Tests(unittest.TestCase):
    def test_средняя_оценка(self):
        book = Gradebook()
        book.add("Анна", 4)
        book.add("Анна", 5)
        self.assertEqual(book.average("Анна"), 4.5)

    def test_параметр_times_записывает_оценку_несколько_раз(self):
        book = Gradebook()
        book.add("Анна", 3)
        book.add("Анна", 5, times=3)
        self.assertEqual(book.average("Анна"), 4.5)

    def test_ученик_без_оценок(self):
        with self.assertRaises(ValueError):
            Gradebook().average("Анна")
