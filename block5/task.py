# TODO 1. Generate first N numbers of fibonacci sequence using generators

first_n = int(input())


def fibonacci_sequence(n):
    previous = 0
    current = 1

    for _ in range(n):
        yield previous
        previous, current = current, previous+current


a = fibonacci_sequence(first_n)

for i in a:
    print(i)


# TODO 2. Implement a custom iteration pattern that's different than the usual built-in functions
#  (e.g., range(), reversed(), etc.).

class InverseNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        x = round(1 / self.a, 4)
        return x


my_inverse_numbers = InverseNumbers()
my_iter = iter(my_inverse_numbers)

print(next(my_iter))
print(next(my_iter))


# TODO 3. Create a function that gets a generator and N as arguments.
#  The function returns generator discard the first N items.


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


def discard_first_n(gen, n):
    for _ in range(n):
        next(gen())
    return gen


example = discard_first_n(infinite_sequence, 5)
