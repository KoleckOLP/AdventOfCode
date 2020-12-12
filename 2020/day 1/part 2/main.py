f = open("2020\day 1\input.txt", "r") #(kali)

lines = f.readlines()

numbers = []

for line in lines:
    numbers = numbers+[int(line[:-1])]

for numb1 in numbers:
    for numb2 in numbers:
        wanted = 2020 - (numb1 + numb2)
        if wanted in numbers:
            test = numb1 + numb2 + wanted
            result = numb1 * numb2 * wanted
            print(f"{numb1}, {numb2}, {wanted}, {str(test)}, {str(result)}")
            exit()

f.close()