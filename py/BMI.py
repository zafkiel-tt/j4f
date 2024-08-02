from math import *
s=input()
s=s.split()
a=float(s[0])
b=float(s[1])
c=a/(b*b)
print('{0:0.1f}'.format(c))
if c<20:
    print('nguoi gay')
if c<=30 and c>=20:
    print('nguoi li tuong')
else:
    print('nguoi beo')