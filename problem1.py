
result = []

def main():
    s = input("set: ")

    arr = eval(s)

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
        


main()