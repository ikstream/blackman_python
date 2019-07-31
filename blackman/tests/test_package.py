'''
Test module for package functions
'''
import unittest
from package import package

class PackageTest(unittest.TestCase):
    ''' Test class for package functions '''

    print("Test package class")
    def test_is_in_blackarch(self):
        ''' Check is_in_blackarch  function '''
        self.assertTrue(package.is_in_blackarch_repo('rekall'))
        self.assertFalse(package.is_in_blackarch_repo('wireshark'))
        self.assertFalse(package.is_in_blackarch_repo('git'))

if __name__ == '__main__':
    unittest.main()
