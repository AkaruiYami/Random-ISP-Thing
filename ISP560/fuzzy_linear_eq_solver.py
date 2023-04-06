class LinerEQSolver:
    def __init__(self):
        pass

    def read_csv(self, filename, delimeter=",", header=None):
        with open(filename, "r") as file:
            data = file.read().splitlines()
        if header is None:
            header = data.pop(0).split(delimeter)
        self.variables = header
        
        try:
            self.X = [int(x.split(delimeter)[0]) for x in data]
        except ValueError:
            self.X = [float(x.split(delimeter)[0]) for x in data]

        str_vals = [line[line.find(delimeter)+1:] for line in data]
        str_vals = ",".join(str_vals)
        self.values = str_vals.split(",")

    def _get_values(self, header):
        n = len(self.variables) - 1
        i = self.variables.find(header) - 1
        return self.values[i:n]

    def _get_value(self, header, i):
        vals = self._get_values(header)
        return vals[i]

