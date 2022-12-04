input = open('day2.txt')

paper = 2
rock = 1
scissors = 3
score = 0
for line in input.readlines():
    l = line.split()
    print(l, f"{l[0]} and {l[1]}")
    if l[0] == 'A':
        if l[1] == 'Y':
            # Need to TIE
            # Rock
            score += rock
            score += 3
        if l[1] == 'X':
            # Need to LOSE
            # Scissors
            score += scissors
            score += 0
        if l[1] == 'Z':
            # Need to WIN
            # Paper
            score += paper
            score += 6
    if l[0] == 'B':
        if l[1] == 'X':
            # Need to LOSE
            # Rock
            score += rock
            score += 0
        if l[1] == 'Z':
            # Need to WIN
            # Scissors
            score += scissors
            score += 6
        if l[1] == 'Y':
            # Need to TIE
            # Paper
            score += paper
            score += 3
    if l[0] == 'C':
        if l[1] == 'Z':
            # Need to WIN
            # Rock
            score += rock
            score += 6
        if l[1] == 'X':
            # Need to LOSE
            # Paper
            score += paper
            score += 0
        if l[1] == 'Y':
            # Need to TIE
            # Paper
            score += scissors
            score += 3
print(score)