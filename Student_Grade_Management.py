def calculate_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def get_student_data():
    students = []
    
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        print(f"\nEntering data for Student {i + 1}")
        
        # Get student name
        name = input("Enter the student's name: ")
        
        # Get scores for subjects
        num_subjects = int(input(f"Enter the number of subjects for {name}: "))
        scores = []
        
        for j in range(num_subjects):
            score = float(input(f"Enter score for subject {j + 1}: "))
            scores.append(score)
        
        # Calculate average
        average = sum(scores) / len(scores) 
        
        # Get letter grade
        letter_grade = calculate_letter_grade(average)
        
        # Save student data
        students.append({
            "name": name,
            "scores": scores,
            "average": average,
            "grade": letter_grade
        })
    
    return students

def display_student_data(students):
    print("\nStudent Grade Report:")
    print("=" * 40)
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Scores: {student['scores']}")
        print(f"Average Score: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print("-" * 40)

def main():
    students = get_student_data()
    display_student_data(students)

if __name__ == "__main__":
    main()
