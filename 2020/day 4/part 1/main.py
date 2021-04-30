#f = open("2020\\day 4\\part 1\\test.txt", "r") # test from the page
# had to add new line after the last batch to make it detect xDD
f = open("2020\\day 4\\input.txt", "r")

lines = f.readlines()

#print(lines)

batch = []
valid = 0
check = 0

for l in lines:
    batch = batch+[l] 
    
    if l == "\n":
        print(batch)
        for k in batch:
            if "byr:" in k:
                check=check+1
            if "iyr:" in k:
                check=check+1
            if "eyr:" in k:
                check=check+1
            if "hgt:" in k:
                check=check+1
            if "hcl:" in k:
                check=check+1
            if "ecl:" in k:
                check=check+1
            if "pid:" in k:
                check=check+1
        print(check)
        if check == 7:
            valid=valid+1
        batch = []
        check = 0

print(valid)