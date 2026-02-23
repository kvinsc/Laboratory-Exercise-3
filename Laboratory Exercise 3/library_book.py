class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"\n You have successfully borrowed \"{self.title}\".")
            print("   Please return it when you're done.")
        else:
            print(f"\n Sorry, \"{self.title}\" is currently unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"\n Thank you for returning \"{self.title}\"!")
            print("   It is now available for others to borrow.")
        else:
            print(f"\n\"{self.title}\" was not marked as borrowed.")

    def is_available(self):
        return self.available

    def display_info(self):
        status = "Available " if self.available else "Unavailable ❌"
        print("\n ---- Book Information ----")
        print(f"   Title       : {self.title}")
        print(f"   Author      : {self.author}")
        print(f"   Year        : {self.year}")
        print(f"   Status      : {status}")
        print("   ----------------------------")


def main():
    print("=" * 40)
    print(" Library Book Management System")
    print("=" * 40)

    
    title = input("\nEnter book title       : ")
    author = input("Enter author name      : ")

    while True:
        try:
            year = int(input("Enter publication year : "))
            if year < 1 or year > 2025:
                raise ValueError("Year must be between 1 and 2025.")
            break
        except ValueError as e:
            print(f" Invalid input: {e}")

  
    book = Book(title, author, year)
    print(f"\n Book \"{book.title}\" has been added to the library.")

 
    while True:
        print("\n=== MENU ===")
        print("1. Display Book Information")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            book.display_info()
        elif choice == "2":
            book.borrow_book()
        elif choice == "3":
            book.return_book()
        elif choice == "4":
            print("\n Thank you for using the Library System. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()