from numpy import average


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_tuple = tuple(mark for marks in self.grades.values() for mark in marks)
        self.av_grade = round(average(self.grades_tuple), 1)

 # метод выводит полную информацию по классу Student   
    def __str__(self):
        return f"Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания: {self.av_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

# метод позволяет сравнивать объекты класса Student на равенство по ср. оценке     
    def __eq__(self, value):
        if isinstance(value, Student):
            return self.av_grade == value.av_grade
        else:
            'Ошибка'

# метод позволяет студенту оценить лектора по одному из его курсов
    def rate_lecuturer(self, lecturer, course, grage):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grage]
            else:
                lecturer.grades[course] = [grage]
        else:
            return 'Ошибка. Объект не является экземпляром класса Lecturer либо курс не закреплек за лектором'

# родительский класс с базовыми атрибутами     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.grades_tuple = tuple(mark for marks in self.grades.values() for mark in marks)
        self.av_grade = round(average(self.grades_tuple), 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self.av_grade}"

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия:{self.surname}"

# метод позволяет ревьюверу оценить студента по курсу, который он в данный момент проходит
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка. Объект не является экземпляром класса Student либо курс не закреплен за студентом / не начат'
        

def get_av_student_grades(students, course):
    grades_list = []

    for student in students:
        if isinstance(student, Student):
            if course in student.courses_in_progress:
                grades_list.extend(student.grades[course])
            else:
                return 'Ошибка. Не все переданные студенты проходят курс'
            
    if grades_list:
        rounded_grade = round(average([grades_list]), 1)
        return f"Средняя оценка студентов за курс {course}: {rounded_grade}"
    else:
        return 'Нет оценок для данного курса'


def get_av_lector_grades(lectors, course):
    grades_list = []

    for lector in lectors:
        if isinstance(lector, Lecturer):
            if course in lector.courses_attached:
                grades_list.extend(lector.grades[course])
            else:
                return 'Ошибка. Не все переданные лекторы преподают этот курс'
            
    if grades_list:
        rounded_grade = round(average([grades_list]), 1)
        return f"Средняя оценка лекторов за курс {course}: {rounded_grade}"
    else:
        return 'Нет оценок для данного курса'

 
best_student = Student('Ruoy', 'Eman', 'm')
best_student.courses_in_progress += ['Python', 'PHP', 'Git', 'Java']
best_student.finished_courses += ['Введение в програмирование']

loose_student = Student('Bob', 'Milton', 'm')
loose_student.courses_in_progress += ['Python', 'Git', 'PHP', 'Java']
 
lector_1 = Lecturer('Some', 'Buddy')
lector_1.courses_attached += ['Python', 'PHP', 'Git']

lector_2 = Lecturer('James', 'Dean')
lector_2.courses_attached += ['Java']
 
reviewer_1 = Reviewer('Gregg', 'Arraki')
reviewer_1.courses_attached += ['Python', 'Git', 'PHP']

reviewer_2 = Reviewer('David', 'Lynch')
reviewer_2.courses_attached += ['Java']

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 2)
reviewer_1.rate_hw(best_student, 'Python', 5)
reviewer_1.rate_hw(best_student, 'PHP', 5)
reviewer_1.rate_hw(loose_student, 'PHP', 9)
reviewer_1.rate_hw(best_student, 'Git', 9)
reviewer_1.rate_hw(loose_student, 'Python', 4)
reviewer_1.rate_hw(loose_student, 'Git', 7)
reviewer_2.rate_hw(best_student, 'Java', 6)
reviewer_2.rate_hw(loose_student, 'Java', 7)

best_student.rate_lecuturer(lector_1, 'Python', 8)
best_student.rate_lecuturer(lector_1, 'PHP', 7)
best_student.rate_lecuturer(lector_1, 'Git', 10)
loose_student.rate_lecuturer(lector_1, 'Python', 9)
loose_student.rate_lecuturer(lector_2, 'Java', 10)
best_student.rate_lecuturer(lector_2, 'Java', 9)

# print(best_student.grades)
# print(lector_1.grades)

# # print(reviewer_1, '\n')
# # print(lector_1, '\n')
# # print(best_student)

# print(loose_student.grades)
# print(loose_student == best_student)

students_list = [best_student, loose_student]
target_course = 'Python'

print(get_av_student_grades(students_list, target_course))

target_course = 'PHP'

print(get_av_student_grades(students_list, target_course))

lectors_list = [lector_1, lector_2]
target_course = 'Python'

print(get_av_lector_grades(lectors_list, target_course))