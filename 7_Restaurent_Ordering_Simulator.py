# Milestone 1: Goal: Represent a restaurant menu and display it.
# Create a list of food items
food_items = ["Pasta", "Pizza", "Burger", "Noodles"]
# Create a separate list for prices
food_prices = [10, 12, 30, 5]
# Print the menu in a clean format
print("\nSl. \tItem \tPrice")
counter = 1
while counter <= len(food_items):
    sl = counter - 1
    print(f"{counter}. \t{food_items[sl]} \tRs.{food_prices[sl]}")
    counter = counter + 1

# Milestone2:Goal: Use this menu to build an order system
# Let a user “pick” items (simulate for now)
user_input_food_list = []
user_input_food_quantity_list = []
order_item = 1

user_input = input(
    "\nPlease let me know if you would like to order some food (Y for Yes, N for No): "
).title()
while user_input == "Y":
    user_input_food = input(
        "Happy to help!! Please let me know the food you would like to oder from the Menu: "
    ).title()
    user_input_food_quantity = int(
        input("Please let me know the quantity you would like to order for: ")
    )
    # Store selected items in a new list
    user_input_food_list.append(user_input_food)
    user_input_food_quantity_list.append(user_input_food_quantity)
    # Display the growing order
    print(
        f"As of order {order_item}, you have ordered {user_input_food_quantity} number/s of {user_input_food}"
    )
    order_item += 1
    user_input = input(
        "\nPlease let me know if you would like to order some more items? (Y for Yes, N for No: )"
    ).title()

print("\nOrder List")
print("-----------")
print("Order sl. \tOrder_item \tOrder Quantity")
sl2 = 0
while sl2 < len(user_input_food_list):
    print(
        f"{sl2 + 1}. \t{user_input_food_list[sl2]} \t{user_input_food_quantity_list[sl2]}"
    )
    sl2 += 1
