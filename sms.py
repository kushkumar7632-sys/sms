students = []

def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    student = {
        "id": id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student Added Successfully\n")


def view_students():
    if not students:
        print("No records found!\n")
        return

    for s in students:
        print(s)
    print()


def search_student():
    id = int(input("Enter ID to search: "))
    for s in students:
        if s["id"] == id:
            print("Found:", s, "\n")
            return
    print("Student not found!\n")


def delete_student():
    id = int(input("Enter ID to delete: "))
    for s in students:
        if s["id"] == id:
            students.remove(s)
            print("Student deleted!\n")
            return
    print("Student not found!\n")


def update_student():
    id = int(input("Enter ID to update: "))
    for s in students:
        if s["id"] == id:
            s["name"] = input("Enter new name: ")
            s["age"] = int(input("Enter new age: "))
            s["course"] = input("Enter new course: ")
            print("Updated successfully!\n")
            return
    print("Student not found!\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

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
        update_student()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")