lst = [3, 2, 4, 0, 5, 53, 2, 224]
for i in lst:
    try:
        x = (4 / i)
    except ZeroDivisionError:
        continue
    print x