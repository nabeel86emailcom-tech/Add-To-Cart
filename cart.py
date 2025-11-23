from items import fruits_list
for item,price in fruits_list.items():
    print(f"{item.capitalize()} Rs. {price}")

cart={}
total=0
while True:

    choice=input("Enter Product To Add In Cart Or(done):").lower()

    if choice=="done":
        break
    
    if choice in fruits_list:
        qty=input("Enter Quantity:")

        if qty.isdigit():
           qty=int(qty)
           cart[choice]=cart.get(choice,0)+qty
           print("Your Product is Added")
        else:
            print("Invalid Choice!")
    else:
        print("This Product is Not Available")

for item,qty in cart.items():
        price=fruits_list[item]
        cost=price*qty
        total += cost 
        print(f"{item} x {qty} and total is {total}")

