#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter
#   должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых
#   пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

def my_func():
    summa = 0
    a = 1
    while a == 1:
        chisla = input('Введите строку чисел через пробел или введите "N" для выхода: ').split()
        result = 0
        for el in range(len(chisla)):
            if chisla[el] == 'N':
                a = 2
                break
            else:
                result = result + int(chisla[el])
        summa = summa + result
        print('Сумма элементов равна', summa, '!')
    print('Сумма элементов равна', summa, '! Выход!')

my_func()
my_func()
