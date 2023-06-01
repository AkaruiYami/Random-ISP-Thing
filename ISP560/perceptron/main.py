from inspect import isfunction

import perceptron_cal
import activation_function as act_func


def get_activation_function():
    is_act_func = lambda n: isfunction(getattr(act_func, n))
    sign_func = [name for name in dir(act_func) if is_act_func(name)]

    print("Choose activation function [default=1] : ")
    for i, name in enumerate(sign_func, 1):
        print(f"[{i}] {name}")
    respond = int(input("Activation Function: ") or 0)

    return getattr(act_func, sign_func[respond - 1])


def prepare_xs(ixs):
    return list(zip(*ixs))


def main():
    nx = int(input("How many x? :"))
    ixs = []
    ws = []
    for i in range(1, nx + 1):
        x = input(f"x{i} [List of int] : ")
        w = input(f"w{i} [float] : ")

        ixs.append(list(map(int, x.split(","))))
        ws.append(float(w))

    for xs in ixs:
        print(" | ".join(map(str, xs)))

    yds = list(map(int, input("Desired Output [List of int] : ").split(",")))
    alpha = float(input("Alpha [float] : "))
    theta = float(input("Theta [float] : "))
    epoch = int(input("Epoch [int] : ") or -1)
    bias = int(input("Bias [1 or -1]: "))
    fn = get_activation_function()

    perceptron_cal.full_solve(prepare_xs(ixs), ws, yds, alpha, theta, bias, epoch, fn)


if __name__ == "__main__":
    main()
