# def convert(number):
#     r = ""
#     if number % 3 == 0:
#         r += "Pling"
#     if number % 5 == 0:
#         r += "Plang"
#     if number % 7 == 0:
#         r += "Plong"
#     if not r:
#         return str(number)
#     return r
# ----------------------more DRY
# def convert(number):
#     drops = ""
#     rain = {3:"Pling",5:"Plang",7:"Plong"}
#     for n in rain:
#         if number % n == 0:
#             drops += rain[n]
#     return str(number) if not drops else drops
#------------------------ more DRY
# RAIN = {3:"Pling", 5:"Plang", 7:"Plong"}

# def convert(number):
#     drops = ""
#     for key, value in RAIN.items():
#         if number % key == 0:
#             drops = "".join([drops, value])
#     return drops or str(number)

# x = convert(105)
# print(x)

FACTORS = {3:"Pling", 5:"Plang", 7:"Plong"} 

def convert(number): 

    list = [value for key, value in FACTORS.items() if number % key == 0]
    drops = "".join(list)
    
    return drops or str(number) 

print(convert(52))