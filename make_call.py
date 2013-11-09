# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "AC264c92d0ed6dd6ecedc35bc304ac3634"
auth_token = "a7d38f89b3096948acb92ee119676675"
client = TwilioRestClient(account_sid, auth_token)

# Make the call
call = client.calls.create(to="+12037339862",
                           from_="+12038262959",
                           url="https://dl.dropboxusercontent.com/u/80891743/twilio.xml") #address is in my public dropbox folder
print call.sid
