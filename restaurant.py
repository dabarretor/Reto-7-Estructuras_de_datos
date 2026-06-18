"""This program allows us to create a restaurant with a menu of 10
(3 drinks, 3 main dishes, 2 desserts, and 2 additional dishes).
We take customer orders and apply discounts depending on the combo they order.
The program demonstrates the use of classes, composition, and inheritance in Python.
"""


class Restaurant:
    def __init__(self, name: str, size: str):
        self._name = name
        self._size = size

        # Composition: the restaurant is created with its own menu
        self.menu: list["MenuItem"] = []
        self.create_menu()  # We call a function to create the 10 items

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_size(self):
        return self._size

    def set_size(self, value):
        self._size = value

    def create_menu(self):
        # There are your 10 minimum items
        # 3 Drinks (type_drink, size, name, price)
        self.menu.append(Drinks("Gaseosa", "Mediana", "Coca-Cola", 2.50))
        self.menu.append(Drinks("Juice", "Big", "Natural lemonade", 3.0))
        self.menu.append(Drinks("Beer", "Small", "Corona", 4.0))

        # 3 Main Dishes (dish_type, dish_size, name, price)
        self.menu.append(PrincipalDishes("Fast food", "Double", "Hamburguer", 12.0))
        self.menu.append(PrincipalDishes("Spaghetti", "Personal", "Spaghetti", 10.0))
        self.menu.append(PrincipalDishes("Meat", "Family", "Chopped meat", 25.0))

        # 2 Desserts (dessert_type, portion_size, name, price)
        self.menu.append(Desserts("Cold", "1 scoop", "Ice Cream", 3.50))
        self.menu.append(Desserts("Hot", "1 portion", "Brownie", 4.50))

        # 2 AdditionalDishes (portion_size, name, price)
        self.menu.append(AdditionalDishes("for share", "French fries", 3.50))
        self.menu.append(AdditionalDishes("Personal", "salad", 2.25))


class MenuItem:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def __str__(self) -> str:
        return f"{self._name} (${self._price:.2f})"


class Order:
    def __init__(self, name: str):
        # allows us to identify the order, for example,
        # if it's for a specific table or a takeout order.
        self._name = name
        self._items: list["MenuItem"] = []

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_items(self):
        return self._items

    def set_items(self, value):
        self._items = value

    # The add_item method allows us to add items to the order,
    # which will be stored in the items list.
    def add_item(self, item: MenuItem):
        self._items.append(item)

    # The total_price method calculates the total price of all items in the order.
    def get_price_total(self):
        total = 0.0
        for item in self._items:
            total += item._price
        return total

    """ 
    In calculate_total_price allows identify the orders for determine 
    if gets discount of 15% or 10%.
    Receive a 10% discount when you place three orders from the following
    subclasses: drinks, main courses, and side dishes.
    Receive a 15% discount when you place all orders from all subclasses.
    """

    def calculate_total_price(self):
        # allows us to identify if the order includes items from each of the subclasses
        # (Drinks, PrincipalDishes, Desserts, AdditionalDishes)
        # to determine the applicable discount.
        asked_drink = False
        asked_principal_dishes = False
        asked_desserts = False
        asked_additional_dishes = False
        # We iterate through the items in the order and check their type to set
        # the corresponding flags (asked_drink, asked_principal_dishes, etc.)
        # to True if an item of that type is found.
        for item in self._items:
            if isinstance(item, Drinks):
                asked_drink = True
            if isinstance(item, PrincipalDishes):
                asked_principal_dishes = True
            if isinstance(item, Desserts):
                asked_desserts = True
            if isinstance(item, AdditionalDishes):
                asked_additional_dishes = True
        total = self.get_price_total()
        if (
            asked_drink
            and asked_principal_dishes
            and asked_desserts
            and asked_additional_dishes
        ):
            discount = total * 0.15
            return round(total - discount, 2)
        elif asked_drink and asked_principal_dishes and asked_additional_dishes:
            discount = total * 0.10
            return round(total - discount, 2)
        else:
            return round(total, 2)


class Drinks(MenuItem):
    def __init__(self, type_drink: str, size: str, name: str, price: float):
        super().__init__(name, price)
        self._type = type_drink
        self._size = size

    def get_type(self):
        return self._type

    def set_type(self, value):
        self._type = value

    def get_size(self):
        return self._size

    def set_size(self, value):
        self._size = value


class PrincipalDishes(MenuItem):
    def __init__(self, dish_type: str, dish_size: str, name: str, price: float):
        super().__init__(name, price)
        self._dish_type = dish_type
        self._dish_size = dish_size

    def get_dish_type(self):
        return self._dish_type

    def set_dish_type(self, value):
        self._dish_type = value

    def get_dish_size(self):
        return self._dish_size

    def set_dish_size(self, value):
        self._dish_size = value


class Desserts(MenuItem):
    def __init__(self, dessert_type: str, portion_size: str, name: str, price: float):
        super().__init__(name, price)
        self._dessert_type = dessert_type
        self._portion_size = portion_size

    def get_dessert_type(self):
        return self._dessert_type

    def set_dessert_type(self, value):
        self._dessert_type = value

    def get_portion_size(self):
        return self._portion_size

    def set_portion_size(self, value):
        self._portion_size = value


class AdditionalDishes(MenuItem):
    def __init__(self, portion_size: str, name: str, price: float):
        super().__init__(name, price)
        self._portion_size = portion_size

    def get_portion_size(self):
        return self._portion_size

    def set_portion_size(self, value):
        self._portion_size = value


class Payment:
    def __init__(self):
        pass

    def pay(self, amount: float) -> str:
        raise NotImplementedError("Subclasses must implement pay()")


class Card(Payment):
    def __init__(self, number: str, cvv: int):
        super().__init__()
        self._number = number
        self._cvv = cvv

    def pay(self, amount: float) -> str:
        return f"""
        Paying {amount} with card {self._number[-4:]}
        Transaction approved.
        """

    def get_number(self):
        return self._number

    def set_number(self, value: str):
        self._number = value

    def get_cvv(self):
        return self._cvv

    def set_cvv(self, value: int):
        self._cvv = value


class Cash(Payment):
    def __init__(self, amount_delivered: float):
        super().__init__()
        self._amount_delivered = amount_delivered

    def pay(self, amount: float) -> str:
        if self._amount_delivered >= amount:
            # genera cambio/vueltas
            return f"""    More needed to complete the payment. 
    Change: {round(self._amount_delivered - amount, 2)}"""
        else:
            return f"""Insufficient funds. 
             {round(amount - self._amount_delivered, 2)} more needed to complete the payment.
            """

    def get_amount_delivered(self):
        return self._amount_delivered

    def set_amount_delivered(self, value: float):
        self._amount_delivered = value


# test of program functionality
if __name__ == "__main__":
    # The restaurant opens (with all 10 dishes available)
    my_restaurant = Restaurant("The Corral Python", "Big")

    # The client arrives at table 1
    table_1 = Order("Table order 1")

    # The client orders a 10% combo (Drink + Main Course + Additional Dish)
    print("--- Taking the order ---".center(46))
    table_1.add_item(my_restaurant.menu[0])  # Order Coca-Cola
    table_1.add_item(my_restaurant.menu[3])  # Order Hamburguer
    table_1.add_item(my_restaurant.menu[8])  # Order the French fries
    print("-" * 43)
    print(f"Order 1: {my_restaurant.menu[0]}")
    print(f"Order 2: {my_restaurant.menu[3]}")
    print(f"Order 3: {my_restaurant.menu[8]}")

    # The results are printed
    print("Bill".center(43))
    print("-" * 43)
    print(
        f"total without discount: ${round(table_1.get_price_total(), 2)}"
    )  # Output: 18.0
    print(
        f"Discount applied: ${round(table_1.get_price_total() - table_1.calculate_total_price(), 2)}"
    )  # Output: 1.8
    print(
        f"Total to pay (with discount applied): ${round(table_1.calculate_total_price(), 2)}"
    )  # Output: 16.2
    end_total = table_1.calculate_total_price()
    print("\n------------- Process the pay -------------")
    # option A: Pay with cash
    metod_pay = Cash(20.0)
    # option B: Pay with card
    # metod_pay = Card("1234-5678-9012-3456", 123)
    print(metod_pay.pay(end_total))
    print("-" * 43)
    print("¡Thanks for your visit, see you later!")
