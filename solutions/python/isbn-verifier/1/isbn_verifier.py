def is_valid(isbn):
    isbn = isbn.replace("-","")

    if len(isbn) != 10:
        return False

    d = []
    for i in range(10):
        c = isbn[i]
        if c.isdigit():
            d.append(int(c))
        elif c == "X" and i == 9:
            d.append(10)
        else:
            return False

    return (d[0]*10 + d[1]*9 + d[2]*8 + d[3]*7 + d[4]*6 + d[5]*5 + d[6]*4 + d[7]*3 + d[8]*2 + d[9]*1) % 11 == 0         