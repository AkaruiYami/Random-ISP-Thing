import copy
import math
from decimal import Decimal


def get_data():
    xs = [1, 1]
    Vs = [[0.5, 0.9], [0.4, 1.0]]
    Ws = [[-1.2], [1.1]]
    thetas = [[0.8, -0.1], [0.3]]
    bias = [[-1, -1], [-1]]
    ts = [0]
    alpha = 0.1

    data = {
        "xs": xs,
        "Vs": Vs,
        "Ws": Ws,
        "thetas": thetas,
        "bias": bias,
        "ts": ts,
        "alpha": alpha,
    }
    return data


def sigmoid(val):
    return 1 / (1 + math.exp(-val))


def activate(vals, ws, b, decimal_places=4):
    val_in = sum(val * w for val, w in zip(vals, ws)) + b
    return round(sigmoid(val_in), decimal_places)


def activate_layer(vals, Ws, bias, thetas, decimal_places=4):
    t_Ws = zip(*Ws)
    activated_nodes = [
        activate(vals, ws, bias[i] * thetas[i], decimal_places)
        for i, ws in enumerate(t_Ws)
    ]
    return activated_nodes


def cal_delta_k(t, y):
    return (t - y) * y * (1 - y)


def cal_delta_ks(ts, ys, decimal_places=4):
    return [round(cal_delta_k(t, y), decimal_places) for t, y in zip(ts, ys)]


def cal_error_gradient(delta_ks, Ws, zs, decimal_places=4):
    delta_jin = [sum(delta_k * w[i] for i, delta_k in enumerate(delta_ks)) for w in Ws]
    delta_j = [
        round(d_jin * z * (1 - z), decimal_places) for d_jin, z in zip(delta_jin, zs)
    ]
    return delta_j


def cal_delta_weight(alpha, deltas, vals, decimal_places=4):
    result = []
    for delta in deltas:
        node = []
        for val in vals:
            r = round(alpha * val * delta, decimal_places)
            node.append(r)
        result.append(node)
    return list(zip(*result))


def cal_delta_bias(alpha, deltas, bias, decimal_places=4):
    return [round(delta * alpha * b, decimal_places) for delta, b in zip(deltas, bias)]


def get_new_weights(Ws, deltas, decimal_places=4):
    new_Ws = copy.deepcopy(Ws)
    for i, delta in enumerate(deltas):
        for j, val in enumerate(delta):
            ws = Decimal(str(new_Ws[i][j])) + Decimal(str(val))
            new_Ws[i][j] = round(float(ws), decimal_places)
    return new_Ws


def print_output(
    zs,
    ys,
    delta_ks,
    delta_js,
    delta_Vs,
    delta_Ws,
    delta_bias1,
    delta_bias2,
    new_Vs,
    new_Ws,
    new_thetas,
):
    def print1d(label, items):
        for i, _item in enumerate(items, start=1):
            print(f"{label}{i} =", _item)

    def print2d(label, items):
        for j, _items in enumerate(items, start=1):
            print1d(label + str(j), _items)

    print1d("z", zs)
    print1d("y", ys)
    print1d("d_k", delta_ks)
    print1d("d_j", delta_js)
    print2d("D_V", delta_Vs)
    print1d("d_b1", delta_bias1)
    print2d("D_W", delta_Ws)
    print1d("d_b2", delta_bias2)
    print2d("new Bs", new_thetas)
    print2d("new V", new_Vs)
    print2d("new W", new_Ws)


def main():
    data = get_data()
    zs = activate_layer(data["xs"], data["Vs"], data["bias"][0], data["thetas"][0])
    ys = activate_layer(zs, data["Ws"], data["bias"][1], data["thetas"][1])
    delta_ks = cal_delta_ks(data["ts"], ys)
    delta_js = cal_error_gradient(delta_ks, data["Ws"], zs)
    delta_Vs = cal_delta_weight(data["alpha"], delta_js, data["xs"])
    delta_Ws = cal_delta_weight(data["alpha"], delta_ks, zs)
    delta_bias1 = cal_delta_bias(data["alpha"], delta_js, data["bias"][0])
    delta_bias2 = cal_delta_bias(data["alpha"], delta_ks, data["bias"][1])
    new_Vs = get_new_weights(data["Vs"], delta_Vs)
    new_Ws = get_new_weights(data["Ws"], delta_Ws)
    new_thetas = get_new_weights(data["thetas"], [delta_bias1, delta_bias2])

    print_output(
        zs,
        ys,
        delta_ks,
        delta_js,
        delta_Vs,
        delta_Ws,
        delta_bias1,
        delta_bias2,
        new_Vs,
        new_Ws,
        new_thetas,
    )


if __name__ == "__main__":
    main()
