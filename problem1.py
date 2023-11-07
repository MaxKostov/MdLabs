
result = []

def main():
    elem = []
    arr = []
    s = input("set: ")
    if (s[0] != '[' or s[len(s)-1] != ']'):
        return
    for i in range(1, len(s)-1):
        if (s[i] == ','):
            continue
        elem.append(s[i])
        if (s[i+1] == ',' or i+2 == len(s)):
            arr.append(''.join(elem))
            elem = []


    print(arr)
    print("")
    for i in powerset(arr):
        result.append(i)
    result.reverse()
    print(result)

def powerset(el):
    if len(el) <= 1:
        yield el
        yield []
    else:
        for i in powerset(el[1:]):
            gg = [el[0]] + i
            yield gg
            yield i
        

def sset(strng):
    arr = []
    elem = []
    if (strng[0] != '[' or strng[len(strng)-1] != ']'):
        return
    for i in range(1, len(strng)-1):
        if (strng[i] == ','):
            continue
        elem.append(s[i])
        if (strng[i+1] == ',' or i+2 == len(strng)):
            arr.append(''.join(elem))
            elem = []


main()