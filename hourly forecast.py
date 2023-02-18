def forecast(*args):
    location = {}

    for info in args:
        if info[0] not in location:
            location[info[0]] = info[1]
    sorted_location = sorted(location.items(), key=lambda x: (x[1], x[0]))
    sunny = ''
    rainy = ''
    cloudy = ''
    for k, v in sorted_location:
        if v == "Sunny":
            sunny += f"{k} - {v}\n"
        elif v == "Cloudy":
            cloudy += f"{k} - {v}\n"
        elif v == 'Rainy':
            rainy += f"{k} - {v}\n"
    return sunny + cloudy + rainy


print(forecast(('Sofia', 'Sunny'), ('London', 'Cloudy'), ('New York', 'Sunny'), ('Tokyo', 'Rainy')))
