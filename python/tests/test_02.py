import unittest
from task_02 import count_by_city


class Tests(unittest.TestCase):
    def test_считает_людей_по_городам(self):
        people = [{"name": "Анна", "city": "Тула"}, {"name": "Борис", "city": "Омск"}, {"name": "Вера", "city": "Тула"}]
        self.assertEqual(count_by_city(people), {"Тула": 2, "Омск": 1})
