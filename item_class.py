#Defines the class Item
class Item(object):
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.loc = "No location has been set yet"
    
    def __str__(self):
        return "\n Item Name: " + self.name + "\n Current Count: " + str(self.count) + "\n Current Location: " + self.loc + "\n"
    
    def change_name(self, new_name):
        self.name = new_name
    
    def add_one(self):
        self.count = self.count + 1
    
    def set_total(self, total):
        self.count = total
    
    def remove_one(self):
        self.count = self.count - 1
    
    def change_loc(self, new_loc):
        self.loc = new_loc
    
    def get_name(self):
    	return self.name
    
    def get_count(self):
    	return self.count
    
    def get_loc(self):
    	return self.loc
