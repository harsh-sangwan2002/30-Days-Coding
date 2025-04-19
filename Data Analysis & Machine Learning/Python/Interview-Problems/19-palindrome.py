word = "racecar"
i = 0; j = len(word)-1

while i < j:
    if word[i] != word[j]:
        print("Not a palindrome")
        break
    i += 1
    j -= 1
else:
    print("Palindrome")