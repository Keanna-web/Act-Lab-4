def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid score, please enter a value between 0 to 100")
        return 

    if score >= 90:
        print("Grade is A")
    elif score >= 80:
        print("Grade is B")
    elif score >= 70:
        print("Grade is C")
    elif score >= 60:
        print("Grade is D")
    else:
        print("Grade is F")

while True:
        score = int(input("enter a score: "))
        assign_grade(score)
    
