import unittest

from key import Key


class TestKey(unittest.TestCase):

    def setUp(self):
        self.key = Key()

    def test_len(self):
        self.assertEqual(len(self.key), 1337, "AssertionError: len(key) == 1337")

    def test_getitem(self):
        self.assertEqual(self.key[404], 3, "AssertionError: key[404] == 3")

    def test_gt(self):
        self.assertTrue(self.key > 9000, "AssertionError: key > 9000")

    def test_passphrase(self):
        self.assertEqual(self.key.passphrase, "zax2rulez", "AssertionError: key.passphrase == 'zax2rulez'")

    def test_str(self):
        self.assertEqual(str(self.key), "GeneralTsoKeycard", "AssertionError: str(key) == 'GeneralTsoKeycard'")


if __name__ == '__main__':
    unittest.main()
