inputFile = open('day1.txt')

allElfCalories = []
caloriesOnElf = 0
for line in inputFile.readlines():
    if line == "\n":
        print(f"new elf, previous one had: {caloriesOnElf}")
        allElfCalories.append(caloriesOnElf)
        caloriesOnElf = 0
        continue
    print(line.replace("\n", ""))
    caloriesOnElf = caloriesOnElf + int(line.replace("\n", ""))

allElfCalories.sort()
allElfCalories.reverse()
print("Total Calories: ", allElfCalories[0] + allElfCalories[1] + allElfCalories[2])