import unittest
from package import package

class PackageTest(unittest.TestCase):
    print("Test package class\n")
    def test_is_in_blackarch(self):
        self.assertTrue(package.is_in_blackarch_repo('rekall'))
        self.assertFalse(package.is_in_blackarch_repo('wireshark'))
        self.assertFalse(package.is_in_blackarch_repo('git'))

if __name__ == '__main__':
    unittest.main()
