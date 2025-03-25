def testing_for_exception():
    numerator = 10
    denominator = 0
    try:
        devision(numerator, denominator)
        assert(False)
    except ArithmeticError:
        assert(True)
    except ZeroDivisionError:
        assert(False)
testing_for_exception()