import unittest
from task_07 import without_zeros, done_share


class Tests(unittest.TestCase):
    def test_убирает_ноль(self):
        self.assertEqual(without_zeros([1, 0, 2]), [1, 2])

    def test_доля_выполненных(self):
        tasks = [{"done": True}, {"done": False}]
        self.assertEqual(done_share(tasks), 0.5)

    def test_пустой_список_задач(self):
        self.assertEqual(done_share([]), 0)
