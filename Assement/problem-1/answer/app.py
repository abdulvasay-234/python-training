# Restaurant Billing System

menu_items = ["Pizza", "Burger", "Pasta", "Biryani", "Sandwich"]
menu_prices = [250, 150, 200, 180, 120]

print("----- RESTAURANT MENU -----")
print(menu_items[0], "-", menu_prices[0])
print(menu_items[1], "-", menu_prices[1])
print(menu_items[2], "-", menu_prices[2])
print(menu_items[3], "-", menu_prices[3])
print(menu_items[4], "-", menu_prices[4])

item1 = input("Enter your first food item: ")
item2 = input("Enter your second food item: ")

price1 = menu_prices[menu_items.index(item1)]
price2 = menu_prices[menu_items.index(item2)]

total_amount = price1 + price2
gst = total_amount * 18 / 100
final_bill = total_amount + gst

print("\n----- BILL -----")
print("Selected Item 1:", item1)
print("Selected Item 2:", item2)
print("Total Amount:", total_amount)
print("GST (18%):", gst)
print("Final Bill:", final_bill)
