pat = ["#"]
pat = [x+x for x in pat] +\
      [x+x.replace("#", "*") for x in pat]
print(pat)

pat = [x+x for x in pat] +\
      [x+x.replace("#", "*") for x in pat]
print(pat)