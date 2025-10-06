import json

# ----------------------------
# File Handling Functions
# ----------------------------
def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# ----------------------------
# Main Program
# ----------------------------
def student_grade_manager():
    filename = "students.json"
    students = load_data(filename)

    while True:
        print("\n📘 STUDENT GRADE MANAGER")
        print("1️⃣ Add Student")
        print("2️⃣ Add Grade")
        print("3️⃣ View Students")
        print("4️⃣ Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            sid = input("Enter student ID: ")
            if sid in students:
                print("⚠️ Student ID already exists!")
            else:
                students[sid] = {"name": name, "grades": []}
                print("✅ Student added!")

        elif choice == '2':
            sid = input("Enter student ID: ")
            if sid in students:
                try:
                    grade = float(input("Enter grade: "))
                    students[sid]["grades"].append(grade)
                    print("✅ Grade added!")
                except ValueError:
                    print("⚠️ Please enter a valid number.")
            else:
                print("❌ Student not found!")

        elif choice == '3':
            if not students:
                print("No students yet.")
            else:
                print("\n🎓 Student Records:")
                for sid, info in students.items():
                    grades = info["grades"]
                    avg = sum(grades) / len(grades) if grades else 0
                    print(f"{sid} - {info['name']}: Grades={grades}, Avg={avg:.2f}")

        elif choice == '4':
            save_data(filename, students)
            print("💾 Data saved. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Try again.")


# ----------------------------
# Run Program
# ----------------------------
if __name__ == "__main__":
    student_grade_manager()
