import unittest
from task_03 import hours_by_employee


class Tests(unittest.TestCase):
    def test_суммирует_подтверждённые_часы(self):
        records = [
            {"employee": "Анна", "hours": 2, "approved": True},
            {"employee": "Анна", "hours": 3, "approved": True},
            {"employee": "Анна", "hours": 100, "approved": False},
            {"employee": "Борис", "hours": 4.5, "approved": True},
        ]
        self.assertEqual(hours_by_employee(records), {"Анна": 5, "Борис": 4.5})
