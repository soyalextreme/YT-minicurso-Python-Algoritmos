""" IMPLEMENTACION DE RECURSIVIDAD CON FIBONACCI """


def fibonacci(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    num = int(input("Dame un numero: "))
    n = fibonacci(num)
    print(n)
