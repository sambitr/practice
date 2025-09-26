def evenOddNumber(number):
    if isinstance(number, int):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Invalid Input"