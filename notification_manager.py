import data_manager
from twilio.rest import Client
import enviroment

new_data = data_manager.DataManager.new_data_cheap
account_sid = enviroment.account_sid
auth_token = enviroment.auth_token
new_data_cheap = data_manager.DataManager.new_data_cheap
count = data_manager.DataManager.count


class NotificationManager:

    client = Client(account_sid, auth_token)

    if count != 0:

        for x in new_data_cheap:
            message = client.messages \
                .create(
                body=f'Low price alert! \nOnly €{new_data_cheap[x]["price"]}to fly from Warsaw-WAW to {new_data_cheap[x]["city"]}-{x}, from {new_data_cheap[x]["date_from"]} to {new_data_cheap[x]["date_back"]}',
                from_="+15736335279",
                to="+48881248882"
            )
            print(message.status)

    pass
