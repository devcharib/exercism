
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

    #######
def response(hey_bob):
    hey_bob = hey_bob.strip()#mentored by IssacG
    if not hey_bob: #mentored by IsaacG
        return "Fine. Be that way!"
    if hey_bob.endswith("?"):#mentored by IsaacG
        if hey_bob.isupper():#mentored by IsaacG
            return "Calm down, I know what I'm doing!" #mentored by IsaacG
        return "Sure." #mentored by IsaacG
    if hey_bob.isupper():#mentored by IsaacG
        return "Whoa, chill out!"
    return "Whatever."

x = response("1, 2, 3?")
print(x)