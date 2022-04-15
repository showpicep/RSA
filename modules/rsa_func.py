from modules.Miller import Miller_Rabin, nBitRandom
from modules.pows import extended_Euclidean_algorithm


def Decor(func):
    def Wrapper(*args, **kwargs):
        p, q = int(args[0], 10), int(args[1], 10)
        return func(p, q)
    return Wrapper


def Get_prime_dig(n_bits):
    cur = nBitRandom(n_bits)
    while not Miller_Rabin(cur, 10):
        cur = nBitRandom(n_bits)

    return cur


@Decor
def Get_n(p, q):
    return p*q


@Decor
def Get_func(p, q):
    return (p-1)*(q-1)


def Get_e(n_bits):
    n = 2*n_bits//3
    cur = nBitRandom(n)
    while not Miller_Rabin(cur, 10):
        cur = nBitRandom(n)

    return cur


@Decor
def Get_d(phi, e):
    """ Вычисляем значение закрытого ключа по алгоритму Евклида """
    _, d, _ = extended_Euclidean_algorithm(phi, e)

    while d < 0:
        d += phi

    return d
