
f = open("2020\\day 3\\input.txt", "r")

lines = f.read().splitlines()

f2 = open("2020\\day 3\\input_processed.txt", "w")

for line in lines:
    for i in range(0,500):
        f2.write(line)
        #print(i)
    f2.write("\n")
f2.close

f.close


FTrees = 0

def road(col=0, row=0, var=FTrees):
    f3 = open("2020\\day 3\\input_processed.txt", "r")

    lines = f3.read().splitlines()
    CHRow = 0
    CHCol = 0
    done = 1
    while(done):
        CHRow = CHRow + row
        CHCol = CHCol + col
        try:
            if lines[CHRow][CHCol] == "#":
                var = var + 1
        except IndexError:
            done = 0
            print(var)
            print("done")
    f3.close
    return var

FTrees11 = 0
FTrees11 = road(1, 1, FTrees11)
FTrees31 = 0
FTrees31 = road(3, 1, FTrees31)
FTrees51 = 0
FTrees51 = road(5, 1, FTrees51)
FTrees71 = 0
FTrees71 = road(7, 1, FTrees71)
FTrees12 = 0
FTrees12 = road(1, 2, FTrees12)



print(f"{FTrees11}, {FTrees31}, {FTrees51}, {FTrees71}, {FTrees12}")
FTrees = FTrees11 * FTrees31 * FTrees51 * FTrees71 * FTrees12
print(FTrees)