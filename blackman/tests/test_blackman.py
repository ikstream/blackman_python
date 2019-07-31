'''
Test module for blackman
'''

import unittest
import blackman

class PackageTest(unittest.TestCase):
    '''
    Test class for basic blackman tests
    '''
    print("Test blackman")
    def test_groups(self):
        ''' Test list_groups function'''
        self.assertEqual(blackman.list_groups(), 0)


    def test_dirs(self):
        ''' Test for config and git direcotries '''
        print(f"Testing if {blackman.BLACKARCH_CONFIG} exists")
        self.assertEqual(blackman.check_config_dir(), 0)


if __name__ == '__main__':
    unittest.main()
