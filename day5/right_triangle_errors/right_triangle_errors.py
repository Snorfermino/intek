def right_triangle_errors(a, b, c):
    try:
        if isinstance(a,int) or isinstance(b, int) or isinstance(c, int):
            raise ValueError('Incorrect value')
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Incorrect value')
        if a ** 2 == (b ** 2 + c ** 2):
            return True
        else:
            return False
    except ValueError:
        print(ValueError('Incorrect value'))
