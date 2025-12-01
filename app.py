# این فایل نقطه ورود به اصلی برنامه CLI است
# شامل منو، اضافه کردن دانش آموز، ثبت نمره و نمایش لیست است

import sys
from student import Student
import storage


def show_menu():
    """Print menu options"""
    # چاپ کردن گزینه های منوی اصلی
    print("\n=== Student Score Tracker ===")
    print("1. Add Student")
    print("2. Add Score")
    print("3. List Students")
    print("4. Exit")


def handle_add_student():
    """Add a new student to JSON"""
    # اضافه کردن یک دانش آموز جدید
    name = input("Student Name: ")

    students = storage.load_students()
    new_student = Student(name)
    students.append(new_student.to_dict())

    storage.save_students(students)
    print("Student added!")


def handle_add_score():
    """Add a score to an existing student."""
    # اضافه کردن نمره برای یک دانش آموز
    name = input("Student name: ")

    students = storage.load_students()

    for s in students:
        if s["name"] == name:
            score = float(input("Score: "))
            s["scores"].append(score)
            storage.save_students(students)
            print("Score added!")
            return

    print("Student not found!")


def handle_list_students():
    """Display all students with their averages."""
    # نمایش لیست کامل دانش آموزان + میانگین نمره
    students = storage.load_students()

    if not students:
        print("No students found.")
        return

    print("\n--- Students ---")
    for s in students:
        avg = sum(s["scores"]) / len(s["scores"]) if s["scores"] else 0
        print(f"{s['name']} -- Scores: {s["scores"]} | Average: {avg: .2f}")


def run():
    """Main loop"""
    # حلقه اصلی که برنامه را تا زمان خروج اجرا می کند
    while True:
        show_menu()
        choice = input("Your choice: ")

        if choice == '1':
            handle_add_student()
        elif choice == '2':
            handle_add_score()
        elif choice == '3':
            handle_list_students()
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid Option!")


if __name__ == "__main__":
    run()
