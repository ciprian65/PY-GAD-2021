def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            temp = greater
            break
        greater += 1

    return temp


class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def get_numarator(self):
        return self.numarator

    def get_numitor(self):
        return self.numitor

    def set_numarator(self, numarator):
        self.numarator = numarator

    def set_numitor(self, numitor):
        self.numitor = numitor

    def __str__(self):
        return str(self.numarator) + "/" + str(self.numitor)

    def __add__(self, other):
        new_numitor = lcm(self.numitor, other.numitor)
        new_numarator = self.numarator * int(new_numitor / self.numitor) + other.numarator * int(new_numitor / other.numitor)
        return Fractie(new_numarator, new_numitor)

    def __sub__(self, other):
        new_numitor = lcm(self.numitor, other.numitor)
        new_numarator = self.numarator * int(new_numitor / self.numitor) - other.numarator * int(new_numitor / other.numitor)
        return Fractie(new_numarator, new_numitor)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


f1 = Fractie(1, 6)
f2 = Fractie(3, 4)

print(f1.__add__(f2))
print(f2.__sub__(f1))
print(f1.inverse())
print(f2.inverse())