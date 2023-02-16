class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 0
        self.student_list = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def count_avg_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        self.avg_grade = sum(grades_list) / len(grades_list)

    def __str__(self):
        self.count_avg_grade()
        student_res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашку: {self.avg_grade}' \
                      f'\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}' \
                      f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return student_res

    def __lt__(self, other):
        self.count_avg_grade()
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self.avg_grade < other.avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = 0

    def count_avg_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list.extend(grade)
        self.avg_grade = sum(grades_list) / len(grades_list)

    def __str__(self):
        self.count_avg_grade()
        lecturer_res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}'
        return lecturer_res

    def __lt__(self, other):
        self.count_avg_grade()
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self.avg_grade < other.avg_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return reviewer_res



first_student = Student('First', 'Student', 'your_gender')
second_student = Student('Second', 'Student', 'your_gender')
student_list = [first_student, second_student]

first_lecturer = Lecturer('First', 'Lecturer')
second_lecturer = Lecturer('Second', 'Lecturer')

first_reviewer = Reviewer('First', 'Reviewer')
second_reviewer = Reviewer('Second', 'Reviewer')


first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Введение в программирование']

second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в программирование']

first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']

second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

first_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 8)
first_student.rate_lecturer(first_lecturer, 'Git', 7)
first_student.rate_lecturer(first_lecturer, 'Git', 9)
first_student.rate_lecturer(first_lecturer, 'Git', 6)

second_student.rate_lecturer(second_lecturer, 'Python', 9)
second_student.rate_lecturer(second_lecturer, 'Python', 9)
second_student.rate_lecturer(second_lecturer, 'Python', 8)
second_student.rate_lecturer(second_lecturer, 'Git', 7)
second_student.rate_lecturer(second_lecturer, 'Git', 8)
second_student.rate_lecturer(second_lecturer, 'Git', 8)

first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Git', 6)
first_reviewer.rate_hw(first_student, 'Git', 9)
first_reviewer.rate_hw(first_student, 'Git', 9)

second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Git', 7)
second_reviewer.rate_hw(second_student, 'Git', 7)
second_reviewer.rate_hw(second_student, 'Git', 8)

print(first_reviewer)
print(second_reviewer)
print('--------')
print(first_lecturer)
print(second_lecturer)
print()
print('Меньше ли средняя оценка первого лектора? - ', first_lecturer.__lt__(second_lecturer))
print('--------')
print(first_student)
print(second_student)
print()
print('Меньше ли средняя оценка первого студента? - ', first_student.__lt__(second_student))


student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]

def avg_grade_course_students(students, course):
    course_grades = []
    for student in students:
        if course in student.grades.keys():
            for grades in student.grades[course]:
                course_grades.append(grades)
    return f'{sum(course_grades) / len(course_grades):.2}'

def avg_grade_course_lecturers(lecturers, course):
    course_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            for grades in lecturer.grades[course]:
                course_grades.append(grades)
    return f'{sum(course_grades) / len(course_grades):.2}'

print(f"Средняя оценка за домашние задания по курсу 'Python': {avg_grade_course_students(student_list, 'Python')}")
print(f"Средняя оценка за домашние задания по курсу 'Git': {avg_grade_course_students(student_list, 'Git')}")


print(f"Средняя оценка за лекции по курсу 'Python': {avg_grade_course_lecturers(lecturer_list, 'Python')}")
print(f"Средняя оценка за лекции по курсу 'Git': {avg_grade_course_lecturers(lecturer_list, 'Git')}")
