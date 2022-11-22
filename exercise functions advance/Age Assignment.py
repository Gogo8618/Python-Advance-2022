def age_assignment(*args, **kwargs):
    result = {}
    for el in args:
        first_alpha = el[0]
        age = kwargs[first_alpha]
        result[el] = age
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36,A=22, B=61))