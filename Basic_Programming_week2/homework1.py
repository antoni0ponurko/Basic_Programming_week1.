my_trousers = int(input("How many trousers have been bought: "))
my_tshirt = int(input("How many T-shirts have been bought: "))
my_vests = int(input("How many vests have been bought: "))

total = 604.87

my_package = {
    "trousers": my_trousers,
    "tshirt": my_tshirt,
    "vests": my_vests
}


def process_payment(payment_details, total_amount):
    return True


def checkout(payment_details):
    return total


if process_payment(my_package, total):
    print(f"Payment successful! Total amount to pay: ${total:.2f}")
else:
    print("Payment failed!")
