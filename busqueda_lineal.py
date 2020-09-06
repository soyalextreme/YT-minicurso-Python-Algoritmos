"""
    ALGORITMOS DE ORDENAMIENTO DE NUMEROS
    BUSQUEDA LINEAL
    BUSQUE BINARIA
"""

import random


def busqueda_lineal(n, ln):
    """ Search a number in a list """
    counter = 0

    for num in ln:
        counter += 1
        if n == num:
            return True, counter

    return False, counter


def busqueda_binaria(inicio, final, n, ln_ordenada, counter=0):
    """ Search a number in a list in a more eficient way """
    # [2, 22, 30, 50, 100]
    counter += 1
    medio = (inicio + final) // 2

    if inicio >= final:
        return False, counter

    if ln_ordenada[medio] == n:
        return True, counter
    elif ln_ordenada[medio] < n:
        return busqueda_binaria(medio + 1, final, n, ln_ordenada, counter)
    else:
        return busqueda_binaria(inicio, medio - 1, n, ln_ordenada, counter)


if __name__ == "__main__":
    n = int(input("Number you are searching: "))
    s = int(input("Size of the list:"))
    ln = [random.randint(0, 50) for s in range(s)]
    print(ln)
    f_l, c_l = busqueda_lineal(n, ln)
    ln_ordenada = sorted(ln)
    f_b, c_b = busqueda_binaria(0, s, n, ln_ordenada)

    print(f_l, c_l)
    print(f_b, c_b)
