"""
    CICLOS EN PYTHON Y SU USO
    FOR Y WHILE
    PRIMITIVO RANGE()
"""



if __name__ == "__main__":
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    list_names = ["Alejandro", "David", "Fernando"]    
    for name in list_names:
        print(name)
    p_n = []
    for n in range(0,100,2):
        p_n.append(n)
    

    pair_numbers = [n for n in range(0, 100, 2)]


    print(p_n)
    print(pair_numbers)

    for _ in range(100):
        print("hola")
