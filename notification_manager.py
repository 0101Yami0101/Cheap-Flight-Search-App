from twilio.rest import Client

TWILIO_AUTH = "85985b20f6f9426387679f68958f26cf"
SID = "ACb395f4340abc099e6fbffcb1ff018d08"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details via Twilio
    def send_notification(self, price, from_Loc,from_IATA, to_Loc, to_IATA, outbound_date, inbound_date):
        pass

        client = Client(SID, TWILIO_AUTH)

        message = client.messages \
                        .create(
                            body= f"LOW PRICE ALERT!!! Only ₹ {price} to fly from {from_Loc}-{from_IATA} to {to_Loc}-{to_IATA}, from {outbound_date} to {inbound_date} ",
                            from_='+12029785045', #OWN GENERATED NUMBER/OWN TWILIO ACCOUNT
                            to='+916002059806' #VERIFIED NUMBER
                        )
        print(message.status)