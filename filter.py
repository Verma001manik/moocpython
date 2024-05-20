def filter_forbidden(string: str, forbidden: str):
    r  = [character for character in string if character not in forbidden]
    return ''.join(r)
sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)
