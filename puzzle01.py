def main():    
    i = 0
    sums = []
    currSum = 0
    with open("input01.txt") as f:
        for line in f.readlines():
            if line == "\n":
                sums.append(currSum)
                i += 1
                currSum = 0
            else:
                currSum += int(line[:-1])

    sums.sort()
    print("Part a:", sums[-1])
    print("Part b:", sum(sums[-3:]))

if __name__ == "__main__":
    main()
