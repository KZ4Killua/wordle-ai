import unittest
import wordle

class PatternTestCase(unittest.TestCase):

    def test_get_pattern(self):
        self.assertEqual(
            wordle.get_pattern("cocoa", "comma"), "ggaag"
            )
        self.assertEqual(
            wordle.get_pattern("focus", "comma"), "agyaa"
        )
        self.assertEqual(
            wordle.get_pattern("brass", "stair"), "aygya"
        )

    def test_matches_pattern(self):
        self.assertTrue(
            wordle.matches_pattern("stair", "brass", "aygya")
        )
        self.assertTrue(
            wordle.matches_pattern("comma", "cocoa", "ggaag")
        )