def is_isogram(phrase):
    cleaned_phrase = phrase.lower().replace("-", "").replace(" ", "")

    for i in range(len(cleaned_phrase)):
        for j in range(i + 1, len(cleaned_phrase)):
            if cleaned_phrase[i] == cleaned_phrase[j]:
                return False
    return True