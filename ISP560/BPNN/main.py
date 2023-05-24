import math
import itertools
from decimal import Decimal


def to_matrix(l, n):
    return [l[i : i + n] for i in range(0, len(l), n)]


def to_decimal(x):
    try:
        x = iter(x)
    except TypeError:
        x = str(x)
        return Decimal(x)
    else:
        x = map(str, x)
        return list(map(Decimal, x))


def to_decimal_all(*args):
    return [to_decimal(arg) for arg in args]


def activate_node(values, weights, theta=0.0, decimal_places=4):
    assert len(values) == len(weights)
    values, weights, theta = to_decimal_all(values, weights, theta)
    v_in = sum(v * w for v, w in zip(values, weights)) + theta
    return round(float(1 / (1 + math.exp(-v_in))), decimal_places)


def activate_nodes(values, weights2d, theta=None, decimal_places=4):
    if theta is None:
        theta = [0.0] * len(values)
    node_weights = zip(*weights2d)
    activated_values = [
        activate_node(values, weights, t, decimal_places)
        for weights, t in zip(node_weights, theta)
    ]
    return activated_values


def cal_delta_k(targets, values, decimal_places=4):
    assert len(targets) == len(values)
    targets, values = to_decimal_all(targets, values)
    errors = map(lambda x: x[0] - x[1], zip(targets, values))
    return [
        round(float(e * v * (1 - v)), decimal_places) for e, v in zip(errors, values)
    ]


def get_delta_weight(delta, value, alpha):
    values = to_decimal_all(delta, value, alpha)
    return math.prod(values)


def get_delta_bias(bias, alpha):
    values = to_decimal_all(bias, alpha)
    return math.prod(values)


def cal_delta_weights(deltas, values, alpha, decimal_places=4):
    pairs = itertools.product(values, deltas)
    result = [get_delta_weight(d, v, alpha) for v, d in pairs]
    result = [round(float(r), decimal_places) for r in result]
    return to_matrix(result, len(deltas))


def cal_delta_biases(biases, alpha, decimal_places=4):
    return [round(float(get_delta_bias(b, alpha)), decimal_places) for b in biases]


def get_delta_j_in(values, weights):
    assert len(values) == len(weights)
    values = to_decimal_all(values, weights)
    return sum(v * w for v, w in zip(*values))


def cal_delta_j_ins(values, weights2d, decimal_places=4):
    node_weights = weights2d
    return [
        round(float(get_delta_j_in(values, w)), decimal_places) for w in node_weights
    ]


def cal_delta_j(delta_j_in, values, decimal_places=4):
    assert len(delta_j_in) == len(values)
    values = to_decimal_all(delta_j_in, values)
    return [
        round(float(d_j_in * v * (1 - v)), decimal_places) for d_j_in, v in zip(*values)
    ]


def main():
    alpha = 0.5
    inputs = [0.05, 0.1]
    i_layers = [[0.15, 0.20], [0.25, 0.30]]
    b1 = [0.35, 0.35]
    j_layers = [[0.4, 0.45], [0.5, 0.55]]
    b2 = [0.6, 0.6]
    targets = [0.01, 0.99]

    z = activate_nodes(inputs, i_layers, b1)
    print(z)

    y = activate_nodes(z, j_layers, b2)
    print(y)

    delta_ks = cal_delta_k(targets, y)
    print(delta_ks)

    delta_ws = cal_delta_weights(delta_ks, z, alpha)
    print(delta_ws)

    delta_b2 = cal_delta_biases(b2, alpha)
    print(delta_b2)

    delta_j_ins = cal_delta_j_ins(delta_ks, j_layers, 6)
    print(delta_j_ins)

    delta_js = cal_delta_j(delta_j_ins, z, 6)
    print(delta_js)


x = [0.15, 0.25]
w = [0.05, 0.1]
r = activate_node(x, w, 0.35)
print(r)

a = [1, 2]
b = [3, 4]
r = itertools.product(a, b)
print(list(r))

main()
