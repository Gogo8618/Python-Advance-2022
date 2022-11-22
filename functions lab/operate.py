def operate(operator, *args):
    def add():
        return sum(args)

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result
    if operator == '+':
        return add()


print(operate("+", 1, 2, 3))
