# TODO 1. Copy my_dict to new_dict. Swap keys and values from the new_dictionary
from copy import deepcopy

my_dict = {
    'first_key': 'first_value',
    'second_key': 'second_value',
    'third_key': 'third_value'
}

some_dict = dict(my_dict)
new_dict = {value: key for key, value in my_dict.items()}

# TODO 2. Create a list from my dict keys

keys_list = list(new_dict.keys())

# TODO 3. Create two lists with 5 items in them. Create a dict from those two lists.

first_list = ['1', '2', '3', '4', '5']
second_list = ['a', 'b', 'c', 'd', 'e']

final_dict = dict(zip(first_list, second_list))

# TODO 4. Create a list. Create lambda function that square each element of the list.

list_of_nums = [1, 2, 3, 4, 5]
doubled_list = list(map(lambda n: n ** 2, list_of_nums))

# TODO 5. Create a function that takes all positional arguments and returns their sum.
#  If a value is not number - skip it (use try/except statement).

first_arg = 'a'
second_arg = 2
third_arg = 'b'
fourth_arg = 5
fifth_arg = '23'


def summer(*args):
    answer = 0

    for arg in args:
        try:
            answer += arg
        except TypeError:
            print("Not a number")
    print(answer)


summer(first_arg, second_arg, third_arg, fourth_arg, fifth_arg)


# TODO 6. Create a function foo_1, that takes function foo_2 as a required argument.
#  foo_1 should return result of execution foo_2.


def foo_1():
    def foo_2():
        print("Hi")

    return foo_2


foo_1()


# TODO 7. Create a function that takes any number of positional and keywords arguments.
#  Check keywords arguments, if there are functions among them, call each function and pass
#  all positional arguments as arguments.

def foo(*args):
    print(args)


def some_interesting_function(*args):
    funcs = []
    arguments = []

    for arg in args:
        if isinstance(arg, (str, float, list, int)):
            arguments.append(arg)
        else:
            funcs.append(arg)

    for func in funcs:
        func(*arguments)


some_interesting_function(foo, "def", 1)
