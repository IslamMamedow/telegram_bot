import os
from typing import Generator


def get_file_path(catalog_to_find: str, path=os.path.abspath(os.path.sep)) -> Generator:

    for i_elem in os.listdir(path):
        temp_path = os.path.join(path, i_elem)
        if catalog_to_find == i_elem:
            yield temp_path
            print(f'Каталог {catalog_to_find} найден!')
            return
        elif os.path.isdir(temp_path):
            yield from get_file_path(catalog_to_find=catalog_to_find, path=temp_path)
        elif os.path.isfile(temp_path):
            yield temp_path


# catalogs = get_file_path(path=os.path.abspath(os.path.join('..', '..', '..')), catalog_to_find='Module22')
# for i in catalogs:
#     print(i)





