def main():
    f = open("input01.txt", "r")
    
    i = 0
    sums = []
    currSum = 0
    for line in f.readlines():
        if line == "\n":
            sums.append(currSum)
            i += 1
            currSum = 0
        else:
            currSum += int(line[:-1])

    sums.sort()
    print(sums[-1])
    print(sum(sums[-3:]))

if __name__ == "__main__":
    main()