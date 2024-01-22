students_marks = {
    'Yassine': 82,
    'ilyass': 84,
    'Khalid': 70,
    'Bader' : 60,
    'achraf': 50,
    'jennty': 100,
    'Ram' : 30
}
for i in students_marks.keys():
    marks = students_marks[i]
    if marks >= 91 and marks <= 100:
        print(f"{i} is A+")
    elif marks >= 81 and marks <= 90:
        print(f"{i} is A")
    if marks >= 71 and marks <= 80:
        print(f"{i} is B+")
    elif marks >= 61 and marks <= 70:
        print(f"{i} is B")
    elif marks >= 51 and marks <= 60:
        print(f"{i} is C")
    elif marks >= 41 and marks <= 50:
        print(f"{i} is D")
    elif  marks < 41 :
        print(f"{i} is F")