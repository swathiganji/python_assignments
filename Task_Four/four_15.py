import functools
x = [1,2,3,4,5,6,7]
x = functools.reduce(lambda x, y: x*y ,x)
print(x)

#or

a = [1, 2, 3, 4, 5, 6, 7]
b = map(lambda x : x*x, a)
print(list(b))

def foo():
    try:
      return 1
    finally:
      return 2
k = foo()
print(k)


def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()