# Thoughts on this prog:
# This prog could definitely be done in a better way. The storage of items needs to be persistant,
# which it is not currently. It could use an SQL database for this. Another idea is to store the
# items as independent files modifiable with IO, instead of as class objects. That way the item
# could be opened and remain open and modifiable until closed. Right now, modifying an item once
# takes you back to the main menu, which is frustrating and adds a lot of work. A GUI would help in
# this regard as well. Look into adding SQL capabilities. 

#this class defines the inventory item
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
        self.loc = new_loc
    
    def get_name(self):
    	return self.name
    
    def get_count(self):
    	return self.count
    
    def get_loc(self):
    	return self.loc

#prompts the user for an item name when adding a new item to the inventory
def get_new_item_name():
    n = str(raw_input("What is the NAME of the new item? \n"))
    print "The name of the new item is %s." % n
    return n

#prompts the user for an initial count of the item when adding a new item to the inventory
def get_new_item_count(name):
    cnt_str = str(raw_input("How many %s do you currently count? \n" % name))
    while cnt_str.isdigit() == False:
        print "Sorry, that is not a valid number. Please try again. "
        cnt_str = str(raw_input("How many %s do you currently count? \n" % name))
    else:
        return int(cnt_str)

#initializes a dictionary of the inventory items
inven_dict = {}

#creates a new item and adds it to the dictionary
def add_item():
    new_name = get_new_item_name()
    inven_dict[new_name] = item(new_name, get_new_item_count(new_name))

#allows the user to view an item of their choice
def view_item():
    i = raw_input("Which item would you like to view? \n")
    #need to add a validity check here, to make sure i is in inven_dict
    print inven_dict[i]

#allows user to modify an already created item
def change_item():
    #need to add a validity check here, to make sure i is in inven_dict
    i = raw_input("Which item would you like to change? \n")
    print "You are updating %s. How would you like to update it?" %inven_dict[i].get_name()
    usr_inpt = str(raw_input("Enter 'n' to change the name. Enter 'c' to change the count. Enter 'l' to change the location: "))
    if usr_inpt == 'n':
        inven_dict[i].change_name(str(raw_input("Please enter a new name for the item: ")))
        print "The new name of the item is: %s" %inven_dict[i].get_name()
        # Changes the name, but does not change the dictionary entry. Will throw an error.
    elif usr_inpt == 'c':
        print "How would you like to change the count?"
        cnt_chng = str(raw_input("Enter '+' to add one to the count. Enter '-' to subtract one. Enter 't' to change the total count: "))
        if cnt_chng == '+':
            inven_dict[i].add_one()
        elif cnt_chng == '-':
            inven_dict[i].remove_one()
        elif cnt_chng == 't':
            #needs to check if input actually is an int
            inven_dict[i].set_total(int(raw_input("Please enter the new total count as a whole number: ")))
        else:
            print "That is not a valid response."
        print "The count of %s is now %i." % (inven_dict[i].get_name(), inven_dict[i].get_count())
    elif usr_inpt == 'l':
        inven_dict[i].change_loc(str(raw_input("Please enter the new location of the item: ")))
    else:
        print "That is not a valid response." 

#allows the while loop to begin
inven_run = True

#set of instructions for the user
instruct = ("""Enter 'a' to add an item. 
Enter 'c' to change an item. 
Enter 'r' to remove an item. 
Enter 'v' to view an item. 
Enter 'va' to view all items currently in inventory. 
Enter 'q' to quit. 
Enter 'h' to see these instructions again. """)

#prints welcome message and the instructions
print "Hello, and welcome to your inventory!"
print instruct

#main program loop
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
    elif answer == 'c':
        change_item()
    elif answer == "printdict":
    	print inven_dict
    else:
    	print "testing"

print "Thank you!"
