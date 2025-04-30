import random


def open_gift_box(gift_item):
    is_gift = random.choice([True, False])

    print("\nIs gift present: ", is_gift)
    if is_gift:
        return gift_item

    print("Recursion here")
    open_gift_box(gift_item)


random_gift_item = random.choice(["Ball", "Pen", "Dress", "Cake", "Chocolate", "Car", "Toy", "Doll"])
result = open_gift_box(gift_item=random_gift_item)
print(result)