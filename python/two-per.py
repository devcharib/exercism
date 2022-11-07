def two_fer(name=None):
    # if name:
    #     return f"One for {name[0]}, one for me."
    # else:
    #     return "One for you, one for me"
    #return "One for {0}, one for me.".format(name[0]) if name else "One for you, one for me"
    return "One for {0}, one for me.".format(name if name else "you")
x = two_fer("teste")
print(x)