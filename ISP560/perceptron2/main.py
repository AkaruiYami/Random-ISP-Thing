import perceptron_cal


def prepare_xs(ixs):
    return list(zip(*ixs))


def main():
    nx = int(input("How many x? :"))
    ixs = []
    bs = []
    for i in range(1, nx + 1):
        x = input(f"x{i} [List of int] : ")

        ixs.append(list(map(int, x.split(","))))

    for i, xs in enumerate(ixs):
        print(f"x{i+1} = ", " | ".join(map(str, xs)))
    bs = list(map(int, input("b [List of int] : ").split(",")))
    ts = list(map(int, input("Desired Output [List of int] : ").split(",")))
    alpha = float(input("Alpha [float] : "))
    theta = float(input("Theta [float] : "))
    epoch = int(input("Epoch [int] : "))

    perceptron_cal.full_solve(prepare_xs(ixs), bs, ts, alpha, theta, epoch)


if __name__ == "__main__":
    main()
