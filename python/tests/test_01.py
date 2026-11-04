import unittest
from task_01 import passed_names


class Tests(unittest.TestCase):
    def test_возвращает_имена_прошедших(self):
        students = [{"name": "Анна", "score": 80}, {"name": "Борис", "score": 40}, {"name": "Вера", "score": 90}]
        self.assertEqual(passed_names(students, 50), ["Анна", "Вера"])
