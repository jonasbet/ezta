
import ipaddress
import pandas

def get_server_list():
    fileName = "serverList.csv"
    df = pandas.read_csv(fileName)
    return df

def get_serverIp_by_destPort(destPort, df):
    #df[df.Letters == 'C'].Letters.item()
    #df.loc[df['favorite_color'] == 'yellow']
    #print (df.loc[df.name == 'george', 'age'].iat[0])

    print( df.loc[df['destPort'] == int(destPort)] )
    serverIp = df.loc[df['destPort']== int(destPort), 'serverIp'].iat[0]
    print(serverIp)
    return serverIp

def ramdom_ephimeralPort_selection():
    return ramdomEphimeralPort







def menu():
    loop_condition = True
    df = get_server_list()


    while loop_condition:
        print("\nWelcome to HeraclitusModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Request a new Subnet")
        print("Enter 2 Update serverList")
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

            serverIp = get_serverIp_by_destPort(destPort, df)
            print("\nYour data is now saved as ServerIp = {}, destPort = {}. \n".format(
                serverIp, destPort))

            menu()

        elif menu_choice == 2:
            get_server_list()

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


