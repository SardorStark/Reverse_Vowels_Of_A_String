def reverse_vowels_of_a_string(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    l = []
    result = ''
    for v in s:
        if v in vowels:
            l.append(v)
    for v in s:
        if v in vowels:
            result += l.pop()
        else:
            result += v
    return result
