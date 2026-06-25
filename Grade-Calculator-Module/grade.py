def calculate_grade(maths,english, science,social,telugu):
  total=maths+english+science+social+ telugu
    average = total / 5

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 35:
        grade = "D"
    else:
        grade = "Fail"

    return total,average,grade
