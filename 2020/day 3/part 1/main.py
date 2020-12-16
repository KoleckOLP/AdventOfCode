'''
f = open("2020\\day 3\\input.txt", "r")

lines = f.read().splitlines()

f2 = open("2020\\day 3\\input_processed.txt", "w")

for line in lines:
    for i in range(0,48):
        f2.write(line)
        #print(i)
    f2.write("\n")
f2.close

f.close
'''

f3 = open("2020\\day 3\\input_processed.txt", "r")

lines = f3.read().splitlines()

FTrees = 0
CHRow = 0
CHCol = 0

while(True):
    CHRow = CHRow + 1
    CHCol = CHCol + 3
    if lines[CHRow][CHCol] == "#":
        FTrees = FTrees + 1 
    print(FTrees)