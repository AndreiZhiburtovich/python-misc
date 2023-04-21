# DESCRIPTION:
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false


# def xo(s):
#     s = s.lower()
#     x_count = 0
#     o_count = 0
#     for char in s:
#         if char == "x":
#             x_count += 1
#         elif char == "o":
#             o_count += 1
#     return x_count == o_count


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo('xo')) # 'True expected'
print(xo('xo0')) # 'True expected'
print(xo('xxxoo')) # 'False expected'
print(xo('')) # 'True expected'
print(xo('zzoo')) # 'False expected'
