import unittest
from ShaderManager import *

class ShadermanagerTestCase(unittest.TestCase):

    def listAll(self):
        self.assertEqual(len(ShaderManager.listShaders()), 1)


if __name__ == '__main__':
    unittest.main()
