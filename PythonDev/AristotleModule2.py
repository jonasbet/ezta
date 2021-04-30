
import ipaddress
import uuid
import pandas
import random
import csv

secretHashSeed = '00010203-0405-0607-0809-0a0b0c0d0e0f'
fileName = 'aristotleMapping.csv'

#we are simulating the fist natting on the external firewall
#10.0.0.1 is the first nattable address and they will be used sequentially




def add_heraclitusIp_by_aristotleHash2(aristotleHash, heraclitusIp, df):
    #df[df.Letters == 'C'].Letters.item()
    #df.loc[df['favorite_color'] == 'yellow']
    #print (df.loc[df.name == 'george', 'age'].iat[0])

    print( df.loc[df['aristotleHash'] == aristotleHash] )
    print("This {}".format( heraclitusIp))

    #https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/
    
# importing the pandas library
#import pandas as pd
  # reading the csv file
#df = pd.read_csv("AllDetails.csv")
  # updating the column value/data
#df['Status'] = df['Status'].replace({'P': 'A'})
  # writing into the file
#df.to_csv("AllDetails.csv", index=False)
  #print(df)


def add_heraclitusIp_by_aristotleHash(aristotleHash, heraclitusIp, df):
    #df[df.Letters == 'C'].Letters.item()
    #df.loc[df['favorite_color'] == 'yellow']
    #print (df.loc[df.name == 'george', 'age'].iat[0])

    print( df.loc[df['aristotleHash'] == aristotleHash] )
    print("This {}".format( heraclitusIp))




def get_csv_file(fileName):
    df = pandas.read_csv(fileName)
    return df

def userIpInput():
    ipA = input("\n Please enter value of the fist octet in binary...")
    ipB = input("\n Please enter value of the second octet in binary...")
    ipC = input("\n Please enter value of the third octet in binary...")
    ipD = input("\n Please enter value of the fourth octet in binary...")

    ip = ipA + "." + ipB + "." + ipC + "." + ipD
    print(ipaddress.ip_address(ip))
    print("The given ip is " + ip)
    return ip


# >>> # make a UUID using an MD5 hash of a namespace UUID and a name
# >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
# UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')
def hash_creator(sourceIp, sourcePort):
    return uuid.uuid3(uuid.NAMESPACE_DNS, ( sourceIp + secretHashSeed + sourcePort))

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

def request_new_connection(sourceIp, sourcePort, destIp, destPort, nextAvailableNat1sourceIp):
    #aristotleIp is the first natting done on the external firewall.
    #this translation is done automatically on the firewall = not managed by this module
    #it will be increased sequentially just to reproduce this compexity on the module
    aristotleIp = nextAvailableNat1sourceIp
    #herclitusIp will generated on heraclitusModule at a later stage
    heraclitusIp = 'null'

    print("\nYour data is now saved as  sourceIp = {}, sourcePort = {}, destIp = {}, destPort = {}. \n".format(sourceIp, sourcePort, destIp, destPort))
    aristotleHash = hash_creator(sourceIp, sourcePort)
    print(aristotleHash)
    nat1SourceIP = nextAvailableNat1sourceIp
    print("\nYour data is now saved as    nat1SourceIP = {}, nextAvailableNat1sourceIp  = {}. \n".format(  nat1SourceIP , nextAvailableNat1sourceIp))
    print("\nWe can now pass HeraclitusModule   nat1SourceIP = {}, aristotleHash  = {}. \n".format(  nat1SourceIP , aristotleHash))
    write_line_Aristotle_Mapping(fileName, aristotleHash, sourceIp, sourcePort, destIp, aristotleIp, destPort,
                                 heraclitusIp)

#aristotleHash,sourceIp, sourcePort, destIp, aristotleIp,destPort,heraclitusIp



def menu():
    loop_condition = True
    nextAvailableNat1sourceIp = ipaddress.IPv4Address('10.0.0.1')
    aristotleMapping = get_csv_file("aristotleMapping.csv")

    while loop_condition:
        print(nextAvailableNat1sourceIp)
        print("\nWelcome to AristotleModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Request a new connection")
        print("Enter 2 Show AristotleMapping")
        print("Enter 3 Add HeraclitusIp by AristotleHash")
        print("Enter 4 Check active connections by SourceIp")
        print("Enter 5 Check active connections by SourcePort")
        print("Enter 0 To exit application.")
        menu_choice = int(input("\nWhat would you like to do? \n"))


        if menu_choice == 0:
            print("\n Thanks for using the application")
            exit(0)
        elif menu_choice == 1:
            print("\n Please provide the sourceIP in binary form octet by octet....")
            sourceIp = userIpInput()
            print("\n Please provide the dstIP in binary form octet by octet....")
            destIp = userIpInput()
            sourcePort = input("\nWhat is Source port)\n")
            destPort = input("\nWhat is Destination port)\n")
            request_new_connection(sourceIp, sourcePort, destIp, destPort, nextAvailableNat1sourceIp)
            print("\nYour data is now saved as    nextAvailableNat1sourceIp  = {}. \n".format(
                nextAvailableNat1sourceIp))
            nextAvailableNat1sourceIp = nextAvailableNat1sourceIp + 1

            menu()

        elif menu_choice == 2:
            print(aristotleMapping)
            menu()
        elif menu_choice == 3:
            aristotleHash = input("\nWhat is AristotleHash you want to update?)\n")
            heraclitusIp = input("\nWhat is HeraclitusIp you want to add to the Aristotle hash {}?)\n".format(aristotleHash))
            add_heraclitusIp_by_aristotleHash(aristotleHash, heraclitusIp, aristotleMapping)

            menu()
        elif menu_choice == 4:
            aristotleHash = input("\nWhat is AristotleHash you want to update?)\n")
            heraclitusIp = input("\nWhat is HeraclitusIp you want to add to the Aristotle hash {}?)\n".format(aristotleHash))
            add_heraclitusIp_by_aristotleHash2(aristotleHash, heraclitusIp, aristotleMapping)

            menu()
        elif menu_choice == 5:

            menu()
        else:
            print("\nSorry the valid options are between 0 and 5.\n")
            menu()
menu()


