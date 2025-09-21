class Student:
    def __init__(self, name, marks):  # double underscores before & after init
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.average():.2f}")

    def average(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Alice", [85, 90, 78])
s1.display()

print("\n--- Another Student ---")
s2 = Student("Bob", [70, 65, 80, 75])
s2.display()