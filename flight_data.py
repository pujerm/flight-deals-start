import requests


class FlightData:
    r = requests.get("https://api.sheety.co/b7215182fbcee764ae846215ff9cf24e/flightDeals/prices")
    data = r.json()

    old_list = {}

    for x in data['prices']:

        old_list[x['iataCode']] = {
            "lowest_price": x['lowestPrice'],
            "city": x['city']
        }



    pass
