#Wypisać sto dwudziestą trzecią linię wejścia.

import sys

def main():
    for i, line in enumerate(sys.stdin):
        if i == 12:
            print(line)

if __name__ == '__main__':
    main()