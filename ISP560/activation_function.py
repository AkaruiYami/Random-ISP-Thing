import math


def step(x):
    return 0 if x < 0 else 1


def sign(x):
    return -1 if x < 0 else 1


def sigmoid(x):
    return 1 / (math.exp(-x))


def linear(x):
    return x
