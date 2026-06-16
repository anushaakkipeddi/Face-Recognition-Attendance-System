import csv
from datetime import datetime

students = ["Alice", "Bob", "Charlie"]

today = datetime.now().strftime("%Y-%m-%d")
filename = f"attendance_{today}.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Student Name", "Attendance"])

    print("Mark Attendance (P = Present, A = Absent)\n")

    for student in students:
        status = input(f"{student}: ").upper()

        while status not in ["P", "A"]:
            status = input("Enter P or A: ").upper()

        writer.writerow([student, "Present" if status == "P" else "Absent"])

print(f"\nAttendance saved in {filename}")