from numeral import negativeNum, positiveNum
from solver.QuadraticSolver import QuadraticSolver


def numsTest():
    num = int(input())
    if num < 0:
        num = negativeNum.negativeNum(num)
    elif num > 0:
        num = positiveNum.positiveNum(num)
    print(num.num)


def solveEquation():
    a = int(input("a"))
    b = int(input("b"))
    c = int(input("c"))
    solver = QuadraticSolver(a, b, c)
    print(solver.solve())


if __name__ == '__main__':
    solveEquation()
