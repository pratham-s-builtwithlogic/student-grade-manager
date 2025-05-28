import csv

def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = int(input("Enter marks (out of 100): "))
    grade = calculate_grade(marks)

    with open('students.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, marks, grade])
    print(f"Student {name} added with grade {grade}")

def view_students():
    print("\n--- Student Records ---")
    try:
        with open('students.csv', mode='r') as file:
            reader = csv.reader(file)
            print("{:<20} {:<10} {:<10} {:<5}".format("Name", "Roll", "Marks", "Grade"))
            print("-" * 50)
            for row in reader:
                print("{:<20} {:<10} {:<10} {:<5}".format(row[0], row[1], row[2], row[3]))
    except FileNotFoundError:
        print("No student records found.")

def menu():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
