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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    # Getter - if we do item1.name will call this
    # Making the name as a private attribute by restricting the access to change it.
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name # __ Prevent the access of __name in the code 

    # Setter - if we do item1.name="OtherItem" will call this
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Thae name is too long")
        else:    
            self.__name = value

    # Encapsulation
    # =================    
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # =================

    def calculate_total_price(self):
        return self.__price * self.quantity
    
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
        # return f"Item('{self.name}', {self.__price}, {self.quantity})"
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    # Abstraction - Hiding un-neccessary information from instance level 
    # By adding __ infront will make the methods private 
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone,
        We have {self.name} {self.quantity} times
        Regards One
        """
    
    def __send(self):
        print("Mail Sent!!")

    def send_mail(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
