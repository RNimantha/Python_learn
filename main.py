class MyClass:
    def __init__(self):
        print("Object created")

    def method1(self):
        print("Method 1 executed")

    def method2(self):
        print("Method 2 executed")


def main():
    obj = MyClass()
    obj.method1()
    obj.method2()


if __name__ == "__main__":
    main()