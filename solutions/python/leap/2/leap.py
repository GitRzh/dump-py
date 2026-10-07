def leap_year(year):
    """
    Return True if the year is a leap year,
    Logic (in plain eng.):
    - If divisible by 4: True
    - If also divisible by 100: False
    - If also divisible by 400: True
    - Otherwise: False.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
#    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)