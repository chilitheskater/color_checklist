checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)        

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1   

#def mark_completed(index):
    # Add code here that marks an item as completed


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

# TEST
def test():
    create("purple sox")

    create("red cloak")

    list_all_items()

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list")
    select(selection)
