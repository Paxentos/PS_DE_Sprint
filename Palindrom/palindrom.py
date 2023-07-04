a = 'abcd'
b = 'taco cat'
c = 'black cat'
d = 'rotator'

b = b.replace(' ', '')
c = c.replace(' ', '')

if a[:] == a[::-1]:
    print("True")
else:
    print("False")
if b[:] == b[::-1]:
    print("True")
else:
    print("False")
if c[:] == c[::-1]:
    print("True")
else:
    print("False")
if d[:] == d[::-1]:
    print("True")
else:
    print("False")
    
