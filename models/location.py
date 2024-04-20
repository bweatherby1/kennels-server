class Location():
    def __init__(self, id, name, address, city):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        
new_location = Location(5, "Nashville West", "1234 Chatlotte Pike", "Nashville")

print(new_location.name)
