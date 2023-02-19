def words_sorting(*args):
    words = {}
    total_sum = 0

    for word in args:
        words[word] = 0
        for alpha in word:
            words[word] += ord(alpha)
            total_sum += words[word]
    result = ''
    if total_sum % 2 == 0:
        sort_words = sorted(words.items(), key=lambda x: (x[0]))
    else:
        sort_words = sorted(words.items(), key=lambda x: -(x[1]))

    for key, value in sort_words:
        result += f"{key} - {value}\n"
    return result


print(words_sorting('escape', 'charm', 'mythology'))
