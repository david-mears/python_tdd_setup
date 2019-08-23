import unittest
from module import file

class ModuleTests(unittest.TestCase):

    def test_can_create_instances(self):
        _object = file.ObjectClass()
        self.assertTrue(_object)

if __name__ == "__main__":
    unittest.main()