

def placeorder(item, qty):
    print("\nOrder placed")
    print("**** Order Summary ****")
    print(f"Item: {item}")
    print(f"Quantity: {qty}")


def calc_order(item, qty, price):
    total = qty * price

    print("\n**** Order Summary ****")
    print(f"Item:                 {item}")
    print(f"Quantity:             {qty}")
    print(f"Price per item:      R{price:.2f}")
    print("----------------------------------")
    print(f"Total cost:          R{total:.2f}")
    print("----------------------------------")

item = input("Enter food item: ")
qty = int(input("Enter quantity: "))
price = float(input("Enter price per item: R"))


placeorder(item, qty)
calc_order(item, qty, price)
