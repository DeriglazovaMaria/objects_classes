class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.finished_courses or course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_student(self):
        count = 0
        for grade in self.grades:
            count += len(self.grades[grade])
        avarage = sum(map(sum, self.grades.values())) / count
        return round(avarage, 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_student()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя")
        else:
            return self.average_student() < other.average_student()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя")
        else:
            return self.average_student() > other.average_student()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print("Нельзя")
        else:
            return self.average_student() == other.average_student()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_lector()}\n")

    def average_lector(self):
        count = 0
        for grade in self.grades:
            count += len(self.grades[grade])
        avarage = sum(map(sum, self.grades.values())) / count
        return round(avarage, 1)

    def __lt__(self, other):
        if not isinstance(other, Lector):
            print("Нельзя")
        else:
            return self.average_lector() < other.average_lector()

    def __gt__(self, other):
        if not isinstance(other, Lector):
            print("Нельзя")
        else:
            return self.average_lector() > other.average_lector()

    def __eq__(self, other):
        if not isinstance(other, Lector):
            print("Нельзя")
        else:
            return self.average_lector() == other.average_lector()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ["Git"]

bad_student = Student('Max', 'Mad', 'male')
bad_student.finished_courses += ["C++"]
bad_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['С++']

mad_reviewer = Reviewer('Pol', 'Jonson')
mad_reviewer.courses_attached += ['C++']
mad_reviewer.courses_attached += ['Git']

cool_lector = Lector('Maria', "Deriglazova")
cool_lector.courses_attached += ['Python']

sad_lector = Lector('Dominik', 'Torretto')
sad_lector.courses_attached += ["C++", "Git"]

cool_reviewer.rate_hw(best_student, 'Python', 10)
mad_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'C++', 8)
cool_reviewer.rate_hw(bad_student,'Python', 5)
best_student.rate_lector(sad_lector, 'Git', 8)
bad_student.rate_lector(sad_lector, 'Git', 7)
best_student.rate_lector(sad_lector, 'C++', 10)
best_student.rate_lector(cool_lector, 'Python', 5)

print("_______Студенты_______")
print(str(best_student))
print("_______Другой студент____")
print(str(bad_student))
print("_______Лекторы__________")
print(str(sad_lector))
print("_______Другой лектор____")
print(str(cool_lector))
print("_______Ревьюеры_____")
print(str(cool_reviewer))

print(sad_lector > cool_lector)
print(sad_lector < cool_lector)
print(sad_lector == cool_lector)

print(best_student > bad_student)
print(best_student < bad_student)
print(best_student == bad_student)