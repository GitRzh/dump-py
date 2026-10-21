def rotate(s, key):
    plain = "abcdefghijklmnopqrstuvwxyz"
    trans = plain[key:] + plain[:key]
    plain += plain.upper(); trans += trans.upper()
    
    return s.translate(str.maketrans(plain, trans))