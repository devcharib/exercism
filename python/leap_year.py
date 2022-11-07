# def leap_year(year):
#     """
#     """
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                     return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# x = leap_year(int(input()))
# print(x)

""" Return True or False if year is a leap year.""" #mentor IsaacG
def leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0:
        if year % 400 != 0:
            return False    
    return True

x = leap_year(int(input()))
print(x)