import random, math


def plus(a, message):
    b = float(message.text)
    b = a + b
    return str(b)


def minus(a, message):
    b = float(message.text)
    b = a - b
    return str(b)


def divide(a, message):
    b = float(message.text)
    b = a / b
    return str(b)


def multiply(a, message):
    b = float(message.text)
    b = a * b
    return str(b)


def sqrt(a, message):
    b = float(message.text)
    b = math.pow(a, 1 / b)
    return str(b)


def log(a, message):
    b = float(message.text)
    b = math.log(a, b)
    return str(b)


def get_lower_float(message):
    c = message.text.split()
    b = float(c[1])
    a = float(c[0])
    b = random.uniform(a, b)
    return str(b)


def get_lower_int(message):
    c = message.text.split()
    b = int(c[1])
    a = int(c[0])
    b = random.randint(a, b)
    return str(b)
