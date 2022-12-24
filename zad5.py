#Napisać program, który policzy sumaryczną ilość dwuznaków "cz" i "sz" na wejściu.

def main():
    count = 0
    while True:
        word = input("Podaj slowo: ")
        if word == "koniec":
            break
        else:
            count += word.count("cz")
            count += word.count("sz")
    print(count)

if __name__ == '__main__':
    main()