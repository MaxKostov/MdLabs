def main():
    num = int(input("Enter the number: "))
    serpcarp(num)

def serpcarp(n):
    pat = ['#']
    for i in range(n):
        pat = [x+x+x+x+x for x in pat] +\
        [x+x.replace("#", " ")+x+x.replace("#", " ")+x for x in pat] +\
        [x+x+x+x+x for x in pat]
    print("\n".join(pat))
main()