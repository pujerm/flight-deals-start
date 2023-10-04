import requests
import datetime
import flight_data
import enviroment

apikey = enviroment.apikey

list_of_city = flight_data.FlightData.old_list


class FlightSearch:
    yesterday = datetime.date.today() + datetime.timedelta(days=1)
    yesterday_format = f"{yesterday.day}%2F{yesterday.month}%2F{yesterday.year}"
    six_months_later = datetime.date.today() + datetime.timedelta(days=180)
    six_months_later_format = f"{six_months_later.day}%2F{six_months_later.month}%2F{six_months_later.year}"

    headers = {
        "apikey": apikey
    }
    new_data = {}
    for x in list_of_city:

        r = requests.get(
            url=f'https://api.tequila.kiwi.com/v2/search?fly_from=WAW&fly_to={x}&date_from={yesterday_format}&date_to={six_months_later_format}',
            headers=headers)
        data = r.json()

        dane = [data["data"][0]["id"], data["data"][0]["local_departure"], int(data["data"][0]["price"])]
        for y in data["data"]:

            if int(y["price"]) < (dane[2]):
                dane[0] = (y["id"])
                dane[1] = (y["local_departure"])
                dane[2] = (y["price"])

        new_time = f"{dane[1][8]}{dane[1][9]}%2F{dane[1][5]}{dane[1][6]}%2F{dane[1][0]}{dane[1][1]}{dane[1][2]}{dane[1][3]}"
        new_time_max = datetime.datetime.strptime((dane[1][:10]), "%Y-%m-%d") + datetime.timedelta(days=14)

        time_back = f"{new_time_max.day}%2F{new_time_max.month}%2F{new_time_max.year}"

        ra = requests.get(
            url=f'https://api.tequila.kiwi.com/v2/search?fly_from={x}&fly_to=WAW&date_from={time_back}&date_to={time_back}',
            headers=headers)
        data2 = ra.json()

        dane2 = [data2["data"][0]["id"], data2["data"][0]["local_departure"], int(data2["data"][0]["price"])]

        for y in data2["data"]:

            if int(y["price"]) < (dane2[2]):
                dane2[0] = (y["id"])
                dane2[1] = (y["local_departure"])
                dane2[2] = (y["price"])
        price_all = dane[2] + dane2[2]
        new_data[x] = {
            "id_to": dane[0],
            "date_from": dane[1][0:10],
            "price": price_all,
            "id_back": dane2[0],
            "date_back": dane2[1][0:10],
            "city": list_of_city[x]["city"]

        }

    pass
