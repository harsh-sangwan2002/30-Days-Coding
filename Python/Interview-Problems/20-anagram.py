st1 = "abc"; str2 = "bca"

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram(st1, str2))