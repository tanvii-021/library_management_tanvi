library_books = [
    {"id": 1, "title": "Python Basics", "price": 499, "status": "Available"},
    {"id": 2, "title": "Data Structures", "price": 799, "status": "Available"},
    {"id": 3, "title": "Web Development", "price": 599, "status": "Borrowed"}
]

def view_available_books():
    print("\n--- AVAILABLE BOOKS ---")
    available_count = 0
    
    for book in library_books:
        if book["status"] == "Available":
            print(f"ID: {book['id']} | Title: {book['title']} | Price: ₹{book['price']}")
            available_count += 1
            
    print("-----------------------")
    print(f"Total Available Books: {available_count}\n")


def add_new_book():
    print("\n--- ADD A NEW BOOK ---")
    title = input("Enter book title: ")
    
    try:
        price = int(input("Enter book price (₹): "))
    except ValueError:
        print("Invalid price! Setting price to ₹0 by default.")
        price = 0

    if len(library_books) == 0:
        new_id = 1
    else:
        new_id = library_books[-1]["id"] + 1

    new_book = {
        "id": new_id,
        "title": title,
        "price": price,
        "status": "Available"
    }
    
    library_books.append(new_book)
    print(f"Success! '{title}' has been added to the library with ID: {new_id}.\n")


def borrow_book():
    print("\n--- BORROW A BOOK ---")
    try:
        book_id = int(input("Enter the ID of the book you want to borrow: "))
    except ValueError:
        print("Invalid ID format.")
        return

    for book in library_books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Borrowed"
                print(f"Success! You have borrowed '{book['title']}'.\n")
            else:
                print(f"Sorry, '{book['title']}' is already borrowed by someone else.\n")
            return 
            
    print("Error: Book ID not found.\n")


def return_book():
    print("\n--- RETURN A BOOK ---")
    try:
        book_id = int(input("Enter the ID of the book you are returning: "))
    except ValueError:
        print("Invalid ID format.")
        return

    for book in library_books:
        if book["id"] == book_id:
            if book["status"] == "Borrowed":
                book["status"] = "Available"
                print(f"Success! '{book['title']}' has been returned to the shelf.\n")
            else:
                print(f"This book wasn't borrowed. It's already sitting in the library!\n")
            return
            
    print("Error: Book ID not found.\n")


def main():
    while True:
        print("=== MAIN MENU ===")
        print("1. View Available Books")
        print("2. Add a New Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit Project")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            view_available_books()
        elif choice == "2":
            add_new_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("\nTerminating project. Thank you for using the Library System!")
            break 
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()