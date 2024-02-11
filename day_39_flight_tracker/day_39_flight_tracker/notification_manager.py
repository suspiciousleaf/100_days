from twilio.rest import Client

from credentials import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, twilio_number, my_number


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        pass

    def send_sms(self, flight):
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN

        try:
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'Cheap flight found! Only € {flight["data"][0]["price"]} to fly from {flight["data"][0]["cityFrom"]}-{flight["data"][0]["route"][0]["flyFrom"]} to {flight["data"][0]["cityTo"]}-{flight["data"][0]["route"][0]["flyTo"]}',  # from {} - {}',
                from_=twilio_number,
                to=my_number,
            )

        except Exception as e:
            print(f"Unable to send SMS: {e}")
