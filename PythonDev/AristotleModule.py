
import ipaddress
import uuid

secretHashSeed = '00010203-0405-0607-0809-0a0b0c0d0e0f'
nextAvailableNat1sourceIp = "10.0.0.1"


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

def request_new_connection(sourceIp, sourcePort, destIp, destPort, nextAvailableNat1sourceIp):
    print("\nYour data is now saved as  sourceIp = {}, sourcePort = {}, destIp = {}, destPort = {}. \n".format(sourceIp, sourcePort, destIp, destPort))
    AristotleHash = hash_creator(sourceIp, sourcePort)
    print(AristotleHash)
    nat1SourceIP = nextAvailableNat1sourceIp
    nextAvailableNat1sourceIp += nextAvailableNat1sourceIp
    print("\nYour data is now saved as    nat1SourceIP = {}, nextAvailableNat1sourceIp  = {}. \n".format(  nat1SourceIP , nextAvailableNat1sourceIp))
    print("\nWe can now pass HeraclitusModule   nat1SourceIP = {}, AristotleHash  = {}. \n".format(  nat1SourceIP , AristotleHash))


def menu():
    loop_condition = True

    while loop_condition:
        print("\nWelcome to AristotleModule\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Request a new connection")
        print("Enter 2 Show AristotleMapping")
        print("Enter 3 Check active connections by SourcePort")
        print("Enter 4 Check active connections by SourceIP")
        print("Enter 5 ....")
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
            sourcePort = input("\nWhat is source port)\n")
            destPort = input("\nWhat is source port)\n")
            request_new_connection(sourceIp, sourcePort, destIp, destPort)
            print("\nYour data is now saved as    nextAvailableNat1sourceIp  = {}. \n".format(
                nextAvailableNat1sourceIp))
            menu()

        elif menu_choice == 2:
# using 2 for testing
            print(hash_creator())
            menu()
        elif menu_choice == 3:
            sourcePort = input("\nWhat is source port)\n")
            destPort = input("\nWhat is source port)\n")
            print("\nYour data is now saved as  sourceIp = {}, sourcePort = {}\n".format(sourcePort, destPort))

            menu()
        elif menu_choice == 4:

            menu()
        elif menu_choice == 5:

            menu()
        else:
            print("\nSorry the valid options are between 0 and 5.\n")
            menu()
menu()


