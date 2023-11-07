import random

def main():
    array_length = 200
    random_array = [random.randint(0, 1) for i in range(array_length)]
    starsandhashes = ["#" if x == 1 else " " for x in random_array]
    randstring = ''.join(starsandhashes)
    print(randstring)
    
    for iterations in range(100):
        newgen = [0]

        for x in range(0, len(random_array)-2):
            if (random_array[x:x+3] in [[1,1, 1], [1, 0, 0], [0, 0, 0]]):
                newgen.append(0)
            else:
                newgen.append(1)
        newgen.append(0)


        newstarsandhashes = ["#" if x == 1 else " " for x in newgen]

        newstr = ''.join(newstarsandhashes)
        print(newstr)
        random_array = newgen
        

main()