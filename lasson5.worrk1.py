purchase = float (input( "შეიყვანეთ ყიდვის თანხა: "))
promo_code = input("შეიყვანეთ პრომო კოდი (თუ არ გაქვთ, დააჭირეთ Enter): ")

if purchase >= 200:
    discount_percent = 20
elif purchase >= 100:
    discount_percent = 10
elif purchase >= 50:
    discount_percent = 5
else:
    discount_percent = 0

discount_amount = purchase * discount_percent / 100
final_price = purchase - discount_amount

if promo_code.strip().lower() == "vip":
    final_price -= 5

print(f"ფასდაკლების პროცენტი: {discount_percent}%")
print(f"გადასახდელი თანხა: {final_price:.2f} ლარი")