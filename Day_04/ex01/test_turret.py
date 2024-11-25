import unittest

from personality import turrets_generator


class TestTurretsGenerator(unittest.TestCase):

    def test_turrets_generator(self):
        generator = turrets_generator()
        turret = next(generator)

        self.assertTrue(hasattr(turret, "personality"))
        personality = turret.personality
        self.assertIsInstance(personality, dict)

        expected_traits = ["neuroticism", "openness", "conscientiousness", "extraversion", "agreeableness"]
        self.assertEqual(set(personality.keys()), set(expected_traits))

        total_trait_value = sum(personality.values())
        self.assertAlmostEqual(total_trait_value, 100, delta=0.5)

        self.assertEqual(turret.shoot(), "Shooting")
        self.assertEqual(turret.search(), "Searching")
        self.assertEqual(turret.talk(), "Talking")


if __name__ == "__main__":
    unittest.main()
