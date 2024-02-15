from phonebook import Phonebook


def main() -> None:
    """
    Main function to run the Phonebook application.
    """
    FILE_NAME: str = "phonebook.csv"
    phonebook: Phonebook = Phonebook(FILE_NAME)

    while True:
        print(
            "\n1. Display records\n2. Add record\n3. Edit record\n4. Search records\n0. Exit"
        )
        choice: str = input("Choose an action (0-4): ")

        if choice == "1":
            phonebook.display_records()
        elif choice == "2":
            phonebook.add_record()
        elif choice == "3":
            phonebook.edit_record()
        elif choice == "4":
            phonebook.search_records()
        elif choice == "0":
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
