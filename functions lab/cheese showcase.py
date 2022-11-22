def sorting_cheeses(**kwarks):
    sorted_cheeses = sorted(kwarks.items(), key=lambda x: (-len(x[1]), x[0]))
    result_str = ''
    for key, value in sorted_cheeses:
        value_str = sorted(value, reverse=True)
        result_str += key + '\n'
        result_str += '\n'.join([str(x) for x in value_str]) + '\n'
    return result_str


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125], ))
