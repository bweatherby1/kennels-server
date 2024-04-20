class Customer():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        
new_customer = Customer(1, "Brad", 21)

print(new_customer.name)
