import datetime


FILE_NAME = "attendance_records.txt"

def add_student(name):
    """Add a new student to the system"""
    with open("students.txt", "a") as file:
        file.write(name + "\n")
    print(f"Student {name} added successfully.")

def mark_attendance():
    """Mark attendance for a student"""
    name = input("Enter student name: ")
    status = input("Enter status (P for Present / A for Absent): ").upper()
    
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FILE_NAME, "a") as file:
        file.write(f"{date_time} - {name} - {status}\n")
    
    print(f"Attendance marked for {name} as {status}")

def view_attendance():
    """View all attendance records"""
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            print("\n--- Attendance Records ---")
            for record in records:
                print(record.strip())
    except FileNotFoundError:
        print("No attendance records found yet.")

def menu():
    while True:
        print("\nAttendance Management System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")


menu()
