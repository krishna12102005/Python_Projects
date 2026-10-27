items = {"pizza" : 1.2,
         "banan" : 4.5,
         "orange": 7,
         "Mango" : 6.7,
         "Coconut": 8.9}

cart = []
total = 0

for key , value in items.items():
    print(f"{key} : {value}")

while True:
    food = input("Enter the food (q to quit) :")
    if food == "q":
        break
    elif items.get(food) is not None:
        cart.append(food)



for i in cart:
    total = total + items.get(i)

print(f"Your total is ${total}")

