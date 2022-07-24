from collections.abc import Generator


class NumberSquares:
    def __init__(self, numb: int) -> None:
        self.numb = numb
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self) -> int:
        self.counter += 1
        if self.counter <= self.numb:
            return self.counter ** 2
        raise StopIteration


# square = NumberSquares(10)
# for i in square:
#     print(i)


def generate_number_squares(number: int) -> Generator:
    for i_numb in range(1, number + 1):
        yield i_numb ** 2


gen = generate_number_squares(number=10)
for i in gen:
    print(i)

square_generator = (numb ** 2 for numb in range(1, 15 + 1))

# for i in square_generator:
#     print(i)


