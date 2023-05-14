omg = "aaa bb ccc dd"


def remove_white_spaces(text):
    return [item for item in text if item != " "]


def count_letters(text):
    count = {}
    for item in text:
        count[item] = count[item] + 1 if count.get(item) else 1
    return list(count.items())


def get_most_repeated_letters(letters):
    cen = 0
    for item in letters:
        if cen < item[1]:
            cen = item[1]
    return list(filter(lambda letter: letter[1] == cen, letters))


def print_result(letters):
    count = letters[0][1]
    letters = ", ".join([item[0] for item in letters])
    print(f"Los caractere que más se repiten con {count} son:")
    print(f"{letters}")


def main(text):
    _list = remove_white_spaces(text)
    count = count_letters(_list)
    count = get_most_repeated_letters(count)
    print_result(count)


main(omg)
