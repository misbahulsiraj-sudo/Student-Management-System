students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        marks = int(input("Enter Marks: "))

        students.append({
            "name": name,
            "marks": marks
        })

        print("✅ Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found!")
        else:
            print("\n--- Student List ---")
            for student in students:
                print(
                    f"Name: {student['name']} | Marks: {student['marks']}"
                )

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid Choice")