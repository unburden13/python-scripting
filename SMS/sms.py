from twilio.rest import Client  # OR https://ntfy.sh/  -- free, logins, no user permissions management, no API keys

account_sid = 'AC81b12455629b325d0ae662618efb1196'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16813753169',
  body='Again and again',
  to='+573122187468'
)

print(message.sid)