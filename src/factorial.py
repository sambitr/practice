def fact(num):
    if isinstance(num, int) and num >= 0:
        if num == 0 or num == 1:
            return 1
        else:
            return num * fact(num - 1)
    else:
        return "Invalid Input"