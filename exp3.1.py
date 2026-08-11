# Initialize empty lists for names and grades
student_names = []
student_grades = []

def add_student(name, grade):
    """Add a new student and their grade."""
    student_names.append(name)
    student_grades.append(grade)
    print(f"Added {name} with grade {grade}.")

def update_grade(name, new_grade):
    """Update the grade of an existing student."""
    if name in student_names:
        index = student_names.index(name)
        student_grades[index] = new_grade
        print(f"Updated {name}'s grade to {new_grade}.")
    else:
        print(f"Student {name} not found.")

def remove_student(name):
    """Remove a student from the lists."""
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        student_grades.pop(index)
        print(f"Removed {name} from the system.")
    else:
        print(f"Student {name} not found.")

def display_average():
    """Calculate and display the average grade of the class."""
    if not student_grades:
        print("No students in the class.")
        return
    avg = sum(student_grades) / len(student_grades)
    print(f"Class Average Grade: {avg:.2f}")

def display_high_low():
    """Display the highest and lowest grades in the class."""
    if not student_grades:
        print("No students in the class.")
        return
    highest = max(student_grades)
    lowest = min(student_grades)
    
    # Find names corresponding to high/low grades
    high_name = student_names[student_grades.index(highest)]
    low_name = student_names[student_grades.index(lowest)]
    
    print(f"Highest Grade: {highest} (by {high_name})")
    print(f"Lowest Grade: {lowest} (by {low_name})")

def display_all():
    """Display all students and grades."""
    if not student_names:
        print("No students recorded yet.")
        return
    print("\n--- Current Roster ---")
    for name, grade in zip(student_names, student_grades):
        print(f"{name}: {grade}")
    print("----------------------\n")

# Example usage/test run
if __name__ == "__main__":
    add_student("Alice", 85)
    add_student("Bob", 92)
    add_student("Charlie", 78)
    
    display_all()
    
    update_grade("Charlie", 82)
    remove_student("Alice")
    
    display_average()
    display_high_low()
    display_all()
