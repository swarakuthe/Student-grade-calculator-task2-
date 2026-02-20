# Student Grade Calculator
# Calculates grade based on marks with validation and feedback

# Code:
def calculate_grade(marks):
    """Returns grade and encouraging message based on marks"""
    if marks >= 90:
        return "A", "Excellent work! You’re a star 🌟"
    elif marks >= 80:
        return "B", "Very good! Keep it up 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better 💪"
    elif marks >= 60:
        return "D", "You passed. Don’t give up 📘"
    else:
        return "F", "Don’t be discouraged. Practice makes perfect 💡"


def get_valid_marks():
    """Keeps asking until user enters valid marks (0–100)"""
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


# Main Program
print("🎯 Student Grade Calculator")

student_name = input("Enter student name: ")

marks = get_valid_marks()
grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", student_name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
