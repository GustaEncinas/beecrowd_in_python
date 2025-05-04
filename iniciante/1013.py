val1, val2, val3 = map(int, input().split())
maior1 = (val1 + val2 + abs(val1 - val2)) / 2
maior2 = (maior1 + val3 + abs(maior1 - val3)) / 2
print("{:.0f} eh o maior".format(maior2))