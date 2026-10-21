def rotate(text, key):
    plain = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.lower() in plain:
            new_char = plain[(plain.index(char.lower()) + key) % 26]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char

    return result