numbers = input().split('|')

sublist = []
result = []
while numbers:

    sublist = numbers.pop().split()

    for el in sublist:
        result.append(el)

print(*result, end = '')