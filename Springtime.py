def start_spring(**kwargs):
    new_list = {}
    for k, v in kwargs.items():
        if v not in new_list:
            new_list[v] = []
        new_list[v].append(k)

    result = ''

    sort_collection = sorted(new_list.items(), key=lambda x: (-len(x[1]), x[0]))

    for key in sort_collection:
        result += f"{key[0]}:\n"
        sort_value = sorted(key[1])
        for value in sort_value:
            result += f"-{value}\n"
    return result


example_objects = {"Swallow": "bird", "Thrushes": "bird", "Woodpeckers": "bird", "Swallows": "bird", "Warbles": "bird",
                   "Shrikes": "bird"}

print(start_spring(**example_objects))