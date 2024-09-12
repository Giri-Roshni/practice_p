#define the menu of resturant
menu={
    'Pizza':300,
    'Burger':140,
    'Salad':100,
    'Samosa_chat':80,
    'Chicken_momo':150
}
print("Welcome to Rose Resturant")
print("Pizza: Rs.300\nBurger:Rs.140\nSalad:Rs.100\nSamosa_chat:Rs.80\nChicken_momo:150")

order_total = 0

item_1=input("Enter the name of the item you want to order :")
if item_1 in menu:
    order_total += menu[item_1] #0 +300
    print(f"{item_1} has been added to your order :")
else:
    print(f"ordered item {item_1} is not available yet")

another_order = input("Do you want anything else!? :")
if another_order == "yes":
    item_2 = input("Enter the name of the second item :")
    if item_2 in menu:
        order_total += menu[item_2] 
        print(f"{item_2} has been added to your order:")
    else:
        print(f"ordered item {item_2} is not available!")
print(f"The total amount  is {order_total}:-")

