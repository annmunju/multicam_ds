class Calc:

    @staticmethod # self 지워버림
    def add(a, b):
        return a+b

    def mul(self, a, b):
        return a*b

calc1 = Calc()
calc2 = Calc()
print(calc1.add(3,2))
print(Calc().mul(3,2))
print(Calc.add(3,2))

