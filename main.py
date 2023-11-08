from src.number_service import Numbers, GetNumbers

def main():
    numbers = Numbers()
    sum = numbers.add_two(3, 4)
    print(sum)

    multy = numbers.multi_two(23,45)
    print(multy)

    getnumbers = GetNumbers()
    num1 = getnumbers.getnum( 12, 34, 2)


if __name__ == "__main__":
    main()
    