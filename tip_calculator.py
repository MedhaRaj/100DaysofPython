bill_total = int(input("Welcome to the tip calculator\nWhat was the bill total?\n"))
tip = int(input("How much tip would you like to give, 10$, 15$ or 20$?\n"))
splitt_bill = int(input("How many people would you like to split the bill with?"))

total_w_tip = bill_total+tip
per_person = total_w_tip/splitt_bill
print(f"\nEach person should pay: $ {per_person} people")
