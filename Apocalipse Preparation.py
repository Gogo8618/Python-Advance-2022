from collections import deque

textile = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

items = {"MedKit": 0, "Bandage": 0, "Patch": 0}

while textile and medicaments:
    first = textile.popleft()
    second = medicaments.pop()

    sum_of_both = first + second

    if sum_of_both == 30:
        items['Patch'] += 1
    elif sum_of_both == 40:
        items['Bandage'] += 1
    elif sum_of_both == 100:
        items['MedKit'] += 1
    elif sum_of_both > 100:
        items['MedKit'] += 1
        rest = sum_of_both - 100
        medicaments[-1] += rest
    else:
        second += 10
        medicaments.append(second)
sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
if not textile and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textile:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for key in sorted_items:
    if int(key[1]) > 0:
        print(f"{key[0]} - {key[1]}")
if textile:
    print(f"Textiles left: {', '.join(map(str, textile))}")
if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
