from statistics import mean
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.finished_courses or course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades and 1 <= grade <= 10:
                lecture.grades[grade] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        for i in self.grades.items():
            av_grade = round(mean(i[1]), 1)
            return av_grade
    #
    # def average_grade(self):
    #     average = sum(self.grades.values())/len(self.grades)
    #     return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_grade()}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Этот человек на является студентом!')
            return
        if self.average_grade() > other.average_grade():
            return f'{self.name} {self.surname} получил(а) средний балл выше'
        else:
            return f'{other.name} {other.surname} получил(а) средний балл выше'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        for i in self.grades.items():
            av_grade = round(mean(i[1]), 1)
            return av_grade

    # def average_grade(self):
    #     average = float(sum(self.grades.values()))/len(self.grades)
    #     return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade() if len(self.grades) > 0 else "Оценок пока нет"}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Этот человек на является лектором!')
            return
        if self.average_grade() > other.average_grade():
            return f'{self.name} {self.surname} получил(а) средний балл выше'
        else:
            return f'{other.name} {other.surname} получил(а) средний балл выше'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

# best_student = Student('Ruoy', 'Eman', 'man')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades
s1 = Student('Irina', 'Ivanova', 'W')
s1.finished_courses = 'C#', 'C++'
s1.courses_in_progress = 'Python'
s2 = Student('Egor', 'Egorov', 'M')
s2.finished_courses = 'HTML'
s2.courses_in_progress = 'Java'

r1 = Reviewer('Aleksandr', 'First')
r1.courses_attached = 'Python', 'C++', 'C#'
r2 = Reviewer('Karl', 'Lagerfild')
r2.courses_attached = 'HTML', 'Java', 'Python'

l1 = Lecturer('Maksim', 'Lushin')
l1.courses_attached = 'C#', 'Python'
l2 = Lecturer('Sergey', 'Zorin')
l2.courses_attached = 'HTML', 'Java'

s1.rate_hw(l1, 'Python', 9)
s1.rate_hw(l2, 'Java', 10)
s1.rate_hw(l1, 'C#', 5)

s2.rate_hw(l2, 'HTML', 8)
s2.rate_hw(l1, 'Python', 4)
s2.rate_hw(l2, 'Java', 7)

r1.rate_hw(s1, 'Python', 9)
r1.rate_hw(s1, 'Python', 10)
r1.rate_hw(s1, 'Python', 9)

r2.rate_hw(s2, 'Java', 7)
r2.rate_hw(s2, 'Java', 9)
r2.rate_hw(s2, 'Java', 8)

print(f'{s1}\n{"-"*30}\n{s2}\n{"-"*30}\n{l1}\n{"-"*30}\n{l2}\n{"-"*30}\n{r1}\n{"-"*30}\n{r2}\n{"-"*30}\n{s1 > s2}\n{l1 < l2}')


def students_average_hw(students_list, course):
    grade_list = []
    for student in students_list:
        if course in student.grades:
            grade_list.append(student.grades)
    for i in grade_list:
        return round(mean(i.get(course)))

res = students_average_hw([s1, s2], 'Python')
print('Средняя оценка всех студентов:', res)


def lecturer_average_hw(lecturer_list, course):
    grade_list = []
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            grade_list.append(lecturer.grades)
    for i in grade_list:
        return round(mean(i.get(course)))

res = lecturer_average_hw([s1, s2], 'Python')
print('Средняя оценка всех лекторов:', res)