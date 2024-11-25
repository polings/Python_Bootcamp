import unittest

from splitwise import split_booty


class TestSplitBooty(unittest.TestCase):

    def test_split_even(self):
        purse1 = {'gold_ingots': 6}
        purse2 = {'gold_ingots': 3}
        purse3 = {'gold_ingots': 1}

        p1, p2, p3 = split_booty(purse1, purse2, purse3)

        total = p1.get('gold_ingots', 0) + p2.get('gold_ingots', 0) + p3.get('gold_ingots', 0)
        self.assertEqual(total, 10)

        max_ingots = max(p1.get('gold_ingots', 0), p2.get('gold_ingots', 0), p3.get('gold_ingots', 0))
        min_ingots = min(p1.get('gold_ingots', 0), p2.get('gold_ingots', 0), p3.get('gold_ingots', 0))
        self.assertLessEqual(max_ingots - min_ingots, 1)

    def test_split_uneven(self):
        purse1 = {'gold_ingots': 5}
        purse2 = {'gold_ingots': 3}
        purse3 = {'gold_ingots': 2}

        p1, p2, p3 = split_booty(purse1, purse2, purse3)

        total = p1.get('gold_ingots', 0) + p2.get('gold_ingots', 0) + p3.get('gold_ingots', 0)
        self.assertEqual(total, 10)

        max_ingots = max(p1.get('gold_ingots', 0), p2.get('gold_ingots', 0), p3.get('gold_ingots', 0))
        min_ingots = min(p1.get('gold_ingots', 0), p2.get('gold_ingots', 0), p3.get('gold_ingots', 0))
        self.assertLessEqual(max_ingots - min_ingots, 1)

    def test_no_gold(self):
        purse1 = {'apples': 10}
        purse2 = {'gold_ingots': 0}
        purse3 = {}

        p1, p2, p3 = split_booty(purse1, purse2, purse3)

        self.assertEqual(p1.get('gold_ingots', 0), 0)
        self.assertEqual(p2.get('gold_ingots', 0), 0)
        self.assertEqual(p3.get('gold_ingots', 0), 0)


if __name__ == '__main__':
    unittest.main()
