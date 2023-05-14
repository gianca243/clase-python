# set significa grupo o conjunto

primer = {1, 2, 1, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
segundo = [3, 4, 5]
segundo = set(segundo)

print(primer | segundo)

print(primer & segundo)

print(primer - segundo)

print(primer ^ segundo)
