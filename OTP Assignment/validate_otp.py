import random
import smtplib

def generateOTP():
    otp = ''.join([str(random.randint(0,9)) for i in range(4)])
    return otp


def sendOTPOverEmail(email, otp):
    if validateEmail(email):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('hanumanj2k3@gmail.com', 'iqvuzodoqtsvlfks')
        msg = 'Hello, your OTP is '+ str(otp) +  '\nPlease do not share the OTP with anyone.' +  '\nThis is System generated mail so do not reply.'
        server.sendmail("hanumanj2k3@gmail.com","nihalsathawane2003@gmail.com",msg)
        print(f"OTP is sent to email via email.")
    else:
        print("Invalid email address.")


def sendOTPOverMobile(mobile, otp):
    if validateMobile(mobile):
        
        from twilio.rest import Client
        import keys

        client = Client(keys.account_sid,keys.auth_token)
        msg = client.messages.create(

            body = 'Hello, your OTP is '+ str(otp) +  '\nPlease do not share the OTP with anyone.' +  '\nThis is System generated mail so do not reply.',
            from_ = keys.twilio_number,
            to = keys.target_number  
        )
        

        print(msg.body)
    else:
        print("Invalid mobile number.")


def validateEmail(email):
    
    if "@gmail" in email and "." in email:
        return True
    else:
        return False


def validateMobile(mobile):
    
    if len(mobile) == 10 and mobile.isdigit():
        return True
    else:
        return False


if __name__ == "__main__":
    
    otp = generateOTP()

    
    email = "nihalsathawane2003@gmail.com"
    sendOTPOverEmail(email, otp)

    
    mobile = "7875808821"
    sendOTPOverMobile(mobile, otp)
