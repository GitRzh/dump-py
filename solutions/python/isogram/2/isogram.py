def is_isogram(phrase):
    cleaned_phrase = phrase.lower().replace("-", "").replace(" ", "")

    for index, letter in enumerate(cleaned_phrase):
        for other_letter in cleaned_phrase[index + 1:]:
            if letter == other_letter:
                return False
    return True