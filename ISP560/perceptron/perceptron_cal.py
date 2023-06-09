from decimal import Decimal

import activation_function as act_fn


def get_delta_w(x, e, a):
    return x * e * a


def get_output(xs, ws, theta, fn=None):
    if fn is None:
        fn = lambda r: 0 if r < 0 else 1
    t = 0
    for x, w in zip(xs, ws):
        t += x * w
    return fn(t - theta)


def solve_row(xs, ws, yd, alpha, theta, fn=None):
    ya = get_output(xs, ws, theta, fn)
    e = yd - ya
    delta_ws = [get_delta_w(x, e, alpha) for x in xs]
    new_ws = [Decimal(str(w)) + Decimal(str(dw)) for w, dw in zip(ws, delta_ws)]
    new_ws = [float(new_w) for new_w in new_ws]
    return {"ya": ya, "e": e, "delta_ws": delta_ws, "ws": new_ws}


def to_string_list(xs, label):
    return ", ".join(f"{label}{i}={x}" for i, x in enumerate(xs, 1))


def to_string(x, label):
    return f"{label}={x}"


def print_output(xs, yd, ws, ya, e, delta_ws, new_ws):
    out = f"{to_string_list(xs, 'x')}, {to_string(yd, 'yd')}, {to_string_list(ws, 'ws')}, {to_string(ya, 'ya')}, {to_string(e, 'e')}, {to_string_list(delta_ws, 'dw')}, {to_string_list(new_ws, 'ws')}"
    print(out)


def cal_epoch(ixs, ws, yds, alpha, theta, fn=None):
    er1_msg = "Number of weight must be the same as the number of input"
    assert len(ixs[0]) == len(ws), er1_msg

    correct = 0
    for i, xs in enumerate(ixs):
        r = solve_row(xs, ws, yds[i], alpha, theta, fn)
        new_ws = r["ws"]
        print_output(xs, yds[i], ws, r["ya"], r["e"], r["delta_ws"], new_ws)
        ws = new_ws
        if r["e"] == 0:
            correct += 1

    return r, correct


def full_solve(ixs, ws, yds, alpha, theta, epoch=None, fn=None):
    if epoch is None:
        epoch = -1

    i = 0
    while i < epoch or epoch == -1:
        print(f"Epoch {i+1}".center(15, "="))
        r, correct = cal_epoch(ixs, ws, yds, alpha, theta, fn)

        if correct == len(ixs):
            break

        ws = r["ws"]
        i += 1


if __name__ == "__main__":
    # Initialize variables here
    ixs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    ws = [0.3, -0.1]
    yd = [0, 0, 0, 1]
    alpha = 0.1
    theta = 0.2
    epoch = None

    full_solve(ixs, ws, yd, alpha, theta, epoch=epoch, fn=act_fn.step)
