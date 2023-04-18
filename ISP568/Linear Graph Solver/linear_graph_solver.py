import argparse
from decimal import Decimal


def to_decimal(*args):
    _to_dec = lambda x: Decimal(str(x))
    return list(map(_to_dec, args))


def add_decimal(a, b):
    a, b = to_decimal(a, b)
    return float(a + b)


def sub_decimal(a, b):
    a, b = to_decimal(a, b)
    return float(a - b)


def mul_decimal(a, b):
    a, b = to_decimal(a, b)
    return float(a * b)


def div_decimal(a, b):
    a, b = to_decimal(a, b)
    return float(a / b)


def cal_m(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return div_decimal(sub_decimal(y2, y1), sub_decimal(x2, x1))


def cal_c(m, x, y):
    return sub_decimal(y, mul_decimal(m, x))


def get_linear_eq(point1, point2):
    m = cal_m(point1, point2)
    c = cal_c(m, *point2)
    return f"y={m}x{c:+}"


def get_y_at(x, m, c):
    return add_decimal(mul_decimal(m, x), c)


def get_y_from_points(x, point1, point2):
    m = cal_m(point1, point2)
    c = cal_c(m, *point2)
    return get_y_at(x, m, c)


def full_solve(x, point1, point2):
    eq = get_linear_eq(point1, point2)
    y = get_y_from_points(x, point1, point2)
    print(eq, f"--- when x = {x}, y = {y}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    filereader = parser.add_argument_group("File", "Read input from file")
    singlereader = parser.add_argument_group(
        "Single Input", "Read single input from command line"
    )
    filereader.add_argument("-r", type=str)
    singlereader.add_argument("-x", type=float, metavar="x")
    singlereader.add_argument("-p1", "--point1", type=float, nargs=2)
    singlereader.add_argument("-p2", "--point2", type=float, nargs=2)

    args = parser.parse_args()

    if args.r:
        with open(args.r, "r") as file:
            data = file.read().splitlines()
        for i, line in enumerate(data):
            x, *points = line.split()
            p1 = points[: len(points) // 2]
            p2 = points[len(points) // 2 :]
            print(f"Input {i}".center(30, "="))
            full_solve(x, p1, p2)

    x = args.x
    p1 = args.point1
    p2 = args.point2

    if all([x, p1, p2]):
        full_solve(x, p1, p2)
    elif any([x, p1, p2]):
        raise ValueError("Must suplly enough argument, x, point1, and point2")
