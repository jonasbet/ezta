
import ipaddress





def menu():
    loop_condition = True

    while loop_condition:
        print("\nWelcome to HeraclitusModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Request a new Subnet")
        print("Enter 2 ....")
        print("Enter 3 ....")
        print("Enter 4 .....")
        print("Enter 5 ....")
        print("Enter 0 To exit application.")
        menu_choice = int(input("\nWhat would you like to do? \n"))


        if menu_choice == 0:
            print("\n Thanks for using the application")
            exit(0)
        elif menu_choice == 1:
            aristotleHash = input("\n Please provide the AristotleHash.")
            destPort = input("\n Please provide the destPort in binary.")

            print("\nYour data is now saved as  aristotleHash = {}, destPort = {}. \n".format(
                aristotleHash, destPort))
            menu()

        elif menu_choice == 2:
# using 2 for testing

            menu()
        elif menu_choice == 3:
            menu()
        elif menu_choice == 4:
            menu()
        elif menu_choice == 5:
            menu()
        else:
            print("\nSorry the valid options are between 0 and 5.\n")
            menu()
menu()


