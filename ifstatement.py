amount = int(input("Enter Amount: "))
if amount<1000:
    discount = amount * 0.10
    print("Discount : ", discount)
else:
    discount = amount * 0.20
    print("Discount : ", discount)
print("Net Amount : ", amount - discount)

