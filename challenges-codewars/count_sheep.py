# DESCRIPTION:
# If you can't sleep, just count sheep!!
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
# Input will always be valid, i.e. no negative integers.


# def count_sheep(n):
#     result = ""
#     for i in range(1, n + 1):
#         result += f"{i} sheep..."
#     return result


def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))


def assert_equals(a, b):
    print(a == b)


assert_equals(count_sheep(0), "");
assert_equals(count_sheep(1), "1 sheep...");
assert_equals(count_sheep(2), "1 sheep...2 sheep...")
assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")
