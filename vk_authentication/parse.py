import requests
import re
from pprint import pprint

token = '656914596569145965691459ad651ab88a66569656914593a207c7e0b3638c784f53d18'
version = 5.122

# response = requests.get('https://api.vk.com/method/friends.get',
#                         params={
#                             'access_token': token,
#                             'user_id': 114760116,
#                             'v': version,
#                             'order': 'random',
#                             'count': 5,
#                             'fields': 'city, domain',
#                         }
#                         )
#
# data = response.json()
# pprint(data)

absolute_uri = 'http://127.0.0.1:8000/friendslist?code=7a6fa4dff77a228eeda56603b8f53806c883f011c40b72630bb50df056f6479e52a '
code = re.split('code=', absolute_uri)[1]
print(code)

absolute_uri = 'http://REDIRECT_URI#access_token=533bacf01e11f55b536a565b57531ad114461ae8736d6506a3&expires_in=86400&user_id=8492&state=123456'
code = re.split('access_token=|&expires_in=|user_id=|&', absolute_uri)
print(code)
