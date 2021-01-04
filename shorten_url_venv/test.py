import bitly_api
API_KEY = "2fa1d905646fe5aab2ef73b3e6338f8e7032eb12" 
access = bitly_api.Connection(access_token = API_KEY)
shortened_url = access.shorten("https://www.google.co.in/")

print(shortened_url['url'])