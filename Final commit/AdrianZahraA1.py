"""Adrian Zahra, 21/3/2016, AdrianZahraA1, https://github.com/adrianZahra/CP1404Assignment1.git"""


def show_all_items(items_list):
    # this is the function that prints all items in the list
    print("All items on file (* indicates item is currently out):")
    item_count_number = -1
    for printing_items in items_list:
        if len(printing_items[3]) == 3:
            item_count_number += 1
            print("{0} = {1} = ${2} *".format(item_count_number, printing_items[0:2], printing_items[2]))
        else:
            item_count_number += 1
            print("{0} = {1} = ${2}".format(item_count_number, printing_items[0:2], printing_items[2]))
    return


def hire_and_return(items_list, in_out_check, input_status):
    # this fuction doubles as both the hire and return function
    # by using enumerate the function finds the indexes contents and number which allows for over writing
    """Function hire_and_return(inOrOutTest)
        Get itemToTest
        itemToTest = itemToTest as string
        For i in ItemsList
            If itemToTest as string is in itemsList
            IndexPlace = ItemsList[0]
            IndexPlace[index where in/out string is stored] = inOrOutTest
            itemsList[i] = IndexPlace
        return itemsList
    """

    item_to_check = str(input("Enter the name of the item you wish to {0}: ".format(input_status)))
    for place_holder, item_name in enumerate(items_list):
        if item_name[0] == item_to_check:
            index_place = list(items_list[place_holder])
            index_place[3] = in_out_check
            items_list[place_holder] = tuple(index_place)
    return


def add_item_to_list(items_list):
    # this fucntion alows items to be added to the list
    item_count_number = -1
    input_name = str(input("Item Name: "))
    input_description = str(input("Description: "))
    # a try and except check the users input to see if it is correct
    try:
        input_price = float(input("Price per day: $"))
        str(input_price)
    except ValueError:
        print("Invalid input")
        input_price = float(input("Price per day: $"))
        str(input_price)
    input_hire_status = "in"
    items_list.append((input_name, input_description, input_price, input_hire_status))
    print("{0} {1}, ${2} now available for hire".format(input_name, input_description, input_price))
    return


def save_list(items_list):
    # this fucntion saves the items in the list back to the csv file
    # it works by adding back in new lines and removing the brackets from the converted string
    file_write = open("items.csv", "w")
    for set_items in items_list:
        write_stuff = str(set_items)
        write_stuff.split("( )")
        file_write.write(write_stuff.strip("( )").replace("'", "").strip() + "\n")
    return


def loading_items():
    """
    Function addFileItemsToList()
    itemsList = emptyList
    open “items.csv” as inFile for reading
    for line in inFile
        itemMatch = separate “items.csv”  at “,”
        itemsList[0] = nameItemMatch
        itemsList[1] = descriptionItemMatch
        itemsList[2] = priceItemMatch
            itemsList[3] = hiredItemMatch
    print itemsList
    close inFile
    """

    items_list = []
    in_file = open("items.csv", "r")
    # this first part is where the file opens and assignes the csv's to a place in the list
    # the items are seperated by the , in the file and split into indexes
    for line in in_file:
        item_match = line.strip().replace(" ", "").split(",")
        name = item_match[0]
        description = item_match[1]
        price = item_match[2]
        hired = item_match[3]

        items_list.append((item_match[0], item_match[1], item_match[2], item_match[3]))
    in_file.close()
    return items_list


def main(items_list):
    # this is the main loop where the menu runs from
    print("Items for Hire - by Adrian Zahra")

    user_input = str(
        input(
            "Menu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")).upper()

    while user_input != "Q":
        if user_input == "L":
            show_all_items(items_list)

        elif user_input == "H":
            hire_and_return(items_list, "out", "hire")

        elif user_input == "R":
            hire_and_return(items_list, "in", "return")

        elif user_input == "A":
            add_item_to_list(items_list)

        else:
            print("Invalid menu choice")
        user_input = str(input(
            "Menu: \n(L)ist all items \n(H)ire an item \n(R)eturn an item \n(A)dd new item to stock \n(Q)uit")).upper()

    print("Good Bye, Have a nice day")
    save_list(items_list)
    return


if __name__ == "__main__":
    main(loading_items())
