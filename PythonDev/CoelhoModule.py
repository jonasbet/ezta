
import pandas
import csv

def get_SDN_orchestration_by_aristotleHash(aristotleHash, aristotleCoelhoMapping, heraclitoCoelhoMapping):
    sourceIp = aristotleCoelhoMapping.loc[aristotleCoelhoMapping['aristotleHash'] == aristotleHash, 'sourceIp'].iat[0]
    sourcePort = str(aristotleCoelhoMapping.loc[aristotleCoelhoMapping['aristotleHash'] == aristotleHash, 'sourcePort'].iat[0])
    destIp = aristotleCoelhoMapping.loc[aristotleCoelhoMapping['aristotleHash'] == aristotleHash, 'destIp'].iat[0]
    aristotleIp = aristotleCoelhoMapping.loc[aristotleCoelhoMapping['aristotleHash'] == aristotleHash, 'aristotleIp'].iat[0]
    serverIp = heraclitoCoelhoMapping.loc[heraclitoCoelhoMapping['aristotleHash'] == aristotleHash, 'serverIp'].iat[0]
    destPort = str(heraclitoCoelhoMapping.loc[heraclitoCoelhoMapping['aristotleHash'] == aristotleHash, 'destPort'].iat[0])
    serverPort = str(heraclitoCoelhoMapping.loc[heraclitoCoelhoMapping['aristotleHash'] == aristotleHash, 'serverPort'].iat[0])
    heraclitusIp = heraclitoCoelhoMapping.loc[heraclitoCoelhoMapping['aristotleHash'] == aristotleHash, 'heraclitusIp'].iat[0]
    heraclitusPort = str(heraclitoCoelhoMapping.loc[heraclitoCoelhoMapping['aristotleHash'] == aristotleHash, 'heraclitusPort'].iat[0])
    print("\n \n EndToEnd connection information for AristotleHash: {} .................    \n".format(aristotleHash))
    print("ZoneOne: makes a request from SourceIp:{}, SourcePort:{}      ".format(sourceIp, sourcePort))
    print("ZoneTwo: receives the request on DestIp:{}, DestPort:{} ".format(destIp, destPort))
    print("AristotleModule is the only ones that know the SourceIp of ZoneOne and NATs it into AristotleIp:{}".format(aristotleIp))
    print("AristotleModule does not know the ServerIp but uses HeraclitusIp:{}  to get to the server.   \n".format(heraclitusIp))
    print("AristotleModule does not know the ServerPort but is uses the original destPort:{} to communicate with the server".format(destPort))
    print("HeraclitusModule is only one that know the Server:Ip {} and the ServerPort:{}      ".format(serverIp, serverPort))
    print("HeraclitusModule nats the serverPort with HeraclitusPort: {}      ".format(heraclitusPort))
    print("...and no-one has the full information about this dynamic self-allocated subnetting that enables this end-to-end connection ".format())
    print("\n EndToEnd connection information for AristotleHash: {} .................    \n".format(aristotleHash))

def import_aristotleLine(aristotleLine, df, fileName):
    # aristotleLineSamle
    #94dc03bf-2d4f-378a-a8ac-9e5f76ee3850#7.7.7.7#8010.0.0.110.0.0.1#80.80.80.80#10.0.0.1#10.0.0.1#10.0.0.1
    #'aristotleHash','sourceIp', 'sourcePort', 'destIp', 'aristotleIp','destPort','heraclitusIp'
    # aristotleHash,sourceIp,sourcePort,destIp,aristotleIp,destPort,heraclitusIp
    print(df)
    aristotleHash,sourceIp,sourcePort,destIp,aristotleIp,destPort,heraclitusIp = aristotleLine.split('#')
    oneLineExport = aristotleHash + '#' + sourceIp + '#' + sourcePort +\
    aristotleIp + '#' + destIp + '#' + aristotleIp + '#' + destPort + '#' + heraclitusIp
    print(oneLineExport)
    write_line_Aristotle_Mapping(fileName, aristotleHash, sourceIp, sourcePort, destIp, aristotleIp, destPort,
                                 heraclitusIp)


def import_HeraclitusLine(heraclitusLine, df, fileName):
    print(df)
    #'aristotleHash','sourceIp', 'sourcePort', 'destIp', 'aristotleIp','destPort','heraclitusIp'
    # aristotleHash,serverIp,destPort,serverPort,heraclitusIp,heraclitusPort
    # 94dc03bf-2d4f-378a-a8ac-9e5f76ee3850#10.1.0.1#80#54319#10.10.0.1#64263
    aristotleHash,serverIp,destPort,serverPort,heraclitusIp,heraclitusPort = heraclitusLine.split('#')
    oneLineExport = aristotleHash + '#' + serverIp + '#' + destPort + '#' +\
    serverPort + '#' + heraclitusIp  +   '#' +  heraclitusPort
    print( oneLineExport )
    write_line_HeraclitusMapping(fileName, aristotleHash, serverIp, destPort, serverPort, heraclitusIp, heraclitusPort)


def get_csv_file(fileName):
    df = pandas.read_csv(fileName)
    return df

def write_line_Aristotle_Mapping(fileName,aristotleHash,sourceIp, sourcePort, destIp, aristotleIp,destPort,heraclitusIp):
    with open(fileName, mode='a') as csv_file:
        #aristotleHash,serverIp,destPort,serverPort,heraclitusIp,heraclitusPort
        fieldnames = ['aristotleHash','sourceIp', 'sourcePort', 'destIp', 'aristotleIp','destPort','heraclitusIp']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        #writer.writeheader()
        # writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
        # writer.writerow({'heraclitusPort': , 'aristotleHash': , 'serverIp': 'destPort': , 'serverPort': , 'heraclitusIp': })

        writer.writerow({'aristotleHash': aristotleHash,'sourceIp': sourceIp, 'sourcePort':sourcePort,'destIp': destIp,
                         'aristotleIp':aristotleIp, 'destPort': destPort, 'heraclitusIp' : heraclitusIp})

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
    aristotleFileName = "coelhoAristotleMapping.csv"
    heraclitoFileName = "coelhoHeraclitoMapping.csv"
    aristotleCoelhoMapping = get_csv_file(aristotleFileName)
    heraclitoCoelhoMapping = get_csv_file(heraclitoFileName)



    while loop_condition:
        print("\nWelcome to CoelhoModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Input an AristotleLine")
        print("Enter 2 Input a HeraclitusLine")
        print("Enter 3 Show AristotleCoelhoMapping")
        print("Enter 4 Show HeraclitoCoehloMapping")
        print("Enter 5 Show full orchestration by AristotleHash")
        print("Enter 0 To exit application.")
        menu_choice = int(input("\nWhat would you like to do? \n"))


        if menu_choice == 0:
            print("\n Thanks for using the application")
            exit(0)

        elif menu_choice == 1:
            aristotleLine = input("Please provide the AristotleLine you want to import.")
            import_aristotleLine(aristotleLine, aristotleCoelhoMapping, aristotleFileName)
            menu()
        elif menu_choice == 2:
            heraclitoLine = input("Please provide the HeraclitoLine you want to import.")
            import_HeraclitusLine(heraclitoLine, heraclitoCoelhoMapping, heraclitoFileName)
            menu()
        elif menu_choice == 3:
            print(aristotleCoelhoMapping)
            menu()
        elif menu_choice == 4:
            print(heraclitoCoelhoMapping)
            menu()
        elif menu_choice == 5:
            aristotleHash = input("Please provide the AristotleHash you want to orchestrate.")
            get_SDN_orchestration_by_aristotleHash(aristotleHash, aristotleCoelhoMapping, heraclitoCoelhoMapping)
            menu()
        else:
            print("\nSorry the valid options are between 0 and 5.\n")
            menu()
menu()


