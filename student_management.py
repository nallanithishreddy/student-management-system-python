students = []

def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    students.append({"id": sid, "name": name, "marks": marks})
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Marks: {s['marks']}")

def search_student():
    sid = int(input("Enter Student ID to search: "))
    for s in students:
        if s["id"] == sid:
            print(s)
            return
    print("Student not found.")

def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted.")
            return
    print("Student not found.")

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")