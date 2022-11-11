def response(hey_bob):
    #hey_bob = hey_bob.replace(",", "")
    #hey_bob = hey_bob.replace(" ", "")
    hey_bob = hey_bob.strip()
    #if len(hey_bob) == 0:#
    if not hey_bob or hey_bob.isspace(): #mentored by IsaacG https://docs.python.org/3/library/stdtypes.html#string-methods
        return "Fine. Be that way!"
    #if hey_bob[-1] == "?":#
    if hey_bob.endswith("?"):#mentored by IsaacG
        #hey_bob = hey_bob.replace("?", "")
        #if hey_bob != hey_bob.isupper() or hey_bob.isnumeric():#
        if not hey_bob.isupper():# or hey_bob.isnumeric():#mentored by IsaacG
            return "Sure."
        #if hey_bob.islower() and hey_bob.isupper():#mentored by IsaacG
        #    return "Sure."
        #if hey_bob[1:] != hey_bob[1:].lower():#
        #if hey_bob.isupper():#mentored by IsaacG
        return "Calm down, I know what I'm doing!"
    #if hey_bob == hey_bob.upper() and not hey_bob.isnumeric():#
    if hey_bob.isupper():# and not hey_bob.isnumeric():#
        return "Whoa, chill out!"
    return "Whatever."

    #####
    # def response(hey_bob):
    # hey_bob = hey_bob.strip()#mentored by IssacG
    # if not hey_bob: #mentored by IsaacG
    #     return "Fine. Be that way!"
    # if hey_bob.endswith("?"):#mentored by IsaacG
    #     if not hey_bob.isupper():#mentored by IsaacG
    #         return "Sure."
    #     if hey_bob.isupper():#mentored by IsaacG
    #         return "Calm down, I know what I'm doing!"
    # if hey_bob.isupper():#mentored by IsaacG
    #     return "Whoa, chill out!"
    # return "Whatever."

    ########
    # def response(hey_bob):
    # hey_bob = hey_bob.strip()#mentored by IssacG
    # if not hey_bob: #mentored by IsaacG
    #     return "Fine. Be that way!"
    # if hey_bob.endswith("?"):#mentored by IsaacG
    #     if hey_bob.isupper():#mentored by IsaacG
    #         return "Calm down, I know what I'm doing!" #mentored by IsaacG
    #     return "Sure." #mentored by IsaacG
    # if hey_bob.isupper():#mentored by IsaacG
    #     return "Whoa, chill out!"
    # return "Whatever."

x = response("1, 2, 3?")
print(x)