#Napisac program ktory wypisze podane liczby posortowane malejace i bez powtorzen.

def main():
    numbers = []
    numbers_ok = []
    while True:
        number = input("Podaj liczbe: ")
        if number == "koniec":
            break
        else:
            numbers.append(int(number))
    numbers = set(numbers)
    #numbers.sort(reverse=True)
    for i in sorted(numbers, reverse=True):
        numbers_ok.append(i)
    print(numbers_ok)

if __name__ == '__main__':
    main()