import unittest
from bowling.frame import Frame

class TestFrame(unittest.TestCase):

    def setUp(self):
        self.frame = Frame(1)

    def tearDown(self):
        del self.frame

    def testHasId(self):
        self.assertEqual(self.frame.number, 1)

    def testHasRolls(self):
        self.assertEqual(self.frame.rolls, [])

    def testHasAfter(self):
        self.assertIsNone(self.frame.child)

    def testSimpleScore(self):
        self.frame.rolls = [4, 5]
        self.assertEqual(self.frame.simple_score(), 9)
