import unittest
from module import file

class ModuleTests(unittest.TestCase):

    def setUp(self):
        self._object = file.ObjectClass()

    def test_can_create_instances(self):
        self.assertTrue(self._object)

if __name__ == "__main__":
    unittest.main()