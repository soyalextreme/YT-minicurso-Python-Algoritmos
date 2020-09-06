""" COMO HACER BIFURCACIONES EN NUESTROS PROGRAMAS
    HACER QUE UNA PARTE DEL CODIGO SE EJECUTE DEPENDIENDO
"""

if __name__ == "__main__":
    name = "Alejandro"
    friend_name = "Juan"
    other_friend_name = "Alex"
    my_age = 22
    my_friend_age = 22

    # bifurcadores 

    if name == friend_name:
        print("Somos tocayos!!!")
    elif name == other_friend_name:
        print("Mi otro amigo si se llama igual a mi")
    elif name != friend_name and name != other_friend_name and other_friend_name != friend_name:
        if my_age == my_friend_age:
            print("Mi amigo y yo no nos llamamos igual pero tenmos la misma edad")
        print("Ninguno de los amigos son tocayos")
    else:
        print("No somos tocayos! :c")

