def is_isogram(phrase):
    cleaned_phrase = phrase.lower().replace("-", "").replace(" ", "")
    return len(cleaned_phrase) == len(set(cleaned_phrase))