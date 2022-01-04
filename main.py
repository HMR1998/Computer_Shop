computer_parts = ["Computer",
                  "Monitor",
                  "Keyboard",
                  "Mouse",
                  "Mouse Pad",
                  "HDMI Cable",
                  "Ethernet Cable",
                  "Cable"
                  ]
valid_choices = []
# creating empty lists and adding valid choices to said list
for i in range(1, len(computer_parts) + 1):
    valid_choices.append(str(i))  # storing index numbers in variable valid_choices
customer_choice = "-"  # enters loop and prints menu
cart = [] # list of parts customer have chosen to buy

while customer_choice != '0':  # keep repeating till user enters 0
    if customer_choice in valid_choices:
        index = int(customer_choice) - 1
        customer_choice = computer_parts[index]
        if customer_choice in cart:
            print("Removing {}".format(customer_choice))
            cart.remove(customer_choice)
        else:
            print("Adding {}".format(customer_choice))
            cart.append(customer_choice) # stores customer choice into cart list
        print("your list contains {}".format(cart))
    else:
        print("Add options from menu: ")
        for number, part in enumerate(computer_parts):
            print("{0}: {1}".format(number + 1, part))  # using index to print location
            # and +1 to start from 1 rather then 0
    customer_choice = input("What would you like to buy? ")

print("You have bought {}".format(cart))