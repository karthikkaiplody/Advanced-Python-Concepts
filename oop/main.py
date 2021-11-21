import csv

class Item:
    # Class attributes
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # To store all the instance value which are created.
    __version__ = "Item-version-0.1"

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {price} is not greater than or equal to zero!"

        # Assign to self object -> instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # Methods which can be accessed with class level only
    @classmethod    
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        print("Instantiate Items from items.csv")

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    # Regular or isolated function        
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False    

    # Magic method to represent the instances of the Item class
    def __repr__(self) -> str:
        # return f"Item('{self.name}', {self.price}, {self.quantity})"
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# Child class (Phone) of Parent class (Item)
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        # Call to super function to have access to all Parent class
        super().__init__(name, price, quantity=quantity)

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"
        self.broken_phones = broken_phones

# print(Item.all)
# Item.instantiate_from_csv()
# print(Item.all)

phone1 = Phone("nkPhonev10", 500, 5)
phone1.broken_phones = 1