import unittest

from sample.data_structure import iterateThroughList


class DataStructureTest(unittest.TestCase):
    def test_should_return_map(self):
        list = [5, 8, 56, 5, 87, 65, 56]
        output = iterateThroughList(list)
        expected = {5: 2, 8: 1, 56: 2, 87: 1, 65: 1}
        self.assertEqual(output, expected)
