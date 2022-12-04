def main():
    total_a = 0 
    total_b = 0
    with open("input04.txt") as f:
        for line in f.readlines():
            a, b = line.split(',')
            a1, a2 = a.split('-')
            b1, b2 = b.split('-')
            a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
            if is_contained(a1, a2, b1, b2):
                total_a += 1
            if is_overlapping(a1, a2, b1, b2):
                total_b += 1
            
    print("Part a:", total_a)
    print("Part b:", total_b)

def is_contained(a1, a2, b1, b2):
    if a1 <= b1 and b2 <= a2:
        return True
    
    if b1 <= a1 and a2 <= b2:
        return True
            
    return False

def is_overlapping(a1, a2, b1, b2):
    if a1 <= b1 and b1 <= a2 or a1 <= b2 and b2 <= a2 or is_contained(a1, a2, b1, b2):
        return True

    return False


if __name__ == "__main__":
    main()
