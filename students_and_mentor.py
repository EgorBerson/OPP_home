def separete_average (student_dict, courses):
    n = 0
    l = 0
    for student in student_dict:
        n += sum(student.grades[courses])
        l += len(student.grades[courses])
    return n / l

def average (grades_dict):
    n = 0
    l = 0
    for item in grades_dict.values():
        n += sum(item)
        l += len(item)
    return n / l

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.teaches_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average (self.grades)}'

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance (other, Student):
            if average (self.grades) > average (other.grades):
                return False
            else:
                return True
        else:
            'Ошибка! Cравнение двух студентов'

class Mentor:
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

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.teaches_courses = []
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average (self.grades)}'

    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance (other, Lecturer):
            if average (self.grades) > average (other.grades):
                return False
            else:
                return True
        else:
            'Ошибка! Cравнение двух лекторов'


class Reviewer (Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'SQL']
college_student = Student('Bary', 'Allen', 'Male')
college_student.courses_in_progress += ['SQL', 'Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'SQL']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

good_reviewer = Reviewer ('Дмитрий', 'Степанович', 'SQL')
good_reviewer.courses_attached += ['SQL', 'Python']
college_reviewer = Reviewer ('Александр', 'Бородин', 'Male')

good_reviewer.rate_hw(best_student, 'SQL', 8)
good_reviewer.rate_hw(college_student, 'SQL', 7)
good_reviewer.rate_hw(college_student, 'Python', 7)
good_reviewer.rate_hw(college_student, 'Python', 9)
 
print (best_student.grades)
print (best_student)

bad_lecturer = Lecturer('Василий', 'Гупкин')
bad_lecturer.teaches_courses += ['Python', 'SQL']
better_lecturer = Lecturer('Иван', 'Спичкин')
better_lecturer.teaches_courses += ['SQL', 'JS']

best_student.rate_hw(bad_lecturer, 'Python', 4)
best_student.rate_hw(bad_lecturer, 'SQL', 3)
best_student.rate_hw(better_lecturer, 'SQL', 6)

print (bad_lecturer)
print (better_lecturer)
print (average (college_student.grades))

print (college_student > best_student)
print (bad_lecturer > better_lecturer)

print (separete_average ([best_student, college_student], 'Python'))