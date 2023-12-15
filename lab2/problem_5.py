def main():
    code = "OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM"
    coinsides = []
    letter = {}
    code_length = len(code)

    for i in range(len(code)):
        sub_str = code[:-(i+1)]
        sub_str_length = len(sub_str)
        subc = 0
        for j in range(sub_str_length):
            a = sub_str[j]
            b = code[(code_length - sub_str_length) + j]
            if a == b:
                subc += 1
                if a in letter.keys():
                    letter[a] += 1
                else:
                    letter[a] = 1
        coinsides.append(subc)

    print(coinsides)
    print(letter)

if __name__ == '__main__':
    main()