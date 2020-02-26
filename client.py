import requests
import csv
import datetime
from lxml import etree
import lxml.html
import sys
import time

# My username and password for booking
username = "3oo112"
password = "Ruv2Hu"
# Headers to be used with all requests
headers = {'Content-Type': 'application/xml',
           'Accept': 'application/xml'}



# 0:
# Function to exit the program cleanly
def exit_program():
    print("===============================================")
    print("Exiting Program...")
    print("===============================================")
    sys.exit()



# 1:
# Function to check band availibility and return the results
def check_band_availibility():
    print("===============================================")
    print("Available slots for the band...")
    print("===============================================")
    # Get the current time to use as a request id
    time_id = str(datetime.datetime.now())
    # URL and xml string for finding availibility
    url = 'http://jewel.cs.man.ac.uk:3020/booking/available'
    availibility_xml = ("<availibility><request_id>"
                        + time_id + "</request_id><username>"
                        + username + "</username><password>"
                        + password + "</password></availibility>")
    # Use request to retrieve the html and convert this to text to be parsed
    x = requests.put(url, data = availibility_xml, headers = headers)
    x = (x.text)
    # Parse the string and iterate over each row and print the values
    table = etree.HTML(x).find("body/table")
    rows = iter(table)
    for row in rows:
        values = [col.text for col in row]
        print('\n'.join(values))
    print("===============================================")
    main()



# 2:
# Function to check hotel availibility and return the results
def check_hotel_availibility():
    print("===============================================")
    print("Available slots for the hotel...")
    print("===============================================")
    # Get the current time to use as a request id
    time_id = str(datetime.datetime.now())
    # URL and xml string for finding availibility
    url = 'http://jewel.cs.man.ac.uk:3010/booking/available'
    availibility_xml = ("<availibility><request_id>"
                        + time_id + "</request_id><username>"
                        + username + "</username><password>"
                        + password + "</password></availibility>")
    # Use request to retrieve the html and convert this to text to be parsed
    x = requests.put(url, data = availibility_xml, headers = headers)
    x = (x.text)
    # Parse the string and iterate over each row and print the values
    table = etree.HTML(x).find("body/table")
    rows = iter(table)
    for row in rows:
        values = [col.text for col in row]
        print('\n'.join(values))
    print("===============================================")
    main()



# 3:
# Function to reserve a band slot
def reserve_band_slot():
    print("===============================================")
    print("Reserve a band slot...")
    print("===============================================")
    slot_id = str(input("Enter a slot to reserve: "))
    # Get the current time to use as a request id
    time_id = str(datetime.datetime.now())
    # URL and xml string for finding availibility
    url = 'http://jewel.cs.man.ac.uk:3020/queue/enqueue'
    reserve_xml = ("<reserve><request_id>"
                        + time_id + "</request_id><username>"
                        + username + "</username><password>"
                        + password + "</password><slot_id>"
                        + slot_id + "</slot_id></reserve>")
    # Use request to retrieve the html and convert this to text to be parsed
    x = requests.put(url, data = reserve_xml, headers = headers)
    x = (x.text)
    # Remove the xml tags around the url and concatenate with username/password
    x = x[9:-10]
    url = x + "?username=3oo112&password=Ruv2Hu"
    # Make a new request with the above url to retrieve the message
    x = requests.get(url)
    x = x.text
    # If the server is unavailable wait for 2 seconds and make a new request
    print("Waiting for the server to respond...")
    while (x == "Message unavailable" or x == "Service unavailable"):
        time.sleep(2)
        x = requests.get(url)
        x = x.text
        print("...")
    # Remove the tags around the message to display to the user
    if "<code>200</code>" in x:
        x = x[41:-28]
    else:
        x = x[32:-18]
    print(x)
    print("===============================================")
    main()



# 4:
# Function to reserve a hotel slot
def reserve_hotel_slot():
    print("===============================================")
    print("Reserve a hotel slot...")
    print("===============================================")
    slot_id = str(input("Enter a slot to reserve: "))
    # Get the current time to use as a request id
    time_id = str(datetime.datetime.now())
    # URL and xml string for finding availibility
    url = 'http://jewel.cs.man.ac.uk:3010/queue/enqueue'
    reserve_xml = ("<reserve><request_id>"
                        + time_id + "</request_id><username>"
                        + username + "</username><password>"
                        + password + "</password><slot_id>"
                        + slot_id + "</slot_id></reserve>")
    # Use request to retrieve the html and convert this to text to be parsed
    x = requests.put(url, data = reserve_xml, headers = headers)
    x = (x.text)
    # Remove the xml tags around the url and concatenate with username/password
    x = x[9:-10]
    url = x + "?username=3oo112&password=Ruv2Hu"
    # Make a new request with the above url to retrieve the message
    x = requests.get(url)
    x = x.text
    # If the server is unavailable wait for 2 seconds and make a new request
    print("Waiting for the server to respond...")
    while (x == "Message unavailable" or x == "Service unavailable"):
        time.sleep(2)
        x = requests.get(url)
        x = x.text
        print("...")
    # Remove the tags around the message to display to the user
    if "<code>200</code>" in x:
        x = x[41:-28]
    else:
        x = x[32:-18]
    print(x)
    print("===============================================")
    main()



# 5:
# Function to check your bookings for band
def check_band_booking():
    print("===============================================")
    print("Your current band bookings...")
    print("===============================================")
    # Get the current time to use as a request id
    time_id = str(datetime.datetime.now())
    # URL and xml string for finding availibility
    original_url = 'http://jewel.cs.man.ac.uk:3020/booking?page='
    booking_xml = ("<bookings><request_id>"
                        + time_id + "</request_id><username>"
                        + username + "</username><password>"
                        + password + "</password></bookings>")
    # Change the output if no slots are booked
    numberOfSlots = 0
    #Repeat for the 4 pages of slots
    for i in range(1, 5):
        url = original_url + str(i)
        # Use request to retrieve the html and convert this to text to be parsed
        x = requests.put(url, data = booking_xml, headers = headers)
        x = (x.text)
        # Parse the string and iterate over each row and print the values
        table = etree.HTML(x).find("body/table")
        rows = iter(table)
        for row in rows:
            values = [col.text for col in row]
            # If the username if found in the list of values print out the slot id
            if " 3oo112 " in values:
                numberOfSlots += 1
                print("You have reserved slot:" + values[0])
    # Message displayed if no bookings are held
    if (numberOfSlots == 0):
        print("You don't currently hold any band slots")
    print("===============================================")
    main()



# 6:
# Function to check your bookings for hotel
def check_hotel_booking():
    print("===============================================")
    print("Your current hotel bookings...")
    print("===============================================")
    # Get the current time to use as a request id
    time_id = str(datetime.datetime.now())
    # URL and xml string for finding availibility
    original_url = 'http://jewel.cs.man.ac.uk:3010/booking?page='
    booking_xml = ("<bookings><request_id>"
                        + time_id + "</request_id><username>"
                        + username + "</username><password>"
                        + password + "</password></bookings>")
    # Change the output if no slots are booked
    numberOfSlots = 0
    #Repeat for the 4 pages of slots
    for i in range(1, 5):
        url = original_url + str(i)
        # Use request to retrieve the html and convert this to text to be parsed
        x = requests.put(url, data = booking_xml, headers = headers)
        x = (x.text)
        # Parse the string and iterate over each row and print the values
        table = etree.HTML(x).find("body/table")
        rows = iter(table)
        for row in rows:
            values = [col.text for col in row]
            # If the username if found in the list of values print out the slot
            if " 3oo112 " in values:
                numberOfSlots += 1
                print("You have reserved slot:" + values[0])
    # Message displayed if no bookings are held
    if (numberOfSlots == 0):
        print("You don't currently hold any hotel slots")
    print("===============================================")
    main()



# 7:
# Function to cancel a band booking
def cancel_band_booking():
    print("===============================================")
    print("Cancel a band booking...")
    print("===============================================")
    slot_id = str(input("Enter a slot to cancel: "))
    # Get the current time to use as a request id
    time_id = str(datetime.datetime.now())
    # URL and xml string for finding availibility
    url = 'http://jewel.cs.man.ac.uk:3020/queue/enqueue'
    cancel_xml = ("<cancel><request_id>"
                        + time_id + "</request_id><username>"
                        + username + "</username><password>"
                        + password + "</password><slot_id>"
                        + slot_id + "</slot_id></cancel>")
    # Use request to retrieve the html and convert this to text to be parsed
    x = requests.put(url, data = cancel_xml, headers = headers)
    x = (x.text)
    # Remove the xml tags around the url and concatenate with username/password
    x = x[9:-10]
    url = x + "?username=3oo112&password=Ruv2Hu"
    # Make a new request with the above url to retrieve the message
    x = requests.get(url)
    x = x.text
    # If the server is unavailable wait for 2 seconds and make a new request
    print("Waiting for the server to respond...")
    while (x == "Message unavailable" or x == "Service unavailable"):
        time.sleep(2)
        x = requests.get(url)
        x = x.text
        print("...")
    # Remove the tags around the message to display to the user
    if "<code>200</code>" in x:
        x = x[40:]
        x = x[0:21]
    else:
        x = x[32:-18]
    print(x)
    print("===============================================")
    main()



# 8:
# Function to cancel a hotel booking
def cancel_hotel_booking():
    print("===============================================")
    print("Cancel a hotel booking...")
    print("===============================================")
    slot_id = str(input("Enter a slot to cancel: "))
    # Get the current time to use as a request id
    time_id = str(datetime.datetime.now())
    # URL and xml string for finding availibility
    url = 'http://jewel.cs.man.ac.uk:3010/queue/enqueue'
    cancel_xml = ("<cancel><request_id>"
                        + time_id + "</request_id><username>"
                        + username + "</username><password>"
                        + password + "</password><slot_id>"
                        + slot_id + "</slot_id></cancel>")
    # Use request to retrieve the html and convert this to text to be parsed
    x = requests.put(url, data = cancel_xml, headers = headers)
    x = (x.text)
    # Remove the xml tags around the url and concatenate with username/password
    x = x[9:-10]
    url = x + "?username=3oo112&password=Ruv2Hu"
    # Make a new request with the above url to retrieve the message
    x = requests.get(url)
    x = x.text
    # If the server is unavailable wait for 2 seconds and make a new request
    print("Waiting for the server to respond...")
    while (x == "Message unavailable" or x == "Service unavailable"):
        time.sleep(2)
        x = requests.get(url)
        x = x.text
        print("...")
    # Remove the tags around the message to display to the user
    if "<code>200</code>" in x:
        x = x[40:]
        x = x[0:21]
    else:
        x = x[32:-18]
    print(x)
    print("===============================================")
    main()




# Menu to allow user to pick what functionality to use
def main():
    print("\n")
    print("===============================================")
    print("""Please select one of the following options...\n
          0: Exit program\n
          1: Check availibility for bands\n
          2: Check availibility for hotels\n
          3: Reserve a band slot\n
          4: Reserve a hotel slot\n
          5: Check your band bookings\n
          6: Check your hotel bookings\n
          7: Cancel a band booking\n
          8: Cancel a hotel booking\n""")
    choice = input("Enter option: ")
    print("\n")

    # Depending on the users input call the relevent function
    switcher = {
        0: exit_program,
        1: check_band_availibility,
        2: check_hotel_availibility,
        3: reserve_band_slot,
        4: reserve_hotel_slot,
        5: check_band_booking,
        6: check_hotel_booking,
        7: cancel_band_booking,
        8: cancel_hotel_booking
    }
    function = switcher.get(choice, lambda: "Invalid choice")
    function()

# Call main at the start of the program
main()
