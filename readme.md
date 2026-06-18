| Task No. | Task Name | Approved |
|-----------|------------|----------|
| Task 1 | Python Fundamentals – Interactive Library Management System | ✅ Yes |
| Task 2 | To Be Assigned | ❌ No |
| Task 3 | To Be Assigned | ❌ No |
| Task 4 | To Be Assigned | ❌ No |
| Task 5 | To Be Assigned | ❌ No |



# 📚 Interactive Library Management System

## 📌 Project Overview
This project is built for **Task 1: Python Fundamentals** of the Harzio Founding Batch 2026 Internship Program. 

It is a terminal-based command-line interface (CLI) application that allows users to manage a virtual library. The program runs continuously, allowing users to view the catalog, add new books, and update the borrowing status of items in real time.

---

## ⚙️ Features & Menu Options
When the program runs, the user is presented with an interactive menu with 5 options:
1. **View Available Books:** Scans the library and displays only the books that are currently available, along with the total count.
2. **Add a New Book:** Prompts the user to enter a new book title and price, automatically generates a new ID, and adds it to the system.
3. **Borrow a Book:** Checks if a requested book is available and updates its status to `Borrowed`. Prevents double-borrowing.
4. **Return a Book:** Checks if a book is currently marked as `Borrowed` and updates it back to `Available`.
5. **Exit Project:** Safely terminates the continuous loop and closes the application.

---

## 🧠 Python Concepts Demonstrated
To fulfill the Harzio Phase 1 requirements, this project strictly utilizes foundational Python features without relying on external databases or complex object-oriented programming (OOP).

* **Data Structures:** The library database is built using a global **List** containing nested **Dictionaries**. Each dictionary holds specific key-value pairs (ID, Title, Price, Status).
* **Functions:** Every menu option is encapsulated in its own modular `def` function to keep the code clean and readable.
* **Control Flow & Logic:** Extensive use of `if/elif/else` statements for decision-making (e.g., checking if a book is actually available before allowing someone to borrow it).
* **Loops:** * A `while True` loop is used to keep the main menu running infinitely until the user explicitly chooses to exit.
  * `for` loops are used to iterate through the data structures to find specific book IDs.
* **Error Handling:** `try/except` blocks are used to prevent the program from crashing if a user types a letter when they were supposed to type a number.

---

## 🚀 Setup & Execution Guide

### Prerequisites
* You must have **Python 3.x** installed on your system.
* No external libraries or installations (like `pip install`) are required.

### How to Run
1. Open your native terminal or command prompt.
2. Navigate to the folder containing this project:
   ```bash
   cd simple-library-system
