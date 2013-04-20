dic = {'arun': 123213, 'hari': 31212, 'akila': 321, 'varun': 12132, 'apple': 3212}
u1 = {'arun': 123123, 'orange': 1324214}
u2 = {'akila': 1234124, 'apple': 123123}
u3 = {'hari': 144}
u4 = {'anna': 23322}
for key, value in dic.iteritems():
    try:
        A = u1.get(key, 0)
        B = u2.get(key, 0)
        C = u3.get(key, 0)
        D = u4.get(key, 0)
    except KeyError:
        continue
    print A, B, C, D





