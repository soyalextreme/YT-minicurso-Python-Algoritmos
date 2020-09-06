"""
    ABSTRACCION DE CODIGO CON LAS FUNCIONES 
    ESCRIBE UNA VEZ USALO MUCHAS
"""

def verify_friend_name_age(my_age, my_friend_age, my_friend_name, my_name="Alex" ):
    """ Verifica que mi amigo y yo tengamos la misma edad y nos llamemos igual """ 
    # body function
    
    if my_name == my_friend_name and my_age == my_friend_age:
        print("My friend and I have the same name and the same age")
    elif my_name != my_friend_name and my_age == my_friend_age:
        print("We dont have the same name but we have the same age")
    elif my_name == my_friend_name and my_age != my_friend_age:
        print("We have the same name but we have diferent ages")
    else:
        print("We dont have the same name neither the same age")
    # implement new functions here 

    
    
def say_hello():
    print("Hello world")



if __name__ == "__main__":
    say_hello()
    verify_friend_name_age(22, 19, "David") 
    verify_friend_name_age(22, 22, "Alex", "Fernando") 
    verify_friend_name_age(22, 22, "David") 
    
    



