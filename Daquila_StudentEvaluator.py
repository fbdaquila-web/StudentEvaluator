# FRANZ ROBERT B. DAQUILA, 8-ADELFA
# Define function that prints headers
def display_header():
    print("\nSTUDENT PERFORMANCE REPORT\n")

# Define function that inputs student name and assessment scores
def get_student_info():
    # Make assessment scores global variables
    global student_name
    global assessment_score_1
    global assessment_score_2
    global assessment_score_3
    student_name = input("Enter Student Name: ")
    assessment_score_1 = int(input("Enter the first assessment score: "))
    assessment_score_2 = int(input("Enter the second assessment score: "))
    assessment_score_3 = int(input("Enter the third assessment score: "))

    # Make average assessment score a global variable and calculate student's average score
    global average_assessment_score
    average_assessment_score = (assessment_score_1 + assessment_score_2 + assessment_score_3) / 3


# Define function that evaluates average score into performance levels
def evaluate_performance():
    if average_assessment_score >= 90 and 100 >= average_assessment_score:
        print("Performance Level: Outstanding")
    elif average_assessment_score >= 85 and 90 >= average_assessment_score:
        print("Performance Level: Very Satisfactory")
    elif average_assessment_score >= 80 and 85 >= average_assessment_score:
        print("Performance Level: Satisfactory")
    elif average_assessment_score >= 75 and 80 >= average_assessment_score:
        print("Performance Level:Fairly Satisfactory")
    elif average_assessment_score < 75:
        print("Performance Level: Needs Improvement")

# Define function that prints report contents
def display_report():
    print(f"Student name: {student_name}")
    print(f"Assessment scores: {assessment_score_1}, {assessment_score_2}, {assessment_score_3}")
    print(f"Average Score: {average_assessment_score:.2f}")

# Call functions in correct order
display_header()
get_student_info()
display_header()
display_report()
evaluate_performance()