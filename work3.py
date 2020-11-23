class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        try:
            res = self.count - other.count
            if res > 0:
                return Cell(res)
            else:
                raise ValueError
        except ValueError:
            return "Не возможно вычесть клетки"

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, count):
        star = "*" * count + "\n"
        end = "*" * (self.count - count * (self.count // count))
        return star * (self.count // count) + end


cell1 = Cell(21)
cell2 = Cell(112)
print(cell1.make_order(9))
print("_"*10)
cell3 = cell2 - cell1
print(cell3.make_order(10))
