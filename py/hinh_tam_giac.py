from math import sqrt
s = input()
s = s.split()
a =float(s[0])
b =float(s[1])
c =float(s[2])
p=(a+b+c)/2
s=sqrt(p*(p-a)*(p-b)*(p-c))
print('{0:0.1f}'.format(a+b+c))
print('{0:0.1f}'.format(s))