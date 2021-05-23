import http.client
import json
import time
from dateutil.parser import parse
from datetime import date, datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

datee = input('Date (leave empty if you want the date to be today): ')
if(datee == ''):
    today = date.today()
    print(today)
else:
    today = datetime.strptime(datee , '%Y-%m-%d')
    print(today)

bookingStartTime = input('start time: ')
bookingEndTime = input('end time: ')
print(bcolors.OKBLUE+'You can find you cookie when making a request online and copy the cookie on the get-availability request'+bcolors.ENDC)
cookie = input('cookie: ')

bookingStartTime = parse(str(today)+'T'+bookingStartTime+':00')
bookingEndTime = parse(str(today)+'T'+bookingEndTime+':00')



# check if authorized
def autorized():
    conn = http.client.HTTPSConnection("my.basic-fit.com")
    payload = ''
    headers = {
    'authority': 'my.basic-fit.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'mbf-rct-app-api-2-caller': 'true',
    'mbfloginheadvform': 'jk#Bea201',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://my.basic-fit.com/overview',
    'accept-language': 'en-US,en;q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Im1lbWJlciI6eyJwZW9wbGVJZCI6IjNENjkxQkNFLTJCRUQtNEVDRC1CN0U1LTExNDQ1MjJDMDU3OCIsImVtYWlsIjoiYWNocmFmYmFyZGFuMTRAZ21haWwuY29tIiwibGNpZCI6Im5sX05MIiwiZW1wbG95ZWUiOmZhbHNlfSwiYXV0aCI6eyJzY29wZSI6Im1lbWJlciJ9fSwiaWF0IjoxNjIxNjA5NjY0LCJleHAiOjE2MjE2MTMyNjR9.CE_OVqm4fiXusoP0VEiZi7NtusJwuAG5UNe5eVcpSXc',
    'Cookie': cookie
    }
    conn.request("GET", "/authentication/is-auth", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
# 53f8a330-5cbd-45be-a177-0cedfee57073 braak
# c465235a-721f-4a9f-844c-8fb04ac94a2c rakthof

autorized()


conn = http.client.HTTPSConnection("my.basic-fit.com")

showFalseTimes = input('Show all times: ');

headers = {
  'authority': 'my.basic-fit.com',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
  'accept': 'application/json, text/plain, */*',
  'mbf-rct-app-api-2-caller': 'true',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
  'content-type': 'application/json',
  'origin': 'https://my.basic-fit.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://my.basic-fit.com/gym-time-booking',
  'accept-language': 'en-US,en;q=0.9,nl;q=0.8',
  'cookie': cookie,
  }

def reservate(club, time):
    conn = http.client.HTTPSConnection("my.basic-fit.com")
    payload = json.dumps({
    "doorPolicy": time,
    "duration": "90",
    "clubOfChoice": {
        "name": "Helmond Rakthof",
        "id": club['code'],
        "country": "Nederland",
        "bookable": True,
        "status": "Open",
        "debt_check": False,
        "label_name": "1537",
        "longitude": 5.708592,
        "latitude": 51.471948,
        "blocked_countries": "Belgie, France, Luxembourg, Spain",
        "mbf_payment_page_disabled__c": True
    }
    })
    headers = {
    'authority': 'my.basic-fit.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'mbf-rct-app-api-2-caller': 'true',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://my.basic-fit.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://my.basic-fit.com/gym-time-booking',
    'accept-language': 'en-US,en;q=0.9,nl;q=0.8',
    'cookie': cookie,
    }
    conn.request("POST", "/door-policy/book-door-policy", payload, headers)
    res = conn.getresponse()
    data = res.read()

    if(json.loads(data)['message'] == 'Booked'):
        print(bcolors.OKCYAN+'Booked succesfully check app'+bcolors.ENDC)
    else:
        print(bcolors.FAIL+'Booked not succesfully check app'+bcolors.ENDC)
    
    exit()



def getTimes(club):
    payload = json.dumps({
    "dateTime": str(today),
    "clubId": club['code']
    })
    conn.request("POST", "/door-policy/get-availability", payload, headers)
    res = conn.getresponse()
    data = res.read()

    if(res.status == 204):
        print('go to basic fit and search for times to make it work')
        exit()

    for time in json.loads(data):
        if(time['openForReservation'] == True):
            startDateTime = parse(time['startDateTime'])
            if(startDateTime >= bookingStartTime and startDateTime <= bookingEndTime):

                print(bcolors.OKGREEN+time['startDateTime']+' '+str(time['openForReservation'])+' '+club['name']+ bcolors.ENDC)
                reservate(club, time)
        elif(showFalseTimes):
            print(bcolors.FAIL+time['startDateTime']+' '+str(time['openForReservation'])+' '+club['name']+ bcolors.ENDC)
    
    print(bcolors.OKBLUE+'Got all times'+bcolors.ENDC)

clubs = [
    {
        "code": "53f8a330-5cbd-45be-a177-0cedfee57073",
        "name": "braak",
    },
    {
        "code": "c465235a-721f-4a9f-844c-8fb04ac94a2c",
        "name": "rakthof",
    },
]

while True:
    for club in clubs:
        getTimes(club)
    time.sleep(3)
    
        
