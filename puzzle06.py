def main():
    with open("input06.txt") as f:
        l = f.read()
        a = False
        b = False
        
        for i, _ in enumerate(l):
            if not a:
                if len(set(l[i:i-4:-1])) == 4:
                    print("Part a:", i+1)
                    a = True

            if not b:
                if len(set(l[i:i-14:-1])) == 14:
                    print("Part b:", i+1)
                    b = True
            
            if a and b: break

if __name__=="__main__":
    main()
