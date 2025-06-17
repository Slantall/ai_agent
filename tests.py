# tests.py

import unittest
from functions.get_files_info import get_files_info


class TestCalculator(unittest.TestCase):
    def test_default_dir(self):
        result = get_files_info("calculator", ".")
        print(result)
        print("Expecting no error")

    def test_sub_dir(self):
        result = get_files_info("calculator", "pkg")
        print(result)
        print("Expecting no error")

    def test_nonexistant_dir(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_parent_dir(self):
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')
    def test_nonexistant_dir2(self):
        result = get_files_info("calculator", "s")
        print(result)
        self.assertEqual(result, 'Error: "s" is not a directory')

if __name__ == "__main__":
    unittest.main()