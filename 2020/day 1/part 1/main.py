f = open("2020\day 1\input.txt", "r") #(kali)

lines = f.readlines()

for line in lines:
    wanted = 2020 - int(line[:-1])
    wanted = str(wanted)+"\n"
    if wanted in lines:
        test = int(line[:-1]) + int(wanted[:-1])
        result = int(line[:-1]) * int(wanted[:-1])
        print(f"{line[:-1]}, {wanted[:-1]}, {str(test)}, {str(result)}")
        exit()
    print(line[:-1])

f.close()