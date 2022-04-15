from itertools import count


def fast_pow(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = fast_pow(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p


def powm(a: int, b: int, n: int) -> int:
    """
    Функция быстрого возведения числа в степень
     a ^ b Mod n
    """
    a_list = [a]
    b = bin(b).replace('0b', '')
    a_0 = a
    for i in range(1, len(b)):
        if int(b[i]) == 0:
            a_list.append(a_list[i - 1] ** 2 % n)
        else:
            a_list.append(a_0 * a_list[i - 1] ** 2 % n)

    return a_list[-1]


def tryParseInt(s, base=10):
    try:
        return int(s, base), True
    except ValueError:
        return 0, False


def extended_Euclidean_algorithm(a, b):
    """ Расширенный алгоритм Евклида. Функция фозвращает X, Y, НОД """
    table = [{'A': a, 'B': b, 'A mod B': a % b, 'A div B': a // b}]

    for i in count(start=0, step=1):
        cur_a = table[i]['B']
        cur_b = table[i]['A mod B']
        if cur_a != 1 and cur_b != 0:
            table.append({'A': cur_a, 'B': cur_b, 'A mod B': cur_a % cur_b, 'A div B': cur_a // cur_b})
        else:
            break

    table[-1]['x'], table[-1]['y'] = 0, 1

    for i in range(len(table) - 2, -1, -1):
        table[i]['x'] = table[i + 1]['y']
        table[i]['y'] = table[i + 1]['x'] - table[i + 1]['y'] * table[i]['A div B']

    return table[0]['x'], table[0]['y'], table[-1]['B']


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b