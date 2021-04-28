
import requests
import json
import collections
import ipaddress




def userIpInput():
    ipA = input("\n Please enter value of the fist octet in binary...")
    ipB = input("\n Please enter value of the second octet in binary...")
    ipC = input("\n Please enter value of the third octet in binary...")
    ipD = input("\n Please enter value of the fourth octet in binary...")

    ip = ipA + "." + ipB + "." + ipC + "." + ipD
    print("The given ip is " + ip)
    return ip

def request_new_connection(sourceIp, sourcePort, destPort):


    print("\n The results of the scan will be shortly available on the link below: ")



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
            print("\n Please provide the sourceIP in binary form octet by octet....")
            destIp = userIpInput()
            sourcePort = input("\nWhat is source port)\n")
            destPort = input("\nWhat is source port)\n")
            request_new_connection(sourceIp, sourcePort, destIp, destPort)
            menu()
        elif menu_choice == 2:

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


