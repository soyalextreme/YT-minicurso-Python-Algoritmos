""" ESTRUCTURA DE DATOS MAS COMPLEJOS SETS, LISTAS, DICCIONARIOS, TUPLAS """


if __name__ == "__main__":
    # listas
    name_list = ["Alejandro", "Luis", "Jorge", "David"]
    name_list.append("Manuel")
    name_list.pop(1)
    print(name_list[0:3:2])

    # tuplas 
    age_tuple = (12, 23 , 32, 67)
    print(age_tuple[:3])


    # dictionary

    name_dictionary = {
    "basic_info":{
            "name": "Alejandro",
            "age": 22
        },
    "ubication_info":{
            "country": "Mexico",
            "city": "Tijuana"
        }
    }

    simple_dictionary = {
        "name": "Alejandro",
        "age": 22
    }

    print(name_dictionary)
    print(simple_dictionary)



    # set 
    pair_numbers = {2, 4, 6, 8}
    more_pair_numbers = {8, 16, 100}
    print(pair_numbers)
    print(more_pair_numbers)

    # intesection set
    print(pair_numbers & more_pair_numbers)

    # union set
    print(pair_numbers | more_pair_numbers)

    # diference set 
    print(pair_numbers - more_pair_numbers)

    
