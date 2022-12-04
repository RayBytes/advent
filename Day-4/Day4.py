input = open('day4.txt')
total = 0
for line in input.readlines():
    line = line.split('\n')
    line = line[0].split(',')
    # First section
    data = line[0].split('-')
    first_section = [ ]
    for num in range(int(data[0]), int(data[1]) + 1):
        first_section.append(num)
    data = line[1].split('-')
    second_section = [ ]
    for num in range(int(data[0]), int(data[1]) + 1):
        second_section.append(num)


    if set(first_section).issubset(set(second_section)) or set(second_section).issubset(set(first_section)) == True:
        total += 1

print('Total:', total)