def students_credits(*args):
    credits_info = {}
    sum_all_credits = 0
    info_string = []
    for info in args:
        course_name, course_credits, max_test_points, dyan_points = info.split('-')

        procent_of_credits = int(dyan_points) / int(max_test_points)
        dyan_current_credits = procent_of_credits * int(course_credits)
        sum_all_credits += dyan_current_credits
        credits_info[course_name] = dyan_current_credits

    if sum_all_credits >= 240:
        info_string.append(f"Dyan gets a diploma with {sum_all_credits:.1f} credits.")
    else:
        info_string.append(f"Dyan needs {240 - sum_all_credits} credits more for a diploma")
        sorted_info = sorted(credits_info.items(), key=lambda a: -a[1])

        for course_name, d_credits in sorted_info:
            info_string.append(f"{course_name}-{float(d_credits):.1f}")
        return '\n'.join(info_string)


print(students_credits("Computer Science-12-300-250", "Basic Algebra-15-400-200", "Algoritms-25-500-490"))
