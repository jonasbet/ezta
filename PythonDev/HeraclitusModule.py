
import requests
import json
import pefile
import collections


apiKey = '9764fe688d488ba54b314d34bdd1530603d5b2499502df1399165e7fe55a78f0'


# takes the json object to save and ask the user for a file name to save the file on
# the local path
def save_json(json_file):
    fileName = input("\nWhat is the name for the new json file where to save this information?  \
                     \n(Don't worry about the file extension I will not forget to add it.)\n") + ".json"
    with open(fileName, 'w') as outfile:
        json.dump(json_file, outfile)
    print("\nYour data is now saved as %s. \n" % fileName)

# https://developers.virustotal.com/reference#file-scan
# This endpoint allows you to send a file for scanning with VirusTotal.
def scan_file(path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey':  apiKey }
    files = {'file': (path, open(path, 'rb'))}
    response = requests.post(url, files=files, params=params).json()
    print("\n The results of the scan will be shortly available on the link below: ")
    print(json.dumps(response['permalink'], indent=4))

# https://developers.virustotal.com/reference#file-report
# The resource argument can be the MD5, SHA-1 or SHA-256 of a file for which
# you want to retrieve the most recent antivirus report.
# 99017f6eebbac24f351415dd410d522d hash example
def get_file_report(hash):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': apiKey, 'resource': hash}
    response = requests.post(url, data=params).json()
    save_json(response)
    # uncomment if display to user needed
    # print(json.dumps(response, indent=4))

# https://developers.virustotal.com/reference#url-scan
# url -> The URL that should be scanned
def upload_url(url):
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': apiKey, 'url': url}
    response = requests.post(url, data=params).json()
    print("\n Your report is available on the link below: ")
    print(json.dumps(response['permalink'], indent=4))

#  https://developers.virustotal.com/reference#url-report
#  The resource argument must be the URL for which you want to retrieve the most recent report.
def get_url_report(url):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': apiKey, 'resource': url}
    response = requests.post(url, params=params).json()
    save_json(response)
    # uncomment if display to user needed
    # print(json.dumps(response, indent=4))


def report_stats(filename, detected, description, stats):

    if( detected == 1):
        detected = True
    else:
        detected = False

    if(description == 1):
        description = True
    else:
        description = False

    if(stats == 1):
        stats = True
    else:
        stats = False


    with open(filename, 'r') as f:
        data_scan = json.load(f)

        if detected:
            print("\n Detected malware: ")
            for key, value in data_scan["scans"].items():
                if(value["detected"]):
                    print("\n Malware: %s. \n" % key)
                    if description:
                        print(value, "\n")
        else:
            print("\n Not detected malware: ")
            for key, value in data_scan["scans"].items():
                if(value["detected"]):
                    print("\n Malware not detected: %s. \n" % key)
                    if description:
                        print(value, "\n")

        if(stats):
            malware_type_list = []
            for key, value in data_scan["scans"].items():
                if(value["detected"] == True and data_scan["scans"][key]["result"].lower() not in ('', 'empty', "null")):
                    malware_type_list.append(data_scan["scans"][key]["result"])
            print(print(collections.Counter(malware_type_list).most_common()))




def menu():
    loop_condition = True
    while loop_condition:
        print("\nWelcome to Python Security Tool\n")
        print("\nPlease enter a number for what you want to do.\n")
        print("Enter 1 Scan file")
        print("Enter 2 Get file report")
        print("Enter 3 Upload URL")
        print("Enter 4 Get URL report")
        print("Enter 5 Report stats")
        print("Enter 0 To exit application.")
        menu_choice = int(input("\nWhat would you like to do? \n"))


        if menu_choice == 0:
            print("\n Thanks for using the application")
            exit(0)
        elif menu_choice == 1:
            path = input("\nWhat is the name of the file? \
                           \n(Remenber I am only allow to read files that are on the local folder of this app.)\n")
            scan_file(path)
            menu()
        elif menu_choice == 2:
            hash = input("\nWhat is the hash to analyse? \n")
            get_file_report(hash)
            menu()
        elif menu_choice == 3:
            url = input("\nwhat is the Url?\n")
            upload_url(url)
            menu()
        elif menu_choice == 4:
            url = input("\nwhat is the Url?\n")
            get_url_report(url)
            menu()
        elif menu_choice == 5:
            json_path = input("\nWhat is the path to the json file? \n")
            detected = int(input("\n Press 1 to show detected malware or any key to show the not detected malware. \n"))
            description = int(input("\n Press 1 to include the malware description or any key to omit it. \n"))
            stats = int(input("\n Press 1 to include statistics of detected malwary or any key to omit it. \n"))

            report_stats(json_path, detected, description, stats)
            menu()
        else:
            print("\nSorry the valid options are between 0 and 5.\n")
            menu()
menu()


