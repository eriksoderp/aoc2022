import string

def main():
    priorities = {}
    for c, n in zip(list(string.ascii_letters), range(1, 53)):
        priorities[c] = n

    total_a = 0
    total_b = 0
    with open("input03.txt") as f:
        lines = f.readlines()
        for line in lines:
            total_a += priorities[find_dup(line)]

        for triple in chunker(lines, 3):
            l1, l2, l3 = triple[0], triple[1], triple[2]
            total_b += priorities[find_triple(l1, l2, l3)]
            
    print("Part a:", total_a)
    print("Part b:", total_b)

def find_dup(line):
    a, b = line[:len(line)//2], line[len(line)//2:]
    letters_in_a = {}
    for c in a:
        letters_in_a[c] = True

    for c in b:
        if c in letters_in_a:
            return c

def find_triple(line1, line2, line3):
    letters_in_first = {}
    for c in line1:
        letters_in_first[c] = False

    for c in line2:
        if c in letters_in_first:
            letters_in_first[c] = True

    for c in line3:
        if c in letters_in_first and letters_in_first[c]:
            return c
    
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

if __name__ == "__main__":
    main()