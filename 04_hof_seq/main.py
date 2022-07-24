from typing import List, Generator


def q_hofstadter_generator(start_list: List) -> Generator:
    if start_list != [1, 1]:
        return
    sequence = start_list[:]
    while True:
        q = sequence[-sequence[-1]] + sequence[-sequence[-2]]
        sequence.append(q)
        yield q


qseq = q_hofstadter_generator([1, 1])
__length_of_list = 0
for i in qseq:
    if __length_of_list == 70:
        break
    print(i, end=' ')
    __length_of_list += 1




