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


def get_delta_weight(delta, value, alpha):
    values = to_decimal_all(delta, value, alpha)
    return math.prod(values)


def get_delta_bias(bias, alpha):
    values = to_decimal_all(bias, alpha)
    return math.prod(values)


def get_delta_j_in(values, weights):
    assert len(values) == len(weights)
    values = to_decimal_all(values, weights)
    return sum(v * w for v, w in zip(*values))


def cal_delta_weights(deltas, values, alpha, decimal_places=4):
    pairs = itertools.product(values, deltas)
    result = [get_delta_weight(d, v, alpha) for v, d in pairs]
    result = [round(float(r), decimal_places) for r in result]
    return to_matrix(result, len(deltas))


def cal_delta_biases(biases, alpha, decimal_places=4):
    return [round(float(get_delta_bias(b, alpha)), decimal_places) for b in biases]


def cal_delta_k(targets, values, decimal_places=4):
    assert len(targets) == len(values)
    targets, values = to_decimal_all(targets, values)
    errors = map(lambda x: x[0] - x[1], zip(targets, values))
    return [
        round(float(e * v * (1 - v)), decimal_places) for e, v in zip(errors, values)
    ]


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


def cal_errors(targets, ys):
    assert len(targets) == len(ys)
    return sum(1 / 2 * math.pow(t - y, 2) for t, y in zip(targets, ys))


def update_weights(old_w, delta_w, decimal_places=4):
    r = []
    for con in zip(old_w, delta_w):
        pairs = zip(*to_decimal_all(*con))
        r.append([round(float(w + d), decimal_places) for w, d in pairs])
    return r


def update_biases(old_b, delta_b, decimal_places=4):
    pairs = zip(old_b, delta_b)
    return [round(float(b + d), decimal_places) for b, d in to_decimal_all(*pairs)]


def print1d(label, items):
    for i, _item in enumerate(items, start=1):
        print(f"{label}{i} =", _item)


def print2d(label, items):
    for j, _items in enumerate(items, start=1):
        print1d(label + str(j), _items)


def solve_once(inputs, i_layers, b1, j_layers, b2, targets, alpha):
    z = activate_nodes(inputs, i_layers, b1)
    print1d("z", z)

    y = activate_nodes(z, j_layers, b2)
    print1d("y", y)

    delta_ks = cal_delta_k(targets, y)
    print1d("δk", delta_ks)

    delta_ws = cal_delta_weights(delta_ks, z, alpha)
    print2d("Δw", delta_ws)

    delta_b2 = cal_delta_biases(b2, alpha)
    print1d("Δb2", delta_b2)

    delta_j_ins = cal_delta_j_ins(delta_ks, j_layers, 6)
    print1d("δj_in", delta_j_ins)

    delta_js = cal_delta_j(delta_j_ins, z, 6)
    print1d("δj", delta_js)

    delta_vs = cal_delta_weights(delta_js, inputs, alpha, 6)
    print2d("Δv", delta_vs)

    delta_b1 = cal_delta_biases(b1, alpha)
    print1d("Δb1", delta_b1)

    new_ws = update_weights(j_layers, delta_ws)
    print2d("new w", new_ws)

    new_vs = update_weights(i_layers, delta_vs)
    print2d("new v", new_vs)

    new_b1 = update_biases(b1, delta_b1)
    print1d("new b1", new_b1)

    new_b2 = update_biases(b2, delta_b2)
    print1d("new b2", new_b2)

    error = cal_errors(targets, y)
    print("Error = ", error)


def main():
    alpha = 0.1
    inputs = [1, 0]
    i_layers = [[0.1, 0.3], [-0.2, 0.2]]
    b1 = [0.1, -0.2]
    j_layers = [[0.1, 0.2], [-0.3, 0.1]]
    b2 = [-0.2, -0.1]
    targets = [0, 1]

    solve_once(inputs, i_layers, b1, j_layers, b2, targets, alpha)


if __name__ == "__main__":
    # TODO: Loop for epoch
    main()
