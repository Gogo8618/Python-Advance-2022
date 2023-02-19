from collections import deque


def flights(*args):
    flights_info = {}

    args = deque(args)

    while args:
        arg_1 = args.popleft()
        if arg_1 == 'Finish':
            break
        destination = isinstance(arg_1, str)
        if destination:
            if arg_1 not in flights_info:
                flights_info[arg_1] = 0
            arg_2 = args.popleft()
            passengers = isinstance(arg_2, int)
            if passengers:
                flights_info[arg_1] += arg_2
    return flights_info


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
