class Beverage :
    def __init__(self, name, price) :
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

class Cocktail(Beverage):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_alcohol(self):
        return self.__alcohol

    def __str__(self):
        return "{} at {}" .format(self.get_name(),self.get_price())

class Mocktail(Beverage):
    def __init__(self, name, price):
        super().__init__(name, price)

    def __str__(self):
        return "{} at {}".format(self.get_name(), self.get_price())


class Bar():
    beverages = []
    orders = []

    def __init__(self):
        self.create_beverages()

    def add_beverage(self, beverage):
        self.__class__.beverages.append(beverage)

    def add_order(self, order):
        self.__class__.orders.append(order)

    def create_beverages(self):
        c1 = Cocktail('4. Cough Medicine', 30)
        self.add_beverage(c1)
        c2 = Cocktail('3. Flu Medicine', 50)
        self.add_beverage(c2)
        b1 = Mocktail('1. Fever Medicine', 100)
        self.add_beverage(b1)


    def show_menu(self):
        c1 = Cocktail(' Cough Medicine', 30)
        c2 = Cocktail(' Flu Medicine',  50)
        b1 = Mocktail(' Fever Medicine', 100)
        while True:
            print('1 Cough Medicine at $30')
            print('2 Flu Medicine at $50')
            print('3 Fever Medicine at $100')
            print('0 Quit program')
            choice = input('Enter your choice (0,1,2,3): ')
            if choice == '0':
                break
            if choice == '1':
                self.add_order(c1)
            if choice == '2':
                self.add_order(c2)
            if choice == '3':
                self.add_order(b1)


    def display_orders(self):
        print("The orders are")
        cost = 0
        for i in self.orders:
            print(i)
            cost += i.get_price()
        print("The total amount is ${:.2f}".format(cost))

bar = Bar()
bar.show_menu()
bar.display_orders()



# medicine = Medicine()
# name = input("Enter name of medicine : ")
# amt = int(input("Enter amount of medicine : "))
#
# medicine.set_item(name)
# medicine.set_quantity(amt)
#
#
# def __str__(self):
#     return"You have purchased {} of {}".format(self.__get_quantity, self.__get_items)
#
#
#
#
# print("You have purchase %d of %s" %(medicine.get_quantity(), medicine.get_item()))


# def processOrder(quantity, item_list):
#     global total
#     if quantity > item_list[2]:
#         print("There is not enough stock!")
#         pass
#     else:
#         total += item_list[1] * quantity
#         item_list[2] -= quantity
#
# total = 0
# A = ["Cough Medicine", float(30), 50], ["Flu Medicine", float(130), 50], ["Fever Medicine", float(35), 50]
#
# print("Welcome to Medicine Purchase Page!")
# print("[1]", A[0][0:2],
#       "\n[2]", A[1][0:2],
#       "\n[3]", A[2][0:2])
#
# while True:
#     choice, quantity = (input("\nWhat would you like?\n")).upper(), int(input("\nHow many would you like?\n"))
#
#     if choice == "COUGH MEDICINE":
#         processOrder(quantity, A[0])
#     elif choice == "FLU MEDICINE":
#         processOrder(quantity, A[1])
#     elif choice == "FEVER MEDICINE":
#         processOrder(quantity, A[2])
#     else:
#         print("Invalid Item")
#
#     more_items = (input("Do you want to order more items?")).lower()
#     if more_items == "yes":
#         pass
#     else:
#         break
#
# print("Thank you for ordering!\nYour total cost is: £" +  str(total))
#
