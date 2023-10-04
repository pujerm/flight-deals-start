import flight_search
import flight_data

old_data = flight_data.FlightData.old_list
new_data = flight_search.FlightSearch.new_data


class DataManager:
    count = 0
    for x in old_data:
        if (old_data[x]["lowest_price"]) < new_data[x]["price"]:
            del new_data[x]
        else:
            count += 1
    new_data_cheap = new_data

    pass
