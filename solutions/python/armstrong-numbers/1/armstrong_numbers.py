def is_armstrong_number(number):
    length = len(str(number))
    total = 0
    for d in str(number):
        total += int(d) ** length

    return total == number