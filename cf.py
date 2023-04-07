import re
import argparse
from functools import reduce
from dataclasses import dataclass, field


@dataclass
class CF:
    h: float
    e: float
    cf: float = field(init=False)

    def __post_init__(self):
        self.cf = round(self.h * self.e, 6)

    @staticmethod
    def from_string(h: str | float, e: str) -> "CF":
        p_and = re.compile(r"(\d\.?\d*(?=&)[&.\d]+)")
        p_or = re.compile(r"(\d\.?\d*(?=\|)[|.\d]+)")

        e = e.replace(" ", "")
        m_and = re.findall(p_and, e)
        for m in m_and:
            p = m.replace(".", "\.")
            e = re.sub(p, str(min(map(float, m.split("&")))), e)
        m_or = re.findall(p_or, e)
        for m in m_or:
            p = m.replace(".", "\.").replace("|", "\|")
            e = re.sub(p, str(max(map(float, m.split("|")))), e)
        h, e = map(float, [h, e])
        return CF(h, e)


class Solver:
    def __init__(self):
        self.cf_list = []

    def add_cf(self, cf: CF):
        self.cf_list.append(cf)

    def solve_cf(self):
        if not self.cf_list:
            return
        r = reduce(Solver.combine_cf, self.cf_list)
        return r

    @staticmethod
    def combine_cf(cf1: CF | float, cf2: CF | float):
        if isinstance(cf1, CF):
            cf1 = cf1.cf
        if isinstance(cf2, CF):
            cf2 = cf2.cf
        if cf1 >= cf2 > 0:
            ans = cf1 + cf2 * (1 - cf1)
        elif cf1 <= cf2 < 0:
            ans = cf1 + cf2 * (1 + cf1)
        else:
            ans = (cf1, cf2) / (1 - min(abs(cf1), abs(cf2)))
        comb_cf = round(ans, 6)
        print(f"{cf1=}, {cf2=}, {comb_cf=}")
        return comb_cf


if __name__ == "__main__":
    progname = "CF Solver"
    desc = "This program able to solve CF problems. Single or Combination CF."
    parser = argparse.ArgumentParser(prog=progname, description=desc)

    parser.add_argument(
        "h_value", metavar="H", type=float, nargs="?", help="Hypothesis value"
    )
    parser.add_argument(
        "e_values",
        metavar="E",
        type=str,
        nargs="?",
        default="1.0",
        help="A string of cf(E) and their relationship. Use '&' to show AND and use '|' to show OR. If none given. default will be a single 1.0.",
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Get input from external file instead. Recommended for Combined CF Question.",
    )
    parser.add_argument(
        "-d",
        "--delimeter",
        help="Specify the delimeter used to seperate cf(H) and cf(E) from given file. Default is ';'",
        default=";",
    )

    solver = Solver()
    args = vars(parser.parse_args())
    if args["file"]:
        with open(args["file"], "r") as f:
            lines = f.read().splitlines()
        for line in lines:
            if line == "":
                continue
            h, e = line.replace(" ", "").split(args["delimeter"])
            new_cf = CF.from_string(h, e)
            solver.add_cf(new_cf)
        r = solver.solve_cf()
        print(f"Ans={r}")
    else:
        new_cf = CF.from_string(args["h_value"], args["e_values"])
        print(new_cf)
