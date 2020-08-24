import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
a = str(input())
for i in range(0, len(a)):
    print('\'{}\''.format(a[i]))
