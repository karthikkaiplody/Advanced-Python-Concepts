from item import Item
from phone import Phone

item1 = Item("MyItem", 1000)
item1.name = "OtherItem"

print(item1.name)

item1.send_mail()

item2 = Phone("MyPhone", 1000)
item1.apply_discount()
print(f"Discounted item1 price = {item1.price}")
item2.apply_discount()
print(f"Discounted item2 price = {item2.price}")