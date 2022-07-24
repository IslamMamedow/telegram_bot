from typing import Generator
import os


def counter_string_in_python_file(path_to_directory) -> Generator:
    for elem in os.listdir(path_to_directory):
        temp_path = os.path.join(path_to_directory, elem)
        if os.path.isdir(temp_path):
            yield from counter_string_in_python_file(temp_path)
        elif os.path.isfile(temp_path) and elem.endswith('.py'):
            with open(temp_path, 'r') as file_for_read:
                for line in file_for_read:
                    if len(line.split()) != 0 and not line.startswith('#'):
                        yield line


test = counter_string_in_python_file(os.path.abspath(os.path.join('..', '..', 'Module25')))
for i in test:
    print(i)
# TODO Требовалось посчитать строки кода, а не выводить их текст в консоль
