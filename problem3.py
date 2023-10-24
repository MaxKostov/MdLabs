def main():
    try:
        num = int(input("Input your number: "))
        num = str(num)
        print(smallestint(num))
    except ValueError:
        print("It is not intefer")


def smallestint(num):
    l_num = list(num)

    i = len(l_num) - 2
    while (i >= 0 and l_num[i] <= l_num[i+1]):
        i -= 1
    
    if (i == -1):
        return num
    
    j = len(l_num)-1
    while (l_num[j] >= l_num[i]):
        j -= 1
    
    l_num[i], l_num[j] = l_num[j], l_num[i]

    l_num[i+1:] = reversed(l_num[i+1:])
    
    comp_number = ""
    for it in l_num:
        comp_number += str(it)

    result = int(comp_number)

    return result

main()