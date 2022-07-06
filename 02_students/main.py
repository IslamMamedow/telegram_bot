class Student:

    def __init__(self, name, group_number, progress):
        self.name = name
        self.group_number = group_number
        self.progress = progress
        self.grade_average = sum(self.progress) / len(self.progress)

    def print_info(self):
        print(f'Имя Фамилия: {self.name}.\nНомер Группы: {self.group_number}.\n'
              f'Успеваемость: {self.progress}\nСредний бал:{self.grade_average}\n')


students = {'Петров Антон': [3, [3, 4, 4, 4, 5]],
            'Иванов Игорь': [2, [4, 4, 5, 5, 4]],
            'Ефремова Анна': [4, [5, 4, 3, 3, 3]],
            'Козлов Максим': [2, [4, 3, 3, 3, 5]],
            'Козлова Мария': [1, [4, 2, 2, 3, 5]],
            'Кузнецов Владимир': [1, [3, 3, 5, 5, 4]],
            'Косова Эля': [2, [4, 5, 5, 5, 5]],
            'Коновалов Иван': [4, [5, 4, 3, 4, 4]],
            'Сурова Инна': [1, [4, 2, 3, 5, 4]],
            'Сюткин Михаил': [1, [3, 3, 2, 5, 4]]
            }

students_with_grade_average = [(Student(student, data[0], data[1]), Student(student, data[0], data[1]).grade_average)
                               for student, data in students.items()]

sorted_grade_average = sorted([students_data[1] for students_data in students_with_grade_average])
sorted_students = []
for grade in sorted_grade_average:
    for student_and_grade_average in students_with_grade_average:
        if grade == student_and_grade_average[1]:
            sorted_students.append(student_and_grade_average[0])
            students_with_grade_average.remove(student_and_grade_average)


for student in sorted_students:
    student.print_info()
