
print("Items for Hire - by Adrian Zahra")

mylist = []
in_file = open("items.csv", "r")
#this first part is where the file opens and assignes the csv's to a place in the list
for line in in_file:
    item_match = line.strip().split(",")
    name = item_match[0]
    description = item_match[1]
    price = item_match[2]
    hired = item_match[3]

    mylist.append((item_match[0], item_match[1], item_match[2], item_match[3]))

in_file.close()

user_input = str(input("Menu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")).upper()

while user_input != "Q":
    if user_input == "L":
        for thing in mylist:
            print(thing[0:3])

    elif user_input == "H":
        print("These are the items currently in stock")
        for thing in mylist:
            if len(thing[3]) != 3 :
                print(thing[0:3])

    elif user_input == "R":
        print("this is for RRRRRRRRRRRR")

    elif user_input == "A":
        list_place_1 = str(input("Enter the name of the item: "))
        list_place_2 = str(input("Enter a description of the item"))
        list_place_3 = str(input("Enter the price of the item"))
        list_place_4 = str(input("Enter the items rental status"))
        mylist.append((list_place_1, list_place_2, list_place_3, list_place_4))
        for thing in mylist:
            print(thing[0:3])

    else:
        print("Invalid")
    user_input = str(input("Menu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")).upper()

print("Good Bye Have a nice day")