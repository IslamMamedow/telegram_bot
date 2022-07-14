class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):
    job_title = 'Работник'

    def salary_calculator(self):
        pass

    def print_info(self):
        print(f'Должность: {self.job_title}:\n   Имя Фамилия: {self.get_name()} {self.get_surname()}\t'
              f'Возраст: {self.get_age()}\n   Зарплата: {self.salary_calculator()}\n')


class Manager(Employee):
    job_title = 'Менеджер'

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary_calculator(self):
        return 13000


class Agent(Employee):
    job_title = 'Агент'

    def __init__(self, name, surname, age, volume_of_sales):
        super().__init__(name, surname, age)
        self.volume_of_sales = volume_of_sales

    def salary_calculator(self):
        return 5000 + self.volume_of_sales / 100 * 5


class Worker(Employee):
    job_title = 'Рабочий'

    def __init__(self, name, surname, age, hours_worked):
        super().__init__(name, surname, age)
        self.hours_worked = hours_worked

    def salary_calculator(self):
        return 100 * self.hours_worked


def add_employee():
    emp_name = input('\nВведите имя: ')
    emp_surname = input('Введите фамилию: ')
    emp_age = int(input('Введите возраст: '))

    return emp_name, emp_surname, emp_age


persons = []
print('Введите информацию о трех менеджерах: ')
for _ in range(3):
    name, surname, age = add_employee()
    persons.append(Manager(name, surname, age))

print('Введите информацию о трех агентах: ')
for _ in range(3):
    name, surname, age = add_employee()
    volume_of_sales = int(input('Введите объем продаж агента: '))
    persons.append(Agent(name, surname, age, volume_of_sales))


print('Введите информацию о трех рабочих: ')
for _ in range(3):
    name, surname, age = add_employee()
    hours_worked = int(input('Введите количество отработанных часов: '))
    persons.append(Worker(name, surname, age, hours_worked))


for person in persons:
    person.print_info()
