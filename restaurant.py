# Restaurant Mini project (using python)
menu={
      "pizza":100,
      "burger":50,
      "fries":80,
      "sandwitch":80,
      "hotcoffee":50,
      "coldcoffee":40
}

print("*****Welcome to our restaurant*****")
print("pizza     :100\nburger    :50\nfries     :80\nsandwitch :80\nhotcoffee :50\ncoldcoffee:40")

ord_amt=0
order=input("What you want to order :")
if order in menu:
    ord_amt+=menu[order]
    print(f"your {order} of amount {menu[order]} added")
else:
   print("Give only order from menu !!")
   order=input("What you want to order :")
   if order in menu:
     ord_amt+=menu[order]
     print(f"your {order} of amount {menu[order]} added")

another_ord=input("You want to order somthing else ? (yes/no) :")

if another_ord=="yes":
    order=input("What you want to order :")
    if order in menu:
     ord_amt+=menu[order]
     print(f"The total amount of order is {ord_amt}")
    else:
     print("Give only order from menu !!")
else:
   print(f"The total amount of order is {ord_amt}")