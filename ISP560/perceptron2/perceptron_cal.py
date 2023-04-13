from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Row:
    xs: list[int]
    ws: list[float]
    b: int
    t: int
    y_in: float
    y: int
    delta_ws: list[float]
    delta_b: float
    new_ws: list[float]
    new_wb: float
    e: list[float]

    def to_string_list(self, xs, label):
        return ", ".join(f"{label}{i}={x}" for i, x in enumerate(xs, 1))

    def to_string(self, x, label):
        return f"{label}={x}"

    def print_output(self):
        d_out = [
            self.to_string_list(self.xs, "x"),
            # self.to_string_list(self.ws, "w"),
            self.to_string(self.b, "b"),
            self.to_string(self.t, "t"),
            self.to_string(self.y_in, "y_in"),
            self.to_string(self.y, "y"),
            self.to_string_list(self.delta_ws, "Δw"),
            self.to_string(self.delta_b, "Δb"),
            self.to_string_list(self.new_ws, "w"),
            self.to_string(self.new_wb, "wb"),
            self.to_string(self.e, "error"),
        ]
        print(", ".join(d_out))


def add_float(*args):
    _decimal = lambda x: Decimal(str(x))
    args = tuple(map(_decimal, args))
    return float(sum(args))


def get_delta(x, alpha, e):
    return x * alpha * e


def get_y_in(xs, ws, b, wb):
    return add_float(sum(x * w for x, w in zip(xs, ws)), wb * b)


def get_y(y_in, theta):
    if y_in > theta:
        return 1
    elif -theta <= y_in <= theta:
        return 0
    else:
        return -1


def get_error(t, y):
    return t - y


def solve_row(xs, b, t, ws, wb, alpha, theta):
    y_in = get_y_in(xs, ws, b, wb)
    y = get_y(y_in, theta)
    e = get_error(t, y)
    delta_ws = [get_delta(x, alpha, e) for x in xs]
    delta_b = get_delta(b, alpha, e)
    new_ws = [add_float(w, delta_w) for w, delta_w in zip(ws, delta_ws)]
    new_wb = add_float(wb, delta_b)
    return Row(xs, ws, b, t, y_in, y, delta_ws, delta_b, new_ws, new_wb, e)


def cal_epoch(ixs, bs, ts, ws, wb, alpha, theta):

    for xs, b, t in zip(ixs, bs, ts):
        row = solve_row(xs, b, t, ws, wb, alpha, theta)
        wb = row.new_wb
        ws = row.new_ws
        row.print_output()
    return row


def full_solve(ixs, bs, ts, alpha, theta, epoch=5):
    ws = [0.0] * len(ixs[0])
    wb = 0.0

    for i in range(epoch):
        print(f"Epoch {i+1}".center(15, "="))
        row = cal_epoch(ixs, bs, ts, ws, wb, alpha, theta)
        ws = row.new_ws
        wb = row.new_wb


if __name__ == "__main__":
    ixs = [[1, 1], [1, 0], [0, 1], [0, 0]]
    b = [1, 1, 1, 1]
    ts = [1, 1, 1, -1]
    alpha = 0.1
    theta = 0.5

    full_solve(ixs, b, ts, alpha, theta, epoch=2)
