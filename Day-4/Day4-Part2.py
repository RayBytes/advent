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
    # Second section
    data = line[1].split('-')
    second_section = [ ]
    for num in range(int(data[0]), int(data[1]) + 1):
        second_section.append(num)
    

    c = [ x for x in first_section if x in second_section ]
    ans = len(c) 
    if ans != 0:
        total += 1

print('Total:', total)