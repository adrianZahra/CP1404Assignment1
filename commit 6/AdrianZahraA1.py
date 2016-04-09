"""Adrian Zahra, 21/3/2016, AdrianZahraA1, https://github.com/adrianZahra/CP1404Assignment1.git"""

def show_all_items():
    item_count_number = -1
    for list_print_1 in mylist:
        if len(list_print_1[3]) == 3:
            item_count_number += 1
            print("{0} = {1} = ${2} *".format(item_count_number, list_print_1[0:2], list_print_1[2]))
        else:
            item_count_number += 1
            print("{0} = {1} = ${2}".format(item_count_number, list_print_1[0:2], list_print_1[2]))
    return


def hire_and_return(number_check, in_out_check, stock_check):
    item_count_number = -1
    print("These are the items currently {0} stock".format(stock_check))
    for list_print_2 in mylist:
        if len(list_print_2[3]) != number_check:
            item_count_number += 1
            print("{0} = {1} = ${2}".format(item_count_number, list_print_2[0:2], list_print_2[2]))

    item_to_check = str(input("enter the name of the item you wish to hire"))
    for i, item_name in enumerate(mylist):
        if item_name[0] == item_to_check:
            temp = list(mylist[i])
            temp[3] = in_out_check
            mylist[i]=tuple(temp)
    for thingeee in mylist:
        print(thingeee[0:])
    return


def add_item_to_list():
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
    return


def save_list():
    file_write = open("items.csv", "w")
    for set_items in mylist:
        write_stuff = str(set_items)
        write_stuff.split("( )")
        print(write_stuff)
        file_write.write(write_stuff.strip("( )").replace("'","").strip() + "\n")
    return


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


user_input = str(input("Menu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")).upper()

while user_input != "Q":
    if user_input == "L":
        show_all_items()

    elif user_input == "H":
        hire_and_return(3, "out", "in")

    elif user_input == "R":
        hire_and_return(2, "in", "out of")

    elif user_input == "A":
        add_item_to_list()

    else:
        print("Invalid")
    user_input = str(input("Menu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")).upper()

print("Good Bye, Have a nice day")
save_list()