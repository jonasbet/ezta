
import pandas
import csv





def import_aristotleLine(aristotleLine, df):
    #'aristotleHash','sourceIp', 'sourcePort', 'destIp', 'aristotleIp','destPort','heraclitusIp'
    # aristotleHash,sourceIp,sourcePort,destIp,aristotleIp,destPort,heraclitusIp
    print(df)
    aristotleHash,sourceIp,sourcePort,destIp,aristotleIp,destPort,heraclitusIp = aristotleLine.split('#')
    oneLineExport = aristotleHash + '#' + sourceIp + '#' + sourcePort +\
    aristotleIp + '#' + destIp + '#' + aristotleIp + '#' + destPort + '#' + heraclitusIp
    print(oneLineExport)

def not_expected_to_be_used(df):
    aristotleHash = 0
    sourceIp = df.loc[df['aristotleHash'] == aristotleHash, 'sourceIp'].iat[0]
    sourcePort = str(df.loc[df['aristotleHash'] == aristotleHash, 'sourcePort'].iat[0])
    destIp = df.loc[df['aristotleHash'] == aristotleHash, 'destIp'].iat[0]
    aristotleIp = df.loc[df['aristotleHash'] == aristotleHash, 'aristotleIp'].iat[0]
    destPort = df.loc[df['aristotleHash'] == aristotleHash, 'aristotleIp'].iat[0]
    heraclitusIp = df.loc[df['aristotleHash'] == aristotleHash, 'aristotleIp'].iat[0]



def import_HeraclitusLine(heraclitusLine, df):
    print(df)
    #'aristotleHash','sourceIp', 'sourcePort', 'destIp', 'aristotleIp','destPort','heraclitusIp'
    # aristotleHash,serverIp,destPort,serverPort,heraclitusIp,heraclitusPort
    aristotleHash = 0
    serverIp = df.loc[df['aristotleHash']== aristotleHash, 'serverIp'].iat[0]
    destPort = str(df.loc[df['aristotleHash'] == aristotleHash, 'destPort'].iat[0])
    serverPort = str(df.loc[df['aristotleHash']== aristotleHash, 'serverPort'].iat[0])
    heraclitusIp = df.loc[df['aristotleHash']== aristotleHash, 'heraclitusIp'].iat[0]
    heraclitusPort = str(df.loc[df['aristotleHash']== aristotleHash, 'heraclitusPort'].iat[0])



def get_csv_file(fileName):
    df = pandas.read_csv(fileName)
    return df


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
    heraclitusFileName = "coelhoHeraclitusMapping.csv"
    coelhoAristotleMapping = get_csv_file(aristotleFileName)



    while loop_condition:
        print("\nWelcome to CoelhoModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Input an AristotleLine")
        print("Enter 2 Input a HeraclitusLine")
        print("Enter 3 Show CoelhoMapping")
        print("Enter 4 .....")
        print("Enter 5 ....")
        print("Enter 0 To exit application.")
        menu_choice = int(input("\nWhat would you like to do? \n"))


        if menu_choice == 0:
            print("\n Thanks for using the application")
            exit(0)

        elif menu_choice == 1:
            aristotleLine = input("Please provide AristotleLine you want to import.")
            import_aristotleLine(aristotleLine, coelhoMapping)
            menu()

        elif menu_choice == 2:
            menu()
        elif menu_choice == 3:
            print(coelhoMapping)
            menu()
        elif menu_choice == 4:
            menu()
        elif menu_choice == 5:
            menu()
        else:
            print("\nSorry the valid options are between 0 and 5.\n")
            menu()
menu()


