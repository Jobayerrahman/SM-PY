x = lambda a : a + 10
print(x(2))


x = lambda a, b : a * b
print(x(3,5))



x = lambda a, b, c : a + b + c
print(x(2,4,4))



def myfunc(n):
    return lambda a : a * n
x = myfunc(10)
print(x(3))


def ourfunc(n):
    return lambda a: a * n
x=ourfunc(10)
y=ourfunc(20)
print(x(2))
print(y(1))