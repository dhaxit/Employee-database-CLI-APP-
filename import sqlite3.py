import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")
conn.commit()


def add_employee():
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    cursor.execute(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        (name, department, salary)
    )
    conn.commit()
    print("Employee added successfully.\n")


def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    if not employees:
        print("No employee records found.\n")
    else:
        print("\nID | Name | Department | Salary")
        print("-" * 35)
        for emp in employees:
            print(emp)
        print()


def update_employee():
    emp_id = int(input("Enter employee ID to update salary: "))
    new_salary = float(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employees SET salary = ? WHERE id = ?",
        (new_salary, emp_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("Employee ID not found.\n")
    else:
        print("Employee salary updated.\n")


def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))

    cursor.execute(
        "DELETE FROM employees WHERE id = ?",
        (emp_id,)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("Employee ID not found.\n")
    else:
        print("Employee record deleted.\n")


# Main menu loop
while True:
    print("----- Employee Database Menu -----")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee Salary")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice. Please try again.\n")

# Close database connection
conn.close()
