f = open("2020\day 2\input.txt", "r")

lines = f.readlines()

split = []

for line in lines:
    split = split+[line.split(" ")]

prepared = []
true = 0

#print(len(split))

for list in split:
    numb = list[0].split("-")
    letter = list[1][:-1]
    line = list[2][:-1]
    occ = line.count(letter)
    if occ >= int(numb[0]):
        if occ <= int(numb[1]):
            true = true + 1

    print(numb[0]+", "+numb[1]+", "+letter+", "+line+", "+str(occ)+", "+str(true))

f.close