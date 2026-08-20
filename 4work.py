class Student:
    def __init__(self, surname, name, gender):
        self.surname = surname
        self.name = name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []

        for grades in self.grades.values():
            all_grades.extend(grades)

        if not all_grades:
            return 0

        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе изучения: '
            f'{", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []

        for grades in self.grades.values():
            all_grades.extend(grades)

        if not all_grades:
            return 0

        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_grade()}'
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_student_grade(students, course):
    grades = []

    for student in students:
        if isinstance(student, Student) and course in student.grades:
            grades.extend(student.grades[course])

    if not grades:
        return 0

    return round(sum(grades) / len(grades), 1)


def average_lecturer_grade(lecturers, course):
    grades = []

    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            grades.extend(lecturer.grades[course])

    if not grades:
        return 0

    return round(sum(grades) / len(grades), 1)


student_1 = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Смирнов', 'Иван', 'М')

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Анна', 'Петрова')

reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Мария', 'Соколова')

student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['Введение в программирование']

lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'Java']

reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Java', 10)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Git', 9)
student_2.rate_lecture(lecturer_1, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Java', 10)

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

print('Средняя оценка студентов по Python:',
      average_student_grade(students, 'Python'))

print('Средняя оценка лекторов по Python:',
      average_lecturer_grade(lecturers, 'Python'))

print('Сравнение студентов:', student_1 > student_2)
print('Сравнение лекторов:', lecturer_1 > lecturer_2)

print()
print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(reviewer_2)