# Step 1: Write student data to a file
with open("students.txt", "w") as f:
    f.write("101, Ravi, 85\n")
    f.write("102, Priya, 90\n")
    f.write("103, Arjun, 78\n")

print(" Student data written to students.txt")

# Step 2: Read and process student data
total = 0
count = 0

with open("students.txt", "r") as f:
    for line in f:
        roll, name, marks = line.strip().split(",")
        marks = int(marks)
        total += marks
        count += 1
        print(f"Roll: {roll.strip()}, Name: {name.strip()}, Marks: {marks}")

# Step 3: Print average
if count > 0:
    print(f"\nAverage Marks = {total / count:.2f}")