# Press the green button in the gutter to run the script.
import math


class QuadraticSolver:
    a, b, c = 0, 0, 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        discriminant = (self.b ** 2) - (4 * self.a * self.c)
        x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
        x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
        return {
            "x1": x1,
            "x2": x2
        }
