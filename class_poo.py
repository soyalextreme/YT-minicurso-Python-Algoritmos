""" 
    POO EN PYTHON
"""


class Person:
    def __init__(self, name, age):
        # propiedades ocultas
        self._name = name
        self._age = age
            
    def say_hello(self):
        print(f"{self._name}: Says hello!")

    def _get_name(self):
        return self._name

    def _set_name(self, new_name):
        self._name = new_name

    @staticmethod
    def print_hello():
        print("Hello")

    name = property(_get_name, _set_name)


class Worker:

    def __init__(self, job):
        self._job = job

    def work(self):
        print(f"Estoy trabajndo de {self._job}")


class Deportista(Person, Worker):

    def __init__(self, name, age, job):
        Person.__init__(self, name, age)
        Worker.__init__(self, job )

    def work(self):
        print(f"Estoy entrenando de {self._job}")
    

if __name__ == "__main__":
    alex = Person("alex", 22)
    rafael = Deportista("Rafael", 32, "Tenista")

    rafael.say_hello()
    rafael.work()

    alex.name = "Alejandro"
    print(alex.name)

    alex.say_hello()



