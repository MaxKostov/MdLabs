def shortest_palindrome(s):
    rev_s = s[::-1]
    new_str = s + rev_s

    kmp_table = [0] * len(new_str)
    j = 0
    for i in range(1, len(new_str)):
        while j > 0 and new_str[i] != new_str[j]:
            j = kmp_table[j - 1]
        if new_str[i] == new_str[j]:
            j += 1
        kmp_table[i] = j

    remaining = rev_s[:-kmp_table[-1]]

    return remaining + s


input_str = input("str = ")
result = shortest_palindrome(input_str)
print(result)
