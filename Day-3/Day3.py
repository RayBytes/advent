
def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2

input = open('day3.txt')
priorities = 0
for line in input.readlines():
    first_compartment, second_compartment = splitstring(line)
    first = [ ]
    for chara in first_compartment:
        first.append(chara)
    second = [ ]
    for chara in second_compartment:
        second.append(chara)
    comparison = set(first) & set(second)
    comparison = list(comparison)
    if comparison.upper() != comparison:
        priority = ord(comparison) - 96
    else:
        priority = ord(comparison) - 38
    priorities += priority
print(priorities)