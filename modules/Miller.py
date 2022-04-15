from random import randint, randrange
from modules.pows import powm, fast_pow
import math


def nBitRandom(n):
    """ Фунция для генерации n - битного числа """
    return randrange(fast_pow(2, n-1)+1, fast_pow(2, n)-1)


def Miller_Rabin(num, test_count):
    """
    Тест Миллера Рабина на простоту
    :param num: число, которое мы тестируем
    :return: True - число простое / False - число составное
    """
    amount = int(math.log(num, 2))
    # счетчик удачных прохождений теста
    c = 0
    # Представим num − 1 в виде 2^s * t,
    # где t нечётно
    # можно сделать последовательным делением num - 1 на 2.
    t, s = num - 1, 0
    while t % 2 == 0 and num-1 != 2**s * t:
        t = t // 2

    # Цикл А: повторить test_count раз
    for i in range(test_count):
        if milrab(num, t, s):
            c += 1
    if c == test_count:
        return True
    else:
        return False


def milrab(p, t, s):
    # Выбрать случайное целое число a в отрезке [2, num − 1]
    a = randint(2, p - 1)
    # x = a^t mod num,
    # вычисляется с помощью алгоритма возведения в степень по модулю
    x = powm(a, t, p)
    # если x = 1 или x = num − 1, то перейти на следующую итерацию цикла А
    if x == 1 or x == p - 1:
        return True
    # цикл B: повторить s − 1 раз
    while s > 1:
        # x = x ^ 2 mod num
        x = powm(x, 2, p)
        #  если x = 1, то вернуть составное
        if x == 1:
            return False
        # если x = n − 1, то перейти на следующую итерацию цикла A
        if x == p - 1:
            return True
        s = s - 1
    # вернуть составное
    return False
