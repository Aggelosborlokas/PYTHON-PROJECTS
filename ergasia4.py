def times(x):
    x = str(x) + "*"
    return x


def minus(x):
    x = str(x) + "-"
    return x


def plus(x):
    x = str(x) + "+"
    return x


def chooseoperation(y, calc, number):
    if calc == "*":
        return number * y
    elif calc == "-":
        return y - number
    elif calc == "+":
        return number + y


def zero(x=10):
    if x == 10:
        return 0
    else:
        y = 0
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def one(x=10):
    if x == 10:
        return 1
    else:
        y = 1
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def two(x=10):
    if x == 10:
        return 2
    else:
        y = 2
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def three(x=10):
    if x == 10:
        return 3
    else:
        y = 3
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def four(x=10):
    if x == 10:
        return 4
    else:
        y = 4
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def five(x=10):
    if x == 10:
        return 5
    else:
        y = 5
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def six(x=10):
    if x == 10:
        return 6
    else:
        y = 6
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def seven(x=10):
    if x == 10:
        return 7
    else:
        y = 7
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def eight(x=10):
    if x == 10:
        return 8
    else:
        y = 8
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


def nine(x=10):
    if x == 10:
        return 9
    else:
        y = 9
        number = int(x[0])
        calc = x[1]
        print(chooseoperation(y, calc, number))


zero(plus(one()))
two(minus(three()))
four(times(five()))
six(plus(seven()))
eight(minus(nine()))
