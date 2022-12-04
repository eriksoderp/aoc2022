points = {'X':1, 'Y':2, 'Z':3}
s = "AXBYCZ"
def main():    
    total_a = 0
    total_b = 0
    with open("input02.txt") as f:
        for line in f.readlines():
            total_a += get_points_a(line)
            total_b += get_points_b(line)
        
    print("Part a:", total_a)
    print("Part b:", total_b)

def get_points_a(line, diff = 22):
    opp, elf = line.split(' ')
    elf = elf.strip()
    res = (ord(elf) - ord(opp) + diff) % 3
    if res == 0:
        return (3 + points[elf])
    elif res == 1:
        return (6 + points[elf])
    elif res == 2:
        return points[elf]

def get_points_b(line):
    opp, elf = line.split(' ')
    elf = elf.strip()
    if elf == 'X':
        return points[s[(s.find(opp) - 1) % 6]]
    elif elf == 'Y':
        return (3 + points[s[s.find(opp) + 1]])
    elif elf == 'Z':
        return (6 + points[s[(s.find(opp) + 3) % 6]])

if __name__ == "__main__":
    main()
