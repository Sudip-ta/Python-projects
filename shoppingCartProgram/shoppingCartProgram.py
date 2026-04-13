
foods = []
prices = []
total = 0

while True:
    food = input("Enter your food item and press q to quit: ")
    if food.lower() =="q" :
        break
    price = float(input("Enter the price: "))
    foods.append(food)
    prices.append(price)

print("--Your Cart--")
for x in range(len(foods)) :
    print(f"{foods[x]} ${prices[x]}")
    total +=prices[x]

print(f"Total price: ${float(total)}")