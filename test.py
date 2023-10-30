pat = ["#"]
pat = [x+x+x+x+x for x in pat] +\
      [x+x.replace("#", "*")+x+x.replace("#", "*")+x for x in pat] +\
      [x+x+x+x+x for x in pat]
print(pat)

pat = [x+x+x+x+x for x in pat] +\
      [x+x.replace("#", "*")+x+x.replace("#", "*")+x for x in pat] +\
      [x+x+x+x+x for x in pat]
print(pat)