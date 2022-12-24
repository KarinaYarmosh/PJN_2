#Wypisać linie od 10 do 20 włącznie (razem 11 linii).

import sys

def main():
    line2= []
    for i, line in enumerate(sys.stdin):
        while not i == 20:
            if i >= 9 and i <= 19:
                line2.append(line)
                break
            else:
                break
            #print(line)
    print(line2)
if __name__ == '__main__':
    main()