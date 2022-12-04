
def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2

input = open('day3.txt')
priorities = 0
charas1 = [ ]
charas2 = [ ]
charas3 = [ ]
count = 0
for line in input.readlines():
    count += 1
    if count == 1:
        for chara in line:
            charas1.append(chara)
    if count == 2:
        for chara in line:
            charas2.append(chara)
    if count == 3:
        for chara in line:
            charas3.append(chara)
    if count == 3:
        new_list = charas1.remove('\n')
        comparison = set(charas1) & set(charas2) & set(charas3)
        m_list = list(comparison)
        comparison = m_list[0]
        if comparison.upper() != comparison:
            priority = ord(comparison) - 96
        else:
            priority = ord(comparison) - 38
        priorities += priority
        count = 0
        charas1 = [ ]
        charas2 = [ ]
        charas3 = [ ]
        
print(priorities)