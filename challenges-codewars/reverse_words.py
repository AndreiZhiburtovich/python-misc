# DESCRIPTION:
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_words(text):
    words = text.split(" ")
    reversed_words = []
    for i in words:
        reversed_words.append(i[::-1])
    return " ".join(reversed_words)


def assert_equals(a, b):
    print(a == b)


assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
assert_equals(reverse_words('apple'), 'elppa')
assert_equals(reverse_words('a b c d'), 'a b c d')
assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')
