import unittest
from ..lengthOfLastWord import lengthOfLastWord

class TestLengthOfLastWord(unittest.TestCase):
    def TestLength(self):
        self.assertEqual(lengthOfLastWord("Hello World"), 5)
        self.assertEqual(lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(lengthOfLastWord("luffy is still joyboy"), 6)
    