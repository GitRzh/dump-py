def steps(number):
    if 0 >= number:
        raise ValueError("Only positive integers are allowed")
        
    temp = number
    count = 0

    while temp != 1:
        if temp % 2 == 0:
            temp = temp // 2
        else:
            temp = 3 * temp + 1
        count += 1

    return count