
import ipaddress
import uuid
import pandas
import csv

secretHashSeed = '00010203-0405-0607-0809-0a0b0c0d0e0f'
fileName = 'aristotleMapping.csv'
fileNameAristotleIp = 'nextAristotleIp.csv'

def get_aristotleLine_by_aristotleHash(aristotleHash, df):
    #aristotleLine sample
    # 94dc03bf-2d4f-378a-a8ac-9e5f76ee3850#7.7.7.7#8010.0.0.1#80.80.80.80#10.0.0.1#10.0.0.1#10.0.0.1
    #'aristotleHash','sourceIp', 'sourcePort', 'destIp', 'aristotleIp','destPort','heraclitusIp'
    # aristotleHash,sourceIp,sourcePort,destIp,aristotleIp,destPort,heraclitusIp
    sourceIp = df.loc[df['aristotleHash']== aristotleHash, 'sourceIp'].iat[0]
    sourcePort = str(df.loc[df['aristotleHash']== aristotleHash, 'sourcePort'].iat[0])
    destIp = df.loc[df['aristotleHash']== aristotleHash, 'destIp'].iat[0]
    aristotleIp = df.loc[df['aristotleHash']== aristotleHash, 'aristotleIp'].iat[0]
    destPort = str(df.loc[df['aristotleHash']== aristotleHash, 'destPort'].iat[0])
    heraclitusIp = df.loc[df['aristotleHash']== aristotleHash, 'heraclitusIp'].iat[0]
    oneLineExport = aristotleHash + '#' + sourceIp + '#' + sourcePort + '#' +\
    destIp + '#' + aristotleIp + '#' + destPort + '#' + heraclitusIp
    print(oneLineExport)

def add_heraclitusIp_by_aristotleHash( aristotleHash, heraclitusIp, df):
    print( df.loc[df['aristotleHash'] == aristotleHash] )
    print("This is the heraclitusIp{}".format( heraclitusIp))
    print("This is the aristotleHash {}".format(aristotleHash))
    df['heraclitusIp'] = df['heraclitusIp'].replace({aristotleHash: heraclitusIp})
    print( df.loc[df['aristotleHash'] == aristotleHash] )
    df.to_csv(fileName, index=False)
    get_aristotleLine_by_aristotleHash(aristotleHash, df)

def get_csv_file(fileName):
    df = pandas.read_csv(fileName)
    return df

def userIpInput():
    ipA = input("\n Please enter value of the fist octet (decimal values are expected)...")
    ipB = input("\n Please enter value of the second octet (decimal values are expected)...")
    ipC = input("\n Please enter value of the third octet (decimal values are expected)...")
    ipD = input("\n Please enter value of the fourth (decimal values are expected)...")

    ip = ipA + "." + ipB + "." + ipC + "." + ipD
   # print(ipaddress.ip_address(ip))
    print("The given ip is " + ip)
    return ip


# >>> # make a UUID using an MD5 hash of a namespace UUID and a name
# >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
# UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')
def hash_creator(sourceIp, sourcePort):
    return uuid.uuid3(uuid.NAMESPACE_DNS, ( sourceIp + secretHashSeed + sourcePort))

def write_line_Aristotle_Mapping(fileName,aristotleHash,sourceIp, sourcePort, destIp, aristotleIp,
                                 destPort,heraclitusIp):
    with open(fileName, mode='a') as csv_file:
        #aristotleHash,serverIp,destPort,serverPort,heraclitusIp,heraclitusPort
        fieldnames = ['aristotleHash','sourceIp', 'sourcePort', 'destIp', 'aristotleIp','destPort','heraclitusIp']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'aristotleHash': aristotleHash,'sourceIp': sourceIp, 'sourcePort':sourcePort,'destIp': destIp,
                         'aristotleIp':aristotleIp, 'destPort': destPort, 'heraclitusIp' : heraclitusIp})

def get_ramdom_aristotleIp(df,fileName):

    aristotleIp = ipaddress.ip_address(df.loc[df['controlDigit']==0,'ip'].iat[0])
    nextAristotleIp = aristotleIp + 4
    print(nextAristotleIp)
    with open(fileName, mode='w') as csv_file:
        fieldnames = ['ip', 'controlDigit']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'ip': nextAristotleIp, 'controlDigit': 0})
    return aristotleIp

def request_new_connection(sourceIp, sourcePort, destIp, destPort, df, fileNameAristotleIp, fileNameAristotleMapping):
    #aristotleIp is the first natting done on the external firewall.
    #this translation is done automatically on the firewall = not managed by this module
    #it will be increased sequentially just to reproduce this compexity on the module
    aristotleIp = get_ramdom_aristotleIp(df, fileNameAristotleIp)
    print("\nYour data is now saved as  sourceIp = {}, sourcePort = {}, destIp = {}, destPort = {} and \
    AristotleIp = {}. \n".format(sourceIp, sourcePort, destIp, destPort, aristotleIp))
    aristotleHash = hash_creator(sourceIp, sourcePort)
    print("\nPlease input the aristotleHash = {} and destPort = {} on the HeraclitusModule. \n".format(
        aristotleHash, destPort))
    # herclitusIp will generated on heraclitusModule at a later stage
    # so far we use the uniquesness of aristotleHash to make the change for heraclitusIp later as the
    # value is received from heraclitusModule
    heraclitusIp = aristotleHash
    write_line_Aristotle_Mapping(fileNameAristotleMapping, aristotleHash, sourceIp, sourcePort, destIp, aristotleIp,
                                 destPort, heraclitusIp)

def menu():
    loop_condition = True
    aristotleMapping = get_csv_file("aristotleMapping.csv")
    nextAristotleIpDf = get_csv_file("nextAristotleIp.csv")

    while loop_condition:

        print("\nWelcome to AristotleModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Request a new connection")
        print("Enter 2 Show AristotleMapping")
        print("Enter 3 Add HeraclitusIp by AristotleHash")
        print("Enter 4 Check active connections by SourceIp")
        print("Enter 5 Check active connections by SourcePort")
        print("Enter 6 Get AristotleLine by AristotleHash")
        print("Enter 0 To exit application.")
        menu_choice = int(input("\nWhat would you like to do? \n"))

        if menu_choice == 0:
            print("\n Thanks for using the application")
            exit(0)
        elif menu_choice == 1:
            print("\n Please provide the sourceIP in decimal (octet by octet)....")
            sourceIp = userIpInput()
            print("\n Please provide the dstIP in decimal...")
            destIp = userIpInput()
            sourcePort = input("\nWhat is Source port)\n")
            destPort = input("\nWhat is Destination port)\n")
            request_new_connection(sourceIp, sourcePort, destIp, destPort, nextAristotleIpDf,
                                   fileNameAristotleIp, fileName)
            menu()

        elif menu_choice == 2:
            print(aristotleMapping)
            menu()

        elif menu_choice == 3:
            aristotleHash = input("\nWhat is AristotleHash you want to update?)\n")
            heraclitusIp = input("\nWhat is HeraclitusIp you want to add to the Aristotle hash {}?)"
                                 "\n".format(aristotleHash))
            add_heraclitusIp_by_aristotleHash( aristotleHash, heraclitusIp, aristotleMapping)
            menu()

        elif menu_choice == 4:
            menu()

        elif menu_choice == 5:
            menu()

        elif menu_choice == 6:
            aristotleHash = input("\nPlease introduce the AristotleHash of the AristotleLine you are requesting.\n")
            get_aristotleLine_by_aristotleHash(aristotleHash, aristotleMapping)
            menu()

        else:
            print("\nSorry the valid options are between 0 and 6.\n")
            menu()
menu()


