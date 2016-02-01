# Thoughts on this prog:
# This prog could definitely be done in a better way. The storage of items needs to be persistant,
# which it is not currently. It could use an SQL database for this. Another idea is to store the
# items as independent files modifiable with IO, instead of as class objects. That way the item
# could be opened and remain open and modifiable until closed. Right now, modifying an item once
# takes you back to the main menu, which is frustrating and adds a lot of work. A GUI would help in
# this regard as well. Look into adding SQL capabilities. 

#prompts the user for an item name when adding a new item to the inventory
def get_new_item_name():
    n = str(raw_input("What is the name of the item? \n"))
    print "The name of the item is %s." % n
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
    new_count = get_new_item_count(new_name)
    inven_dict[len(inven_dict)] = {"Name: ":new_name, "Count: ":new_count, "Location: ":"No location set yet"}

#allows the user to view an item of their choice
def view_item():
    for x in inven_dict:
        print "%i: %s" % (x, inven_dict[x]["Name: "])
    # Needs an if/else statement, to determine if there are any items in the inv
    # Cannot have the input immediately stored as int. Must make sure that it isdigit first. 
    i = int(raw_input("Please enter the number of the item you would like to view: "))
    while inven_dict.has_key(i) == False:
        print "Sorry, that is not a valid item. Please try again. \n"
        ui = raw_input("Please enter the number of the item you would like to view: ")
        if ui.isdigit() == False:
            if ui == 'q':
                break
            else:
                print "Sorry, that is not a valid item. Please try again. \n"
        else:
            i = int(ui)
    else:
        print str(inven_dict[i])

#allows user to modify an already created item
def change_item():
    iter = 0
    for x in inven_dict:
        print "%i: %s" % (x, inven_dict[x]["Name: "])
        iter += 1
    if iter == 0:
        print "There are no items in the inventory yet."
    # everything after needs to be in an else statement. if no items in inv, doesn't ask.
    #cannot have the input immediately stored as int. Must make sure that it isdigit first.
    i = int(raw_input("Please enter the number of the item you would like to update: "))
    while inven_dict.has_key(i) == False:
        print "Sorry, that is not a valid item. Please try again. \n"
        ui = raw_input("Please enter the number of the item you would like to update: ")
        if ui.isdigit() == False:
            if ui == 'q':
                break
            else:
                print "sorry, that is not a valid item. Please try again. \n"
        else:
            i = int(ui)
    else:
        print "You are updating " + inven_dict[i]["Name: "] +  ". How would you like to update it? \n"
    usr_inpt = str(raw_input("Enter 'n' to change the name. Enter 'c' to change the count. Enter 'l' to change the location: "))
    if usr_inpt == 'n':
        inven_dict[i]["Name: "] = get_new_item_name()
    elif usr_inpt == 'c':
        print "How would you like to change the count?"
        cnt_chng = str(raw_input("Enter '+' to add one to the count. Enter '-' to subtract one. Enter 't' to change the total count: "))
        if cnt_chng == '+':
           inven_dict[i]["Count: "] += 1
        elif cnt_chng == '-':
            inven_dict[i]["Count: "] -= 1
        elif cnt_chng == 't':
            print "testing"
            #needs to check if input actually is an int
            #inven_dict[i].set_total(int(raw_input("Please enter the new total count as a whole number: ")))
        else:
            print "That is not a valid response."
        print "The count of %s is now %i." % (inven_dict[i]["Name: "], inven_dict[i]["Count: "])
    elif usr_inpt == 'l':
        inven_dict[i]["Location: "] = raw_input("Please enter the new location of the item: ")
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
print "Hello, and welcome to your inventory, V.2!"
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
        for x in inven_dict:
            print "%i: %s" % (x, inven_dict[x])
    elif answer == 'v':
        view_item()
    elif answer == 'c':
        change_item()
   # elif answer == "printdict":
    #	print inven_dict
    else:
    	print "testing"

print "Thank you!"
