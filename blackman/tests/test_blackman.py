import unittest
import blackman

class PackageTest(unittest.TestCase):
    def test_version(self):
        self.assertEqual(blackman.list_groups(), 0)

if __name__ == '__main__':
    unittest.main()
