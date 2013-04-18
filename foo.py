lst = [3, 4, 3, 2, 3, 2, 2, 6]
lst = ' '.join(str(x) for x in lst)

print lst
a = [3, 4, 3]
a = ' '.join(str(x) for x in a)
if a in lst:
    print 'foo'

