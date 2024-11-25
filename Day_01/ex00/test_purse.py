import unittest

from purse import add_ingot, get_ingot, empty


class TestPurseFunctions(unittest.TestCase):

    def test_add_ingot(self):
        purse = {}
        updated_purse = add_ingot(purse)
        self.assertEqual(updated_purse['gold_ingots'], 1)
        self.assertEqual(purse, {})

        updated_purse = add_ingot(updated_purse)
        self.assertEqual(updated_purse['gold_ingots'], 2)

    def test_get_ingot(self):
        purse = {'gold_ingots': 2}
        updated_purse = get_ingot(purse)
        self.assertEqual(updated_purse['gold_ingots'], 1)

        updated_purse = get_ingot(updated_purse)
        self.assertEqual(updated_purse['gold_ingots'], 0)

        updated_purse = get_ingot(updated_purse)
        self.assertEqual(updated_purse['gold_ingots'], 0)

    def test_empty(self):
        purse = {'gold_ingots': 5}
        updated_purse = empty(purse)
        self.assertEqual(updated_purse, {})

        updated_purse = empty({})
        self.assertEqual(updated_purse, {})

    def test_multiple_func(self):
        purse = {'gold_ingots': 5}
        updated_purse = add_ingot(get_ingot(add_ingot(empty(purse))))
        self.assertEqual(updated_purse['gold_ingots'], 1)


if __name__ == '__main__':
    unittest.main()
