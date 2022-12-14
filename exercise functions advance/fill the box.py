def fill_the_box(height, lenght, width, *args):
    volume = height * lenght * width
    cub_left = 0
    for el in args:
        if el == 'Finish':
            break
        if el > volume:
            el -= volume
            cub_left += el
            volume = 0
        else:
            volume -= el
    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cub_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
