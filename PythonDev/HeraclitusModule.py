
import ipaddress
import pandas
import random
import csv


def get_heraclitusLine_by_aristotleHash(aristotleHash, df):
    print(df)
#aristotleHash,serverIp,destPort,serverPort,heraclitusIp,heraclitusPort
    serverIp = df.loc[df['aristotleHash']== aristotleHash, 'serverIp'].iat[0]
    destPort = str(df.loc[df['aristotleHash'] == aristotleHash, 'destPort'].iat[0])
    serverPort = str(df.loc[df['aristotleHash']== aristotleHash, 'serverPort'].iat[0])
    heraclitusIp = df.loc[df['aristotleHash']== aristotleHash, 'heraclitusIp'].iat[0]
    heraclitusPort = str(df.loc[df['aristotleHash']== aristotleHash, 'heraclitusPort'].iat[0])
    oneLineExport = aristotleHash + '#' + serverIp + '#' + destPort + '#' +\
    serverPort + '#' + heraclitusIp  +   '#' +  heraclitusPort
    print( oneLineExport )

def get_csv_file(fileName):
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

def get_ramdom_ephimeralPort_selection():
    #49152-65535
    ramdomEphimeralPort = random.randint(49152, 65535)
    print(ramdomEphimeralPort)
    return ramdomEphimeralPort

def get_heraclitusIP():
    return  "10.10.0.1"

def write_line_HeraclitusMapping(fileName, aristotleHash, serverIp, destPort, serverPort, heraclitusIp, heraclitusPort):
    with open(fileName, mode='a') as csv_file:
        #aristotleHash,serverIp,destPort,serverPort,heraclitusIp,heraclitusPort
        fieldnames = ['aristotleHash', 'serverIp', 'destPort', 'serverPort', 'heraclitusIp', 'heraclitusPort']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        #writer.writeheader()
        # writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
        # writer.writerow({'heraclitusPort': , 'aristotleHash': , 'serverIp': 'destPort': , 'serverPort': , 'heraclitusIp': })

        writer.writerow({'aristotleHash':aristotleHash, 'serverIp': serverIp, 'destPort': destPort,
                         'serverPort': serverPort, 'heraclitusIp': heraclitusIp,'heraclitusPort': heraclitusPort})




def menu():
    loop_condition = True
    serverList = get_csv_file("serverList.csv")
    fileName = "heraclitusMapping.csv"
    heraclitusMapping = get_csv_file(fileName)



    while loop_condition:
        print("\nWelcome to HeraclitusModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Request a new Subnet")
        print("Enter 2 Update serverList")
        print("Enter 3 Show HeraclitusMapping")
        print("Enter 4 Get HeraclitusLine by AristotleHash")
        print("Enter 5 ....")
        print("Enter 0 To exit application.")
        menu_choice = int(input("\nWhat would you like to do? \n"))


        if menu_choice == 0:
            print("\n Thanks for using the application")
            exit(0)
        elif menu_choice == 1:
            aristotleHash = input("\n Please provide the AristotleHash.")
            destPort = input("\n Please provide the destPort in decimal.")

            print("\nYour data is now saved as  aristotleHash = {}, destPort = {}. \n".format(
                aristotleHash, destPort))

            serverIp = get_serverIp_by_destPort(destPort, serverList)
            serverPort = get_ramdom_ephimeralPort_selection()
            heraclitusIp = get_heraclitusIP()
            heraclitusPort = get_ramdom_ephimeralPort_selection()
            print("\nYour data is now saved as ServerIp = {}, destPort = {}, ServerPort = {}, heraclitusIp = {}, \
            heraclitusPort = {}. \n".format( serverIp, destPort, serverPort, heraclitusIp, heraclitusPort))

            write_line_HeraclitusMapping(fileName, aristotleHash, serverIp, destPort, serverPort, heraclitusIp,
                                         heraclitusPort)
            heraclitusMapping = get_csv_file(fileName)
            get_heraclitusLine_by_aristotleHash(aristotleHash, heraclitusMapping)
            menu()

        elif menu_choice == 2:
            get_ramdom_ephimeralPort_selection()
            menu()
        elif menu_choice == 3:
            print(heraclitusMapping)
            menu()
        elif menu_choice == 4:
            aristotleHash = input("\nPlease introduce the AristotleHash of the AristotleLine you are requesting.\n")
            get_heraclitusLine_by_aristotleHash(aristotleHash, heraclitusMapping)
            menu()
        elif menu_choice == 5:
            menu()
        else:
            print("\nSorry the valid options are between 0 and 5.\n")
            menu()
menu()


