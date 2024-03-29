class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, animal_type, sound):
        self.name = name
        self.animal_type = animal_type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.animal_type}"


