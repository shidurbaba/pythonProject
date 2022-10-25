class Calculator:
    num1 = 100

    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print('From parent constructor')

    def Summation(self):
        return self.firstNum + self.secondNum + Calculator.num1


obj = Calculator(1, 2)

print(obj.Summation())
