import ipaddress
import pandas
import random
import csv

def get_heraclitusLine_by_aristotleHash(aristotleHash, df):
    serverIp = df.loc[df['aristotleHash']== aristotleHash, 'serverIp'].iat[0]
    serverPort = str(df.loc[df['aristotleHash']== aristotleHash, 'serverPort'].iat[0])
    heraclitusIp = df.loc[df['aristotleHash']== aristotleHash, 'heraclitusIp'].iat[0]
    heraclitusPort = str(df.loc[df['aristotleHash']== aristotleHash, 'heraclitusPort'].iat[0])
    oneLineExport = aristotleHash + '#' + serverIp + '#'  +\
    serverPort + '#' + heraclitusIp  +   '#' +  heraclitusPort
    return( oneLineExport )

def get_csv_file(fileName):
    df = pandas.read_csv(fileName)
    return df

def get_serverIp_by_destPort(destPort, df):
    serverIp = df.loc[df['destPort']== int(destPort), 'serverIp'].iat[0]
    return serverIp

def get_ramdom_ephimeralPort_selection():
    ramdomEphimeralPort = random.randint(49152, 65535)
    return ramdomEphimeralPort

def get_next_HeraclitusIp(df, fileName):
    heraclitusIp = ipaddress.ip_address(df.loc[df['controlDigit']==0,'ip'].iat[0])
    nextHeraclitusIp = heraclitusIp + 4
    with open(fileName, mode='w') as csv_file:
        fieldnames = ['ip', 'controlDigit']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'ip': nextHeraclitusIp, 'controlDigit': 0})
    return  heraclitusIp

def write_line_HeraclitusMapping(fileName, aristotleHash, serverIp, destPort, serverPort, heraclitusIp, heraclitusPort):
    with open(fileName, mode='a') as csv_file:
        #aristotleHash,serverIp,destPort,serverPort,heraclitusIp,heraclitusPort
        fieldnames = ['aristotleHash', 'serverIp', 'destPort', 'serverPort', 'heraclitusIp', 'heraclitusPort']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'aristotleHash':aristotleHash, 'serverIp': serverIp, 'destPort': destPort,
                         'serverPort': serverPort, 'heraclitusIp': heraclitusIp,'heraclitusPort': heraclitusPort})

def menu():
    loop_condition = True
    fileNameMapping = "heraclitusMapping.csv"
    fileNameServerList = "serverList.csv"
    fileNameNextHeraclitusIp = 'nextHeraclitusIp.csv'
    heraclitusMapping = get_csv_file(fileNameMapping)
    serverList = get_csv_file( fileNameServerList)
    heraclitusIpDf = get_csv_file(fileNameNextHeraclitusIp)


    while loop_condition:
        print("\nWelcome to HeraclitusModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Request a new Subnet")
        print("Enter 2 Update serverList")
        print("Enter 3 Show HeraclitusMapping")
        print("Enter 4 Get HeraclitusLine by AristotleHash")
        print("Enter 0 To exit application.")
        menu_choice = int(input("\nWhat would you like to do? \n"))
        if menu_choice == 0:
            print("\n Thanks for using the application")
            exit(0)
        elif menu_choice == 1:
            aristotleOnHeraclitusInput = input("\n Please provide the information given by the AristotleModule.\n")
            aristotleHash, destPort = aristotleOnHeraclitusInput.split('#')
            serverIp = get_serverIp_by_destPort(destPort, serverList)
            serverPort = get_ramdom_ephimeralPort_selection()
            heraclitusIp =  get_next_HeraclitusIp(heraclitusIpDf, fileNameNextHeraclitusIp)
            heraclitusPort = get_ramdom_ephimeralPort_selection()
            write_line_HeraclitusMapping(fileNameMapping, aristotleHash, serverIp, destPort, serverPort, heraclitusIp,
                                         heraclitusPort)
            heraclitusMapping = get_csv_file(fileNameMapping)
            print("\nYour data is now saved as ServerIp = {}, destPort = {}, ServerPort = {}, heraclitusIp = {}, "
                  "heraclitusPort = {}. \n".format( serverIp, destPort, serverPort, heraclitusIp, heraclitusPort))
            print("\n Pass the following to AristotleModule to make them aware of the new HeraclitusIp (opt3):"
                  " \n {}#{} \n  \nAfterwards come back to HeraclitusModule to get HeraclitusLine (opt4)\n"
                  "".format(aristotleHash, heraclitusIp))
            menu()

        elif menu_choice == 2:
            get_ramdom_ephimeralPort_selection()
            menu()

        elif menu_choice == 3:
            print(heraclitusMapping)
            menu()

        elif menu_choice == 4:
            aristotleHash = input("\nPlease introduce the AristotleHash of the AristotleLine you are requesting.\n")
            heraclitusLine = get_heraclitusLine_by_aristotleHash(aristotleHash, heraclitusMapping)
            print("\nPlease input the following line on CoelhoModule (opt2): \n{}\n".format(heraclitusLine))
            menu()

        else:
            print("\nSorry the valid options are between 0 and 4.\n")
            menu()
menu()


