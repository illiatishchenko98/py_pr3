

# def a(value, multiplier=10):
#     """Its def"""
#     return value * multiplier


# print(a(5))


# def print_number_info(num):
#     if (num % 2) == 0:
#         print("Entered number is even")
#     else:
#         print("Entered number is odd")


# def new_def(num):
#     print('Hello', num * num)


# def process_number(num, callback_fn):
#     callback_fn(num)


# entered_num = int(input('Enter any number: '))

# process_number(entered_num, new_def)


# def my_fn(a, b):
#     global abc
#     abc = 24
#     print(a, b)


# my_fn('abc', 'xyz')
# print(abc)


# bool = True
# print(+bool)


# my_car = {
#     'brand': 'Mercedes',
#     'price': 125_000
# }
# print('brand' in my_car)
# print('year' in my_car)
# print('year' not in my_car)

# a = {1324, 23, 121, 'abc'}
# b = {1324, 23, 121, 'abc'}
# print(a == b)
# print(a is b)
# print(1324 in b)


# my_list = []

# print(not my_list)


# a = {22, 24, 25, 'abc'}
# b = {22, 24, 25, 'abc'}
# print(a == b and print('Dict doesnt empty'))

a = {'a': 24,
     'b': 125_000
     }
b = {
    **a,
    'color': 'hameleon'
}
# ab = {
#     **a,
#     **b
# }
ab = a | b
print(ab)
