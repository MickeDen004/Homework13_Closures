# Example 1
"""Определение замыкания - функция,
в теле которой присутствуют ссылки на переменные,
объявленные вне тела этой функции в окружающем коде и не являющиеся ее параметрами"""

"""Область видимости переменных
Переменные - глобальные и локальные
В Питоне: Local, Enclosing, Global"""


# Local

def add_two(a):
    x = 2
    return a + x


print(add_two(4))


# Enclosing

def add_four(a):
    x = 2

    def add_some():
        print("x = " + str(x))
        return a + x
    return add_some()


print(add_four(5))

# Global

x = 4


def func():
    return x+3


print(func())


# Built-in - len(), list(), enumerate(), reversed(), sorted(), filter(), map()
pory_roku = ["Wiosna", "Lato", "Jesień", "Zima"]
print(list(enumerate(pory_roku, start=1)))


# Непосредственно замыкания


# def mul(a, b):
#     return a*b
#
#
# print(mul(3, 5))
#
#
# def mul5(a):
#     return mul (5, a)
#
#
# print(mul5(5))


def mul(a):
    def helper(b):
        return a*b
    return helper


print(mul(5)(8))
new_mul5 = mul(5)
print(new_mul5)
print(new_mul5(4))
def fun1(a):
    x = a*3
    def func2(b):
        nonlocal x
        return b + x
    return func2

test_fun = fun1(4)
print(test_fun(7))
d = lambda a, b: {a:b}
a = d(3, 2)
print(a)
print(a[3])

print(a)














def counter():
    def _counter():
        _counter.count += 1
        return _counter.count

    def _reset():
        _counter.count = 0

    _counter.count = 0
    _counter.reset = _reset
    return _counter
