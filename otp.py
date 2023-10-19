from twilio.rest import Client
import keys
import math
import random
client = Client(keys.account_sid, keys.auth_token)
data = "7875808821"
leng = len(data)
otp = ""


for i in range(6):
    otp += data[math.floor(random.random()*leng)]


message = client.messages.create(
    body="Your 6 digit OTP is "+otp,
    from_=keys.inputNO,
    to=keys.sendNo
)


print(message.body)