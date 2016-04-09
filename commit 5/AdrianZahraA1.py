"""Adrian Zahra, 21/3/2016, AdrianZahraA1, https://github.com/adrianZahra/CP1404Assignment1.git"""
print("Items for Hire - by Adrian Zahra")

mylist = []
in_file = open("items.csv", "r")
#this first part is where the file opens and assignes the csv's to a place in the list
for line in in_file:
    item_match = line.strip().replace(" ","").split(",")
    name = item_match[0]
    description = item_match[1]
    price = item_match[2]
    hired = item_match[3]

    mylist.append((item_match[0], item_match[1], item_match[2], item_match[3]))


in_file.close()

#this is where the loop to run the program begins
user_input = str(input("Menu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")).upper()



while user_input != "Q":
    if user_input == "L":
        item_count_number = -1
        for list_print_1 in mylist:
            if len(list_print_1[3]) == 3:
                item_count_number += 1
                print("{0} = {1} = ${2} *".format(item_count_number, list_print_1[0:2], list_print_1[2]))
            else:
                item_count_number += 1
                print("{0} = {1} = ${2}".format(item_count_number, list_print_1[0:2], list_print_1[2]))


    elif user_input == "H":
        item_count_number = -1
        print("These are the items currently in stock")
        for list_print_2 in mylist:
            if len(list_print_2[3]) != 3 :
                item_count_number += 1
                print("{0} = {1} = ${2}".format(item_count_number, list_print_2[0:2], list_print_2[2]))

        item_to_check = str(input("enter the name of the item you wish to hire"))
        for i, item_name in enumerate(mylist):
            if item_name[0] == item_to_check:
                temp = list(mylist[i])
                temp[3] = "out"
                mylist[i]=tuple(temp)
        for thingeee in mylist:
            print(thingeee[0:])


    elif user_input == "R":
        item_count_number = -1
        print("These are the items currently out of stock")
        for list_print_2 in mylist:
            if len(list_print_2[3]) != 2 :
                item_count_number += 1
                print("{0} = {1} = ${2} *".format(item_count_number, list_print_2[0:2], list_print_2[2]))

        item_to_check = str(input("enter the name of the item you wish to hire"))
        for i, item_name in enumerate(mylist):
            if item_name[0] == item_to_check:
                temp = list(mylist[i])
                temp[3] = "in"
                mylist[i]=tuple(temp)
        for thingeee in mylist:
            print(thingeee[0:])

    elif user_input == "A":
        item_count_number = -1
        input_name = str(input("Item Name: "))
        input_description = str(input("Description: "))
        input_price = str(input("Price per day: $"))
        input_hire_status = "in"
        mylist.append((input_name, input_description, input_price, input_hire_status))
        for list_print_3 in mylist:
            if len(list_print_3[3]) == 3:
                item_count_number += 1
                print("{0} = {1} = ${2} *".format(item_count_number, list_print_3[0:2], list_print_3[2]))
            else:
                item_count_number += 1
                print("{0} = {1} = ${2}".format(item_count_number, list_print_3[0:2], list_print_3[2]))

    else:
        print("Invalid")
    user_input = str(input("Menu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")).upper()



file_write = open("items.csv", "w")
for set_items in mylist:
    write_stuff = str(set_items)
    write_stuff.split("( )")
    print(write_stuff)
    file_write.write(write_stuff.strip("( )").replace("'","").strip() + "\n")



print("Good Bye Have a nice day")