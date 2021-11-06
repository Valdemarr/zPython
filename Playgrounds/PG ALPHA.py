# Discord noob help

def checkout_item():
    n = 0
    total = 0

    while True:
        n += 1
        quantity = int(input(f"Enter quantity of item {n} purchased: "))

        price = int(input(f"Enter price of item {n}: "))

        total += quantity * price

        print(f"Your item total is: ${quantity * price }")

        again = input("Do you want to keep going?: ")

        if again == "yes" or again == "Yes":
            continue
        elif again == "no" or again == "No":
            print(f"Your order total is: ${total}")
            break
        else:
            print("Please type 'yes' or 'no'")


checkout_item()
