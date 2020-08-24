a,b = map(int, input().split())
print(a+b)
if a>b:
    print(a-b)
else:
    print(b-a)
print(a*b)
print(int(round(a/b, 0)))
print(a%b)
print("{0:.2f}".format(round(a/b, 2)))