def input_student_info(num_students, subjects):
    students = []
    for i in range(num_students):
        number = input("학번 :")
        name = input("이름: ")
        scores = []
        for subject in subjects:
            score = float(input(f"{subject}: "))
            while score < 0 or score > 100:
                print("잘못된 범위의 점수입니다. 다시 입력하세요.")
                score = float(input(f"{subject}: "))
            scores.append(score)
        students.append({'학번' :number,'이름': name, '성적': scores})
    return students

def calculate_total_average(students, subjects):
    for student in students:
        total_score = sum(student['성적'])
        average_score = total_score / len(subjects)
        student['총점'] = total_score
        student['평균'] = average_score

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def calculate_rank(students):
    students.sort(key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(students):
        student['등수'] = i + 1
        student['학점'] = calculate_grade(student['평균'])

def print_students(students):
    print("\n<성적 관리 프로그램>")
    print("==============================`")
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("==============================`")
    for student in students:
        print(f"{student['학번']}\t{student['이름']}\t{student['성적'][0]}\t{student['성적'][1]}\t{student['성적'][2]}\t{student['총점']}\t{student['평균']}\t{student['학점']}\t{student['등수']}")

num_students = 5
subjects = ['영어', 'C-언어', '파이썬']
students = input_student_info(num_students, subjects)
calculate_total_average(students, subjects)
calculate_rank(students)
print_students(students)