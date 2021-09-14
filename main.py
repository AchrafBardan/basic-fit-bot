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
        "id": club['id'],
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

def getClubs():
    conn = http.client.HTTPSConnection("my.basic-fit.com")
    payload = ''
    headers = {
    'authority': 'my.basic-fit.com',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'mbf-rct-app-api-2-caller': 'true',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://my.basic-fit.com/gym-time-booking',
    'accept-language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga_tracedock=GA1.2.1087863385.1631533660; _ga_tracedock_gid=GA1.2.626543270.1631533660; _ga_control=GA1.2.1087863385.1631533660; _ga_control_gid=GA1.2.508937287.1631533660; _gid=GA1.2.1560976197.1631533660; _hjid=62c1e13c-cc62-458f-a832-9eb000522a38; _tdid=1087863385.1631533660_1_1; _gcl_au=1.1.1503393276.1631533665; _scid=b149d56f-840a-471d-a643-95a00b534ee0; _fbp=fb.1.1631533665596.1809408134; _pin_unauth=dWlkPVlUWTVOVEU1WkRNdE9HTTRNUzAwTm1SakxUazNPVGN0TmpneVpqZGtZVEU1T1RjMA; _uetvid=691a02d0148811ec948e53552a84fc89; _tdbu=t1631533686145||_ga_tracedock~~GA1.2.1087863385.1631533660; cookieconsent_level=20; cookieconsent_variant=wnl__a1003; cookieconsent_seen=1; ak_bmsc=714D24C4A8208EFE0047908204BEB229~000000000000000000000000000000~YAAQX6HdWCawxJl7AQAAiGSF5A0v1J13RZknMwsYYbJh9KuMGnTB5+U6ZLHBxcHD9vBmTu2bYGLSZYcy07qIjmDUCTePIWt/w+ONN/GqNqcrepNTVy7/jQ6LNsk6R7ngk9xmBluVXr+aWLDUf/vRC6JLl+Cb2M/2Q4hG0RuxIiov+sJZCslSH/cnG+3c63TMsN1ZSvNscBpml+qnOhxyqahsKGFT8ropwthgUL3cbQwt56nTWscbBBjY1oMMPmJ9Rwxr0CqPNn4vPaLQ3iw1VDeP2yLAIUTa0OODuQPG4ltPj9hIU4ngPbApoClNqAIIi/enFrE/nG0O0CGt9ZKMwrTaBVBjgz7MVtfui7FeK0ZnDcMCLLTmePJos1052lOnx/2wOtdc1O4nFID8LQ==; bm_sz=B24AD8780E8904ED8B78B6FBE2C4D89C~YAAQX6HdWCewxJl7AQAAiGSF5A3RDCn0phU/SAnMjK2HEtPv6uvSToofMjy+W87EWAIb8/kBpA/W7lkIz37/ZNhTfq07Rj5hbq8SCeNA2EXRKKyzzeCgfSt9jLFA55gAETYAbY0NPdVdWVW5nJeIYTWOZ48MBIpWjbS0xqdJjCLBj2d4x+h0xJRxp/tesRUWJB+EHfTbUF0+IWfx1YphVOC7MLUIkeD+w/AXxrmLOj+vtgfzSZJkJkP5sYUJeyptEn98cyfxC6nk1vQp6k7l4eDP8YUBuUvhx9JRj0s/bpvPxRh9YRU=~3556419~3224132; connect.sid=s%3As33zv7YwGsyMPT38v8Q6q4GGpemJB6ln.colvsO0dfd6mT37AiTl9wimqR%2BFr1nyuu8pMbR64FKw; _abck=E16C9D448ACF1CE01D6098692D45A02E~0~YAAQX6HdWCuwxJl7AQAASH6F5AaVsO+0InyS/t7ZAz1l4HiSGHQgPb476gIFruzROuxMVbbg/RxcwplbdBFkscN87Hl/tlFUqQZpR3ROOWrVx/htpqbvbZhKvseSjs2eyi3p89CUyxMBYdWCoXR+tGMvoTKiEaYVkCgIPALIYCjq6X4AgtHXwL4I88zKOCWaJq4EBRyqz8aFiNgBpU1EL3rWG+KtxpYOBoCBeWTJz5W7KSTfVAtHumpHtXE2VYed4BKUUhdAPz77HL+25hjQW67kGkppxK6ZgvNr9reqWLHgFeXgZsuIiYGsDVIwSOHlUrdG2HiH8emkRQJP/TttxCM3rCR2wm6wt/AmrI0rLKI8p91Qhw2PF5ZhhYP3mywX42OiKEohIlZZF7DpWBdi0GFr37+JZ8DUQH4a~-1~-1~-1; LanguageCookie=Nederland-nl; gtm-sq-timestamp=-1; bm_mi=78F90D0AD1919FF16B6FD32117410EEB~omcu7LOfQqLo6616pvDhR90aet0+6wUj0ABekQ/fInNsYQG7+gp/oFtLO88FSSCrHjrg3DQoPXWEXV+lpK2+ebkF9HyoHkWjhuufxu66x5IFlNpCqIfZTBQdLJ5MzU20r8Pcen8GcImm/5fVvGVX+EdpuzSzcJFJ7gennckFJpAjH9dCMmfDmkCmYvDNq463cKqgUzAKSsRT+619FSZf5tLy/5e/B0wEgsiDQLQcTMrej7L44U5ygkx7n29zIV/N; RT="z=1&dm=my.basic-fit.com&si=d51f0249-d9ed-4cb2-88ca-c9cc4e61f299&ss=ktk4bkkr&sl=6&tt=mj&obo=5&rl=1"; gtm-sq-pageview=7; _ga_7XWEJD1FC5=GS1.1.1631626552.5.1.1631627363.0; _ga_NF41CTP09F=GS1.1.1631626552.5.1.1631627363.0; _ga=GA1.2.1087863385.1631533660; bm_sv=3834844E0DF5F59B0C7F146C8F8EEED9~/XD8b/wZdaEGQZjDTQ+UEYz7V2KqRThp/Aw/4VKsoOwvA5FzKC3CyGRLmAS70q+dGREKUXCCzB7ZXLE48qH9sXV2nGSuoj3LoiglHIIEsgqzHUALoZ9GTtcbJqDw9Uq516OguoHJxB8GXi9fDScqd7LpxfQhD1U8557ljgjUPZI=; _abck=E16C9D448ACF1CE01D6098692D45A02E~-1~YAAQZKHdWKrVxHF7AQAAJh6U5AZNVf/ZUjCDIheA30G890c5fB7IA9ZYiMZx0rEgr1g07/nE5ksroLF7Qf2u6Ga6NUG1sTBESwiVpyvwIsWf2X8K4/NsDlYEKbWHNtOOiMuzkpCJTSS8Vd2U+b1U0+2bvoNy5VPkqaUooJCZ8PxVBr3QduioLYY+21WRiCqne+BzUoJsZg93n3b2L6sFSa3UwKNvfBWCIZNNtSRxmgF9tUomufaVorUdUleHPM6VRT8tRSDSDDB/BPb2s76as76M+ZTLypPraCFshTV7rC32ylss0vQsA6NaoYZTBU6vbvJVntyEe2Z0YqkLwBYxNNgKo3gGx7Wmpk9sb+Vj1CF9rS1xArzXf6bYwrBjrRuXQ/Hth2uRiEJndjpSCggiBFq5qv4J4sH8V6nt~0~-1~-1; ak_bmsc=714D24C4A8208EFE0047908204BEB229~000000000000000000000000000000~YAAQZKHdWKvVxHF7AQAAJh6U5A3oTZNgYnNItQ/1/sLjlLXeynbvQpKXsKLYJyuPFrZH6QVBht6gXaIO8G6KG5zEWCPhHa4gJ5SLA/C7Wo8StUDS4GTA57QN00SBz8pLLonISzCuxMYoCspTErp5F74xjZqXEbSOWiwFxVJ/kxHaKgaJN1TJag91Kq8wh9kC/ZPLfAEH0It6hvwimJKKCcg23O6KdgbDpq6zMbPuhter+TeNob80fMmIYsEItSZfnPKvK4t1Wdq3URCb/lP7S30IfPVfw43b8XWokvLWVqLm5zV6IA5NB90MVYlxJ7hqusfnnA3T74Xz0jNkntjm5P9pb6Ya1mwmLCQEtiRsUgyj1uiebLjpSQpo2mcvEiKNAYKAmW1QS8QRCKUAzDVuedCCl49vg14gAmKQaBSi5eigFpUx',
    'if-none-match': 'W/"42f36-Jw0SnEziJesWHcYip73oPw8Ak2Y"'
    }
    conn.request("GET", "/door-policy/get-clubs", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    index = 0
    for time in json.loads(data):
        print(str(index) + ' ' + time['name'])
        index += 1

    return json.loads(data)


data = getClubs()
clubId = input('enter club id: ')


def getTimes(club):
    payload = json.dumps({
    "dateTime": str(today),
    "clubId": club['id']
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
    # {
    #     "code": "c465235a-721f-4a9f-844c-8fb04ac94a2c",
    #     "name": "rakthof",
    # },
]

while True:
    getTimes(data[int(clubId)])
    time.sleep(3)
    
        
