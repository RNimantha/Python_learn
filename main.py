from src.number_service import Numbers, GetNumbers
from src.new_srvice import Random
from src.testclass import Bank
from src.dog_service import Dog
from src.car_service import Car
from src.inheritance import Perent , Child1, Child2

def main():
    # exercise car
    # bluecar = Car('blue' , 20000)
    # bluecar.cardetails()

    # exercise number service
    # numbers = Numbers()
    # sum = numbers.add_two(3, 4)
    # print(sum)

    # multy = numbers.multi_two(23,45)
    # print(multy)

    # exercise random service
    # random_number = Random().get_random()
    # print(random_number)

    # exercise bank account
    # owner = input('Please Enter Name of the Owner of account: ')
    # blance = float(input("Enter the balance amount: "))
    # amount = float(input("Enter the deposit amount: "))
    # bank = Bank(owner,blance)
    # output = bank.deposit(amount)
    # print(output)

    # exercise dog service
    # dog = Dog("Timmy", 6)
    # # tim = dog.bark()
    # print(dog)
    # print(dog.species)

    # exercise get numbers service
    # getnumbers = GetNumbers()
    # num1 = getnumbers.getnum(12, 34, 2)
    # print(num1)



    # text = input('Enter you text: ')
    # lentext = Random().newfun(text)
    # print(lentext)

    # inheritance Exercice
    c1 = Child1()
    c2 = Child2()
    print(f'chiled1 speaks ',c1.speaks)
    print(f'chiled2 speaks ',c2.speaks)

if __name__ == "__main__":
    main()
    