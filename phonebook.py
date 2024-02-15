import math
import csv
from typing import List, Dict


class Phonebook:
    """
    A simple phonebook application with basic operations.
    """

    FIELDNAMES: List[str] = [
        "Last Name",
        "First Name",
        "Middle Name",
        "Organization",
        "Work Phone",
        "Personal Phone",
    ]

    def __init__(self, file_name: str) -> None:
        """
        Initialize the Phonebook instance.

        Args:
            file_name (str): The name of the file to store phonebook data.
        """
        self.FILE_NAME: str = file_name
        self.records: List[Dict[str, str]] = self.load_phonebook()

    def load_phonebook(self) -> List[Dict[str, str]]:
        """
        Load phonebook data from the file.

        Returns:
            List[Dict[str, str]]: List of dictionaries representing phonebook records.
        """
        try:
            with open(self.FILE_NAME, "r") as file:
                reader: csv.DictReader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def save_phonebook(self) -> None:
        """
        Save phonebook data to the file.
        """
        with open(self.FILE_NAME, "w", newline="") as file:
            writer: csv.DictWriter = csv.DictWriter(
                file, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            writer.writerows(self.records)

    def display_records(self, records: List[Dict[str, str]] = None) -> None:
        """
        Display records from the phonebook paginated with a fixed page size of 5.

        Args:
            records (List[Dict[str, str]], optional): List of records to display.
                Defaults to None, in which case it uses self.records.
        """
        if records is None:
            records = self.records

        page_size: int = 5

        for i, record in enumerate(records, start=1):
            print(f"{i}. {record}")

            # Check if we have displayed 'page_size' records
            if i % page_size == 0:
                if i < len(records):
                    print(f"Page: {i // page_size}")
                    input("Press Enter to go to next page...")

        if len(records) % page_size != 0:
            print(f"Page: {math.ceil(len(records) / page_size)}")
            input("This is the last page. Press Enter to continue...")

    def get_user_input(self, prompt: str) -> str:
        """
        Get user input from the console.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            str: User input string.
        """
        return input(prompt)

    def add_record(self) -> None:
        """
        Add a new record to the phonebook.
        """
        record: Dict[str, str] = {
            field: self.get_user_input(f"Enter {field}: ") for field in self.FIELDNAMES
        }
        self.records.append(record)
        self.save_phonebook()
        print("Record added successfully.")

    def edit_record(self) -> None:
        """
        Edit a record in the phonebook.
        """
        self.display_records(self.records)  # Refresh the display

        record_index: int = int(
            self.get_user_input("Enter the record number to edit: ")
        )
        if 1 <= record_index <= len(self.records):
            record: Dict[str, str] = self.records[record_index - 1]
            for field in record:
                record[field] = self.get_user_input(
                    f"Enter a new value for {field} ({record[field]}): "
                )
            self.save_phonebook()
            print("Record edited successfully.")
        else:
            print("Invalid record number.")

    def search_records(self) -> None:
        """
        Search records in the phonebook based on specified characteristics.
        """
        search_criteria: List[str] = self.get_user_input(
            "Enter search criteria (comma-separated): "
        ).split(",")
        found_records: List[Dict[str, str]] = [
            record
            for record in self.records
            if any(
                criteria.lower() in record[field].lower()
                for field in record
                for criteria in search_criteria
            )
        ]
        if found_records:
            self.display_records(found_records)
        else:
            print("No records found.")
