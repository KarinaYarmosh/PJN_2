#W kolejnych wierszach dane są informacje na temat samochodów (marka, model,prędkość maksymalna).
# Napisać program, który wypisze prędkość najszybszego samochodu.

def main():
    cars = []
    while True:
        car = input("Podaj dane samochodu: ")
        if car == "koniec":
            break
        else:
            cars.append(car)
    cars.sort(reverse=False)
    print(cars[0])

if __name__ == '__main__':
    main()