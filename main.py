from organizer import organize_folder


def menu():
    while True:
        print("=" * 35)
        print("      File Organizer Pro")
        print("=" * 35)
        print("1. Organize Folder")
        print("2. Settings")
        print("3. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            folder = input("Enter folder path: ")
            organize_folder(folder)

        elif choice == "2":
            print("Settings section")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()