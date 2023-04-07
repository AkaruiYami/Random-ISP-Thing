import os
import matplotlib.pyplot as plt


class LinerEQSolver:
    def read_csv(self, filename, delimeter=",", header=None):
        with open(filename, "r") as file:
            data = file.read().splitlines()
        if header is None:
            header = data.pop(0).split(delimeter)
        self.variables = header
        self.headers = header[1:]

        try:
            self.X = [int(x.split(delimeter)[0]) for x in data]
        except ValueError:
            self.X = [float(x.split(delimeter)[0]) for x in data]

        str_vals = [line[line.find(delimeter) + 1 :] for line in data]
        str_vals = ",".join(str_vals)
        self.values = str_vals.split(",")

    def to_xy(self, header):
        x = []
        y = []
        for _x, _y in zip(self.X, self.get_values(header)):
            if _y == "Y":
                continue
            x.append(_x)
            y.append(int(_y == "Y*"))
        return x, y

    def get_values(self, header):
        n = len(self.headers)
        i = self.headers.index(header)
        return self.values[i::n]

    def get_value(self, header, i):
        vals = self.get_values(header)
        return vals[i]

    def show(self):
        ax = plt.subplot()
        for header in self.headers:
            x, y = self.to_xy(header)
            ax.plot(x, y, label=header)
            ax.legend()
        plt.show()

    def cal_gradient(self, point0, point1):
        x0, y0 = point0
        x1, y1 = point1
        return (y1 - y0) / (x1 - x0)

    def cal_c(self, x, y, m):
        return y - m * x

    def cal_liner_eq(self, point0, point1):
        m = self.cal_gradient(point0, point1)
        c = self.cal_c(point0[0], point0[1], m)
        return f"y={m}x{c:+}"

    def get_changed_points(self, header):
        x, y = self.to_xy(header)
        r = []
        for i in range(len(y) - 1):
            if y[i] == y[i + 1]:
                continue
            point0 = (x[i], y[i])
            point1 = (x[i + 1], y[i + 1])
            r.append((point0, point1))
        return r

    def print_eq(self):
        for header in self.headers:
            print(f"{header}".center(25, "="))
            p_pairs = self.get_changed_points(header)
            for points in p_pairs:
                point0, point1 = points
                range_msg = f"{point0[0]}<=x<={point1[0]}"
                print(f"{self.cal_liner_eq(point0, point1)}; {range_msg}")


file = os.path.join(os.path.dirname(__file__), "data/test.csv")
solver = LinerEQSolver()
solver.read_csv(file)
solver.print_eq()
solver.show()
