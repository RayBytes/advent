input = open('day2.txt')

paper = 2
rock = 1
scissors = 3
score = 0
for line in input.readlines():
    l = line.split()
    print(l, f"{l[0]} and {l[1]}")
    if l[1] == "Y":
        score += paper
    if l[1] == "Z":
        score += scissors
    if l[1] == "X":
        score += rock
    if l[0] == "A":
        if l[1] == "X":
            print('tie')
            score += 3
        if l[1] == "Y":
            print('win')
            score += 6
    if l[0] == 'B':
        if l[1] == 'Y':
            print('tie')
            score += 3
        if l[1] == 'Z':
            print('win')
            score += 6
    if l[0] == "C":
        if l[1] == 'Z':
            print('tie')
            score += 3
        if l[1] == "X":
            print('win')
            score += 6
print(score)