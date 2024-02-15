import unittest
from unittest.mock import patch
from io import StringIO
from phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        # Set up a temporary test file
        self.test_file = "test_phonebook.csv"

    def tearDown(self):
        # Clean up the test file after each test
        try:
            with open(self.test_file, "w") as file:
                file.write("")  # Clear the content
        except FileNotFoundError:
            pass

    def test_add_record(self):
        phonebook = Phonebook(self.test_file)
        user_input = ["John", "Doe", "E.", "TestOrg", "123456", "789012"]

        with patch("builtins.input", side_effect=user_input):
            phonebook.add_record()

        self.assertEqual(len(phonebook.records), 1)
        self.assertEqual(phonebook.records[0]["First Name"], "Doe")
        self.assertEqual(phonebook.records[0]["Last Name"], "John")

    def test_edit_record(self):
        phonebook = Phonebook(self.test_file)
        initial_records = [
            {"First Name": "John", "Last Name": "Doe", "Organization": "TestOrg",
                "Work Phone": "123456", "Personal Phone": "789012"}
        ]
        phonebook.records = initial_records

        user_input = ["", "1", "Jane", "Doe", "NewOrg", "987654", "654321"]

        with patch("builtins.input", side_effect=user_input):
            phonebook.edit_record()

        self.assertEqual(len(phonebook.records), 1)
        self.assertEqual(phonebook.records[0]["First Name"], "Jane")
        self.assertEqual(phonebook.records[0]["Last Name"], "Doe")

    def test_search_records(self):
        phonebook = Phonebook(self.test_file)
        initial_records = [
            {"First Name": "John", "Last Name": "Doe", "Organization": "TestOrg",
                "Work Phone": "123456", "Personal Phone": "789012"},
            {"First Name": "Jane", "Last Name": "Smith", "Organization": "TestOrg2",
                "Work Phone": "987654", "Personal Phone": "654321"}
        ]
        phonebook.records = initial_records

        user_input = "TestOrg2"
        with patch("builtins.input", return_value=user_input):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                phonebook.search_records()

        expected_output = "1. {'First Name': 'Jane', 'Last Name': 'Smith', 'Organization': 'TestOrg2', 'Work Phone': '987654', 'Personal Phone': '654321'}\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
