VOWEL = ("a","e","i","o","u","xr","yt","w")
TRAT = lambda t: t.removeprefix(t[:1])
WORD = lambda w: TRAT(w) + w[:1]

def translate(text):
    word = []
    list = text.split()
    for item in list:
        word.append(result(item))
    if len(word) > 1:
        return " ".join(word)
    return "".join(word)

def result(text):
    if text.startswith(VOWEL) : # rule 1
        return text + "ay"

    if "qu" in text: # rule 3
        while text[-1] != "u":
            text = WORD(text)
        return text + "ay"

    if text[2:3] == "y" or text[1:2] == "y": # rule 4
        while text[:1] != "y":
            text = WORD(text)
        return text + "ay"

    while text[:1] not in ("a","e","i","o","u"): # rule 2
        text = WORD(text)
    return text + "ay"


x = translate("")
print(x)
