# The Fresh Greengrocer

apple_price = 0.85
pear_price = 0.65
orange_price = 0.90

apples = 8
pears = 6
oranges = 4

apple_total = apples * apple_price
pear_total = pears * pear_price
orange_total = oranges * orange_price

amount_due = apple_total + pear_total + orange_total

print("Apple cost: R", format(apple_total, ".2f"))
print("Pear cost: R", format(pear_total, ".2f"))
print("Orange cost: R", format(orange_total, ".2f"))
print("Total amount due: R", format(amount_due, ".2f"))

money = 20.00
change = money - amount_due

print("Money available: R", format(money, ".2f"))
print("Change: R", format(change, ".2f"))