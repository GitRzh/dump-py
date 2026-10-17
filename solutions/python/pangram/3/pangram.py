# from string import ascii_lowercase

def is_pangram(sentence):
    lowercase = sentence.lower()
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabets:
        if letter not in lowercase:
            return False
    return True
    
    # return set(ascii_lowercase) <= set(sentence.lower())