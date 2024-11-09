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

# метод позволяет ревьюверу оценить студента по курсу, который он в данный момент проходит
class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия:{self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка. Объект не является экземпляром класса Student либо курс не закреплен за студентом / не начат'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'PHP', 'Git']
best_student.finished_courses += ['Введение в програмирование']

loose_student = Student('Bob', 'Milton', 'm')
loose_student.courses_in_progress += ['Python', 'Git']
 
lector = Lecturer('Some', 'Buddy')
lector.courses_attached += ['Python', 'PHP', 'Git']
 
reviewer = Reviewer('Gregg', 'Arraki')
reviewer.courses_attached += ['Python', 'Git']

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 9)
reviewer.rate_hw(best_student, 'Python', 8)
reviewer.rate_hw(best_student, 'PHP', 5)
reviewer.rate_hw(best_student, 'Git', 9)
reviewer.rate_hw(loose_student, 'Python', 9)
reviewer.rate_hw(loose_student, 'Git', 7)

best_student.rate_lecuturer(lector, 'Python', 8)
best_student.rate_lecuturer(lector, 'PHP', 7)
best_student.rate_lecuturer(lector, 'Git', 10)

print(best_student.grades)
print(lector.grades)

# print(reviewer, '\n')
# print(lector, '\n')
# print(best_student)

print(loose_student.grades)
print(loose_student == best_student)