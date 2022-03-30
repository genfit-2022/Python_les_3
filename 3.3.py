#   3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает
#   сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    if arg_1 <= arg_3 and arg_3 <= arg_2:
        return arg_2 + arg_3
    elif arg_2 <= arg_1 and arg_2 <= arg_3:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2
print(
    my_func(
        int(input('введите arg_1: ')),
        int(input('введите arg_2: ')),
        int(input('введите arg_3: '))
    )
)