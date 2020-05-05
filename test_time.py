import time


# print(time.clock())    # в Unix, возвращает текущее время. В Windows, возвращает время, прошедшее с момента первого вызова данной функции.

print(time.ctime())
print(type(time.ctime()))

b = time.ctime().split()
c = b[3].split(':')
d = int(c[2])

print(b)
print(c)
print(d)
print(type(d))