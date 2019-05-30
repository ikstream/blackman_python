import unittest
import blackman

class PackageTest(unittest.TestCase):
    print("Test blackman\n")
    print(blackman.HOME)
    def test_groups(self):
        self.assertEqual(blackman.list_groups(), 0)
    def test_dirs(self):
        print(f"Testing if {blackman.BLACKARCH_CONFIG} exists")
        self.assertEqual(blackman.check_config_dir(), 0)


if __name__ == '__main__':
    unittest.main()
