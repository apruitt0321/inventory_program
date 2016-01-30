class item(object):
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.loc = "No location has been set yet"
    
    def __str__(self):
        return " Item Name: " + self.name + "\n Current Count: " + str(self.count) + "\n Current Location: " + self.loc
    
    def change_name(self, new_name):
        self.name = new_name
    
    def add_one(self):
        self.count = self.count + 1
    
    def set_total(self, total):
        self.count = total
    
    def remove_one(self):
        self.count = self.count - 1
    
    def change_loc(self, new_loc):
        self.lock = new_loc
    
    def get_name(self):
    	return self.name
    
    def get_count(self):
    	return self.count
    
    def get_loc(self):
    	return self.loc


def get_new_item_name():
    n = str(raw_input("What is the NAME of the new item? \n"))
    print "The name of the new item is %s." % n
    return n

def get_new_item_count(name):
    cnt_str = str(raw_input("How many %s do you currently count? \n" % name))
    while cnt_str.isdigit() == False:
        print "Sorry, that is not a valid number. Please try again. "
        cnt_str = str(raw_input("How many %s do you currently count? \n" % name))
    else:
        return int(cnt_str)

inven_dict = {}

#def get_dict_obj(i):
#    return inven_dict[i]

def add_item():
    new_name = get_new_item_name()
    inven_dict[new_name] = item(new_name, get_new_item_count(new_name))

def view_item():
    i = raw_input("Which item would you like to view? \n")
    print inven_dict[i]
    print inven_dict[i].get_name()

inven_run = True


instruct = ("Enter 'a' to add an item. \n\
Enter 'c' to change an item. \n\
Enter 'r' to remove an item. \n\
Enter 'v' to view an item. \n\
Enter 'va' to view all items currently in inventory. \n\
Enter 'q' to quit. \n\
Enter 'h' to see these instructions again. ")

print "Hello, and welcome to your inventory!"
print instruct

while inven_run:
    answer = raw_input("Please enter a command: ")
    if answer == 'q':
    	inven_run = False
    elif answer == 'h':
    	print instruct
    elif answer == 'a':
	add_item()
    elif answer == 'va':
        print inven_dict.keys()
    elif answer == 'v':
        view_item()
    elif answer == "printdict":
    	print inven_dict
    else:
    	print "testing"

print "Thank you!"
