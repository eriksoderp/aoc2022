import re
import copy

def main():
    with open("input05.txt") as f:
        stacks, commands = f.read().split('\n\n')
        commands = commands.split('\n')
        stacks = stacks.split('\n')[::-1]

        l1 = [[] for _ in range(int(stacks[0][-2]))]

        for i, stack in enumerate(stacks):
            for j, c in enumerate(stack):
                if j % 4 == 1 and c.isalpha():
                    index, _ = divmod(j, 4)
                    l1[index].append(c)

        l2 = copy.deepcopy(l1)

        for c in commands:
            m, f, t = map(int, re.findall(r'\b\d+\b', c))

            for _ in range(m-1, -1, -1):
                e = l1[f-1].pop()
                l1[t-1].append(e)

            l2[t-1] = l2[t-1] + l2[f-1][-m:]
            l2[f-1] = l2[f-1][:-m]
        
        print("Part a:", ''.join([e[-1] for e in l1]))
        print("Part b:", ''.join([e[-1] for e in l2]))


if __name__=="__main__":
    main()

