class Calculator:
    def multiply(self, *args):
        if len(args) == 2:
            return args[0] * args[1]
        elif len(args) == 3:
            return args[0] * args[1] * args[2]
        else:
            raise ValueError("multiply method accepts only 2 or 3 arguments")

calc = Calculator()
numbers = list(map(int, input("Enter two or three numbers separated by spaces: ").split()))
print(calc.multiply(*numbers))
