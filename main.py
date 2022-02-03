# import library
import requests
import csv

HEADERS = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'method': 'POST'
}
# open data csv
with open("input.csv", "r") as f:
    input_data = csv.DictReader(f)
    # function for check data
    for k in input_data:

        keys = list(k.values())

        datas = {
            'companyNsame': keys[0],
            'address1': keys[1],
            'city': keys[2],
            'state': keys[3],
            'zip': keys[4]
        }
        # check dada in request
        response = requests.post(url='https://tools.usps.com/tools/app/ziplookup/zipByAddress', data=datas,
                                 allow_redirects=False, headers=HEADERS)
        # find success value
        ok = response.text.find("SUCCESS")

        if ok == -1:
            vaild = ''
        else:
            vaild = 'Vaild'

        # create data csv vith check
        with open('new_data.csv', 'a', newline='') as f:
            fieldnames = ['Company', 'Street', 'City', 'St', 'ZIPCode', 'valid']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({'Company': keys[0],
                             'Street': keys[1],
                             'City': keys[2],
                             'St': keys[3],
                             'ZIPCode': keys[4],
                             'valid': vaild, })
