#Napisać program, który ponumeruje linie wejścia a następnie wypisze je w odwrotnejkolejności.

def main():
    lines = []
    while True:
        line = input("Podaj linie: ")
        if line == "koniec":
            break
        else:
            lines.append(line)
    lines.reverse()
    for i, line in enumerate(lines):
        print(i, line)

if __name__ == '__main__':
    main()