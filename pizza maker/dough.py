class Dough:

    def __init__(self, flour_type: str, backing_technique: str, weight: float):
        self.flour_type = flour_type
        self.backing_technique = backing_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, value):
        if value == "":
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = value


    @property
    def backing_technique(self):
        return self.__backing_technique

    @backing_technique.setter
    def backing_technique(self, value):
        if value == "":
            raise ValueError("The baking technique cannot be an empty string")

        self.__backing_technique = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value
