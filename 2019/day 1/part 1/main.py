f = open("2019\\day 1\\input.txt", "r")

lines = f.read().splitlines()

#lines = [12, 14, 1969, 100756]

answer = 0

for l in lines:
    l = int(l)
    l = l / 3
    l = int(l)
    l = l - 2
    answer = answer + l

print(answer)