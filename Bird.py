from Animal import Animal


class Mammal(Animal):
    def __init__(self, name, age, weight, sound, speed):
        super().__init__(name,age,weight,sound)
        self.__speed = speed

    def give_sound(self):
        return self._sound


