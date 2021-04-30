import re

f = open("2020\\day 4\\part 2\\test.txt", "r") # test from the page
# had to add new line after the last batch to make it detect xDD
#f = open("2020\\day 4\\input.txt", "r")

lines = f.readlines()

#print(lines)

batch = []
valid = 0
check = 0
fields = []

for l in lines:
    batch = batch+[l] 
    
    if l == "\n":
        #print(batch)
        for k in batch: # split to get individual fields
            temp = k.split(" ")
            fields = fields+temp
        print(fields)
        for j in fields:
            if "byr:" in j: # success checking byr
                byr = j.replace("byr:", "")
                byr = int(byr)
                if byr >= 1920 and byr <= 2002:
                    check=check+1
            if "iyr:" in j: # sucess checking iyr
                iyr = j.replace("iyr:", "")
                iyr = int(iyr)
                if iyr >= 2010 and iyr <= 2020:
                    check=check+1
            if "eyr:" in j:
                eyr = j.replace("eyr:", "")
                eyr = int(eyr)
                if eyr >= 2020 and eyr <= 2030:
                    check=check+1
            if "hgt:" in j: # sucess checking hgt
                if "cm" in j:
                    hgt = j.replace("hgt:", "")
                    hgt = hgt.replace("cm", "")
                    hgt = int(hgt)
                    if hgt >= 150 and hgt <= 193:
                        check=check+1
                elif "in" in j:
                    hgt = j.replace("hgt:", "")
                    hgt = hgt.replace("in", "")
                    hgt = int(hgt)
                    if hgt >= 59 and hgt <= 76:
                        check=check+1
            if "hcl:" in j: # Broo I used regex to get a sucess!!
                hcl = j.replace("hcl:", "")
                if re.match("^#[a-f0-9]{6}$", hcl):
                    check=check+1
            if "ecl:" in j:
                ecl = j.replace("ecl:", "")
                allowed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if ecl in allowed:
                    check=check+1
            if "pid:" in j:
                pid = j.replace("pid:", "")
                if re.match("^\d{9}$", pid):
                    check=check+1
        
        byr = None
        iyr = None
        eyr = None
        hgt = None
        hcl = None
        ecl = None
        pid = None
        print(check)
        if check == 7:
            valid=valid+1
        batch = []
        fields = []
        check = 0
print(valid)