"""
Student Management System
A comprehensive system for managing student records, grades, attendance, and courses.
"""

import json
import os
import datetime
from typing import List, Dict, Optional
import random
import string


class Student:
    """Represents a student with personal information and academic records."""

    def __init__(
        self, student_id: str, name: str, email: str, age: int, phone: str, address: str
    ):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone
        self.address = address
        self.enrolled_courses = []
        self.grades = {}
        self.attendance = {}
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict:
        """Convert student object to dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "phone": self.phone,
            "address": self.address,
            "enrolled_courses": self.enrolled_courses,
            "grades": self.grades,
            "attendance": self.attendance,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Student":
        """Create student object from dictionary."""
        student = cls(
            data["student_id"],
            data["name"],
            data["email"],
            data["age"],
            data["phone"],
            data["address"],
        )
        student.enrolled_courses = data.get("enrolled_courses", [])
        student.grades = data.get("grades", {})
        student.attendance = data.get("attendance", {})
        student.created_at = data.get("created_at", student.created_at)
        return student

    def enroll_course(self, course_id: str) -> bool:
        """Enroll student in a course."""
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)
            self.grades[course_id] = []
            self.attendance[course_id] = {"present": 0, "absent": 0}
            return True
        return False

    def add_grade(self, course_id: str, grade: float, assignment: str) -> bool:
        """Add a grade for a specific course."""
        if course_id in self.enrolled_courses:
            self.grades[course_id].append(
                {
                    "grade": grade,
                    "assignment": assignment,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d"),
                }
            )
            return True
        return False

    def mark_attendance(self, course_id: str, status: str) -> bool:
        """Mark attendance for a course."""
        if course_id in self.enrolled_courses and status in ["present", "absent"]:
            self.attendance[course_id][status] += 1
            return True
        return False

    def get_average_grade(self, course_id: str) -> Optional[float]:
        """Calculate average grade for a course."""
        if course_id in self.grades and self.grades[course_id]:
            grades = [g["grade"] for g in self.grades[course_id]]
            return sum(grades) / len(grades)
        return None

    def get_attendance_percentage(self, course_id: str) -> Optional[float]:
        """Calculate attendance percentage for a course."""
        if course_id in self.attendance:
            present = self.attendance[course_id]["present"]
            absent = self.attendance[course_id]["absent"]
            total = present + absent
            if total > 0:
                return (present / total) * 100
        return None


class Course:
    """Represents a course with details and enrolled students."""

    def __init__(
        self, course_id: str, name: str, instructor: str, credits: int, description: str
    ):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.credits = credits
        self.description = description
        self.enrolled_students = []
        self.schedule = {}

    def to_dict(self) -> Dict:
        """Convert course object to dictionary."""
        return {
            "course_id": self.course_id,
            "name": self.name,
            "instructor": self.instructor,
            "credits": self.credits,
            "description": self.description,
            "enrolled_students": self.enrolled_students,
            "schedule": self.schedule,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Course":
        """Create course object from dictionary."""
        course = cls(
            data["course_id"],
            data["name"],
            data["instructor"],
            data["credits"],
            data["description"],
        )
        course.enrolled_students = data.get("enrolled_students", [])
        course.schedule = data.get("schedule", {})
        return course

    def add_student(self, student_id: str) -> bool:
        """Add a student to the course."""
        if student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)
            return True
        return False

    def remove_student(self, student_id: str) -> bool:
        """Remove a student from the course."""
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            return True
        return False

    def set_schedule(self, day: str, time: str) -> None:
        """Set course schedule."""
        self.schedule[day] = time


class StudentManagementSystem:
    """Main system for managing students and courses."""

    def __init__(self, data_file: str = "student_data.json"):
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}
        self.load_data()

    def generate_id(self, prefix: str = "STU") -> str:
        """Generate a unique ID."""
        random_str = "".join(random.choices(string.digits, k=6))
        return f"{prefix}{random_str}"

    def add_student(
        self, name: str, email: str, age: int, phone: str, address: str
    ) -> str:
        """Add a new student to the system."""
        student_id = self.generate_id("STU")
        while student_id in self.students:
            student_id = self.generate_id("STU")

        student = Student(student_id, name, email, age, phone, address)
        self.students[student_id] = student
        self.save_data()
        return student_id

    def add_course(
        self, name: str, instructor: str, credits: int, description: str
    ) -> str:
        """Add a new course to the system."""
        course_id = self.generate_id("CRS")
        while course_id in self.courses:
            course_id = self.generate_id("CRS")

        course = Course(course_id, name, instructor, credits, description)
        self.courses[course_id] = course
        self.save_data()
        return course_id

    def enroll_student_in_course(self, student_id: str, course_id: str) -> bool:
        """Enroll a student in a course."""
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]

            if student.enroll_course(course_id) and course.add_student(student_id):
                self.save_data()
                return True
        return False

    def add_grade(
        self, student_id: str, course_id: str, grade: float, assignment: str
    ) -> bool:
        """Add a grade for a student in a course."""
        if student_id in self.students:
            if self.students[student_id].add_grade(course_id, grade, assignment):
                self.save_data()
                return True
        return False

    def mark_attendance(self, student_id: str, course_id: str, status: str) -> bool:
        """Mark attendance for a student in a course."""
        if student_id in self.students:
            if self.students[student_id].mark_attendance(course_id, status):
                self.save_data()
                return True
        return False

    def get_student(self, student_id: str) -> Optional[Student]:
        """Get a student by ID."""
        return self.students.get(student_id)

    def get_course(self, course_id: str) -> Optional[Course]:
        """Get a course by ID."""
        return self.courses.get(course_id)

    def search_students(self, query: str) -> List[Student]:
        """Search students by name or ID."""
        results = []
        query = query.lower()
        for student in self.students.values():
            if (
                query in student.name.lower()
                or query in student.student_id.lower()
                or query in student.email.lower()
            ):
                results.append(student)
        return results

    def search_courses(self, query: str) -> List[Course]:
        """Search courses by name or instructor."""
        results = []
        query = query.lower()
        for course in self.courses.values():
            if (
                query in course.name.lower()
                or query in course.instructor.lower()
                or query in course.course_id.lower()
            ):
                results.append(course)
        return results

    def get_student_report(self, student_id: str) -> Optional[Dict]:
        """Generate a comprehensive report for a student."""
        student = self.get_student(student_id)
        if not student:
            return None

        report = {
            "student_info": {
                "id": student.student_id,
                "name": student.name,
                "email": student.email,
                "age": student.age,
                "phone": student.phone,
            },
            "courses": [],
        }

        for course_id in student.enrolled_courses:
            course = self.get_course(course_id)
            if course:
                avg_grade = student.get_average_grade(course_id)
                attendance_pct = student.get_attendance_percentage(course_id)

                report["courses"].append(
                    {
                        "course_id": course_id,
                        "course_name": course.name,
                        "instructor": course.instructor,
                        "average_grade": round(avg_grade, 2) if avg_grade else "N/A",
                        "attendance": f"{round(attendance_pct, 2)}%"
                        if attendance_pct
                        else "N/A",
                        "grades": student.grades.get(course_id, []),
                    }
                )

        return report

    def get_course_statistics(self, course_id: str) -> Optional[Dict]:
        """Get statistics for a course."""
        course = self.get_course(course_id)
        if not course:
            return None

        total_students = len(course.enrolled_students)
        all_grades = []
        all_attendance = []

        for student_id in course.enrolled_students:
            student = self.get_student(student_id)
            if student:
                avg_grade = student.get_average_grade(course_id)
                if avg_grade:
                    all_grades.append(avg_grade)

                attendance = student.get_attendance_percentage(course_id)
                if attendance:
                    all_attendance.append(attendance)

        stats = {
            "course_id": course_id,
            "course_name": course.name,
            "instructor": course.instructor,
            "total_students": total_students,
            "average_grade": round(sum(all_grades) / len(all_grades), 2)
            if all_grades
            else "N/A",
            "average_attendance": round(sum(all_attendance) / len(all_attendance), 2)
            if all_attendance
            else "N/A",
        }

        return stats

    def delete_student(self, student_id: str) -> bool:
        """Delete a student from the system."""
        if student_id in self.students:
            student = self.students[student_id]

            # Remove from enrolled courses
            for course_id in student.enrolled_courses:
                course = self.get_course(course_id)
                if course:
                    course.remove_student(student_id)

            del self.students[student_id]
            self.save_data()
            return True
        return False

    def delete_course(self, course_id: str) -> bool:
        """Delete a course from the system."""
        if course_id in self.courses:
            course = self.courses[course_id]

            # Remove from enrolled students
            for student_id in course.enrolled_students:
                student = self.get_student(student_id)
                if student and course_id in student.enrolled_courses:
                    student.enrolled_courses.remove(course_id)
                    if course_id in student.grades:
                        del student.grades[course_id]
                    if course_id in student.attendance:
                        del student.attendance[course_id]

            del self.courses[course_id]
            self.save_data()
            return True
        return False

    def save_data(self) -> None:
        """Save all data to JSON file."""
        data = {
            "students": {sid: s.to_dict() for sid, s in self.students.items()},
            "courses": {cid: c.to_dict() for cid, c in self.courses.items()},
        }

        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self) -> None:
        """Load data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)

                self.students = {
                    sid: Student.from_dict(s)
                    for sid, s in data.get("students", {}).items()
                }
                self.courses = {
                    cid: Course.from_dict(c)
                    for cid, c in data.get("courses", {}).items()
                }
            except Exception as e:
                print(f"Error loading data: {e}")
                self.students = {}
                self.courses = {}


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("STUDENT MANAGEMENT SYSTEM".center(50))
    print("=" * 50)
    print("1.  Add Student")
    print("2.  Add Course")
    print("3.  Enroll Student in Course")
    print("4.  Add Grade")
    print("5.  Mark Attendance")
    print("6.  Search Students")
    print("7.  Search Courses")
    print("8.  View Student Report")
    print("9.  View Course Statistics")
    print("10. List All Students")
    print("11. List All Courses")
    print("12. Delete Student")
    print("13. Delete Course")
    print("0.  Exit")
    print("=" * 50)


def main():
    """Main function to run the student management system."""
    sms = StudentManagementSystem()

    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\n--- Add New Student ---")
            name = input("Name: ")
            email = input("Email: ")
            age = int(input("Age: "))
            phone = input("Phone: ")
            address = input("Address: ")

            student_id = sms.add_student(name, email, age, phone, address)
            print(f"✓ Student added successfully! ID: {student_id}")

        elif choice == "2":
            print("\n--- Add New Course ---")
            name = input("Course Name: ")
            instructor = input("Instructor: ")
            credits = int(input("Credits: "))
            description = input("Description: ")

            course_id = sms.add_course(name, instructor, credits, description)
            print(f"✓ Course added successfully! ID: {course_id}")

        elif choice == "3":
            print("\n--- Enroll Student in Course ---")
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")

            if sms.enroll_student_in_course(student_id, course_id):
                print("✓ Student enrolled successfully!")
            else:
                print("✗ Enrollment failed. Check IDs.")

        elif choice == "4":
            print("\n--- Add Grade ---")
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            grade = float(input("Grade (0-100): "))
            assignment = input("Assignment Name: ")

            if sms.add_grade(student_id, course_id, grade, assignment):
                print("✓ Grade added successfully!")
            else:
                print("✗ Failed to add grade.")

        elif choice == "5":
            print("\n--- Mark Attendance ---")
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            status = input("Status (present/absent): ").lower()

            if sms.mark_attendance(student_id, course_id, status):
                print("✓ Attendance marked successfully!")
            else:
                print("✗ Failed to mark attendance.")

        elif choice == "6":
            print("\n--- Search Students ---")
            query = input("Search query: ")
            results = sms.search_students(query)

            if results:
                print(f"\nFound {len(results)} student(s):")
                for student in results:
                    print(
                        f"  ID: {student.student_id} | Name: {student.name} | Email: {student.email}"
                    )
            else:
                print("No students found.")

        elif choice == "7":
            print("\n--- Search Courses ---")
            query = input("Search query: ")
            results = sms.search_courses(query)

            if results:
                print(f"\nFound {len(results)} course(s):")
                for course in results:
                    print(
                        f"  ID: {course.course_id} | Name: {course.name} | Instructor: {course.instructor}"
                    )
            else:
                print("No courses found.")

        elif choice == "8":
            print("\n--- Student Report ---")
            student_id = input("Student ID: ")
            report = sms.get_student_report(student_id)

            if report:
                print(f"\n{'=' * 50}")
                print(f"Student: {report['student_info']['name']}")
                print(f"ID: {report['student_info']['id']}")
                print(f"Email: {report['student_info']['email']}")
                print(f"{'=' * 50}")

                if report["courses"]:
                    for course_info in report["courses"]:
                        print(f"\nCourse: {course_info['course_name']}")
                        print(f"  Instructor: {course_info['instructor']}")
                        print(f"  Average Grade: {course_info['average_grade']}")
                        print(f"  Attendance: {course_info['attendance']}")
                else:
                    print("\nNo courses enrolled.")
            else:
                print("Student not found.")

        elif choice == "9":
            print("\n--- Course Statistics ---")
            course_id = input("Course ID: ")
            stats = sms.get_course_statistics(course_id)

            if stats:
                print(f"\n{'=' * 50}")
                print(f"Course: {stats['course_name']}")
                print(f"Instructor: {stats['instructor']}")
                print(f"Total Students: {stats['total_students']}")
                print(f"Average Grade: {stats['average_grade']}")
                print(f"Average Attendance: {stats['average_attendance']}%")
                print(f"{'=' * 50}")
            else:
                print("Course not found.")

        elif choice == "10":
            print("\n--- All Students ---")
            if sms.students:
                for student in sms.students.values():
                    print(
                        f"ID: {student.student_id} | Name: {student.name} | Courses: {len(student.enrolled_courses)}"
                    )
            else:
                print("No students in system.")

        elif choice == "11":
            print("\n--- All Courses ---")
            if sms.courses:
                for course in sms.courses.values():
                    print(
                        f"ID: {course.course_id} | Name: {course.name} | Students: {len(course.enrolled_students)}"
                    )
            else:
                print("No courses in system.")

        elif choice == "12":
            print("\n--- Delete Student ---")
            student_id = input("Student ID: ")
            confirm = input(
                f"Are you sure you want to delete student {student_id}? (yes/no): "
            )

            if confirm.lower() == "yes":
                if sms.delete_student(student_id):
                    print("✓ Student deleted successfully!")
                else:
                    print("✗ Student not found.")

        elif choice == "13":
            print("\n--- Delete Course ---")
            course_id = input("Course ID: ")
            confirm = input(
                f"Are you sure you want to delete course {course_id}? (yes/no): "
            )

            if confirm.lower() == "yes":
                if sms.delete_course(course_id):
                    print("✓ Course deleted successfully!")
                else:
                    print("✗ Course not found.")

        elif choice == "0":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\n✗ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
