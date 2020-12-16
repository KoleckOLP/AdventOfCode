f = open("2020\\day 2\\input.txt", "r")

lines = f.readlines()

split = []

for line in lines:
    split = split+[line.split(" ")]

prepared = []
true = 0

listt = []

#print(len(split))

for list in split:
    numb = list[0].split("-")  #mumb[0], numb[1]
    numb[0] = int(numb[0])-1
    numb[1] = int(numb[1])-1
    letter = list[1][:-1] #the letter we are looking for
    line = list[2][:-1] #the actuall list
    listt = [None, None]
    try:
        if line[numb[0]] == letter:
            listt[0] = True
        else:
            listt[0] = False
    except IndexError:
        listt[0] = False

    try:
        if line[numb[1]] == letter:
            listt[1] = True
        else:
            listt[1] = False
    except IndexError:
        listt[1] = False

    if listt[0] == listt[1]:
        pass
    else:
        true = true + 1

    print(str(numb[0]+1)+", "+str(numb[1]+1)+", "+letter+", "+line+", "+str(listt)+", "+str(true))
f.close