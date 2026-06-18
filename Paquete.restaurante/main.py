from restaurant import Restaurant, Order, Cash#, Card

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
