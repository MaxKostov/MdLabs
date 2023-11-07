def main():

    ss = ["true", "false", "1", "0"]

    while True:
        try:
            a = input("Input a: ").lower()
            b = input("Input b: ").lower()
            if (a not in ss or b not in ss):
                print("Incorrect input")
            else:
                break;
        except ValueError:
            print("Incorrect input")

    
    if (a in ["true", "1"]):
        f1 = 1
    else:
        f1 = 0

    if (b in ["true", "1"]):
        f2 = 1
    else:
        f2 = 0

    if (f1 != f2):
        print("False")
    else:
        print("True")

main()