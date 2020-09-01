from django.http import HttpResponseRedirect
import requests
import re


API_VER = 5.122
APP_ID = 7580883
APP_KEY = 'UigEwK1kQwRnrcypb4Rd'
APP_SECRET = '18b7745318b7745318b774533e18c4d880118b718b7745347fb5e7a01939f35035a1cb0'


def login(request):
    response = requests.get('https://oauth.vk.com/authorize?client_id={0}'.format(APP_ID),
                            params={'scope': 2,
                                    'redirect_uri': 'http://127.0.0.1:8000/friendslist', 'response_type': 'token',
                                    'v': API_VER})
    print(response.url)
    absolute_uri = request.build_absolute_uri()
    print(absolute_uri)
    token = re.split('access_token=|&expires_in=|user_id=|&', absolute_uri)[1]
    user_id = re.split('access_token=|&expires_in=|user_id=|&', absolute_uri)[2]
    if 'auth_test' not in request.COOKIES:
        # request.set_cookie('auth_test', 'VK_auth', max_age=60 * 60 * 24 * 2)
        response = HttpResponseRedirect(response.url)
        response.set_cookie('auth_test', 'VK_auth', max_age=60 * 60 * 24 * 2)
    return token, user_id


# def get_token(request):
#     absolute_uri = request.build_absolute_uri()
#     print(absolute_uri)
#     # code = re.split('code=', absolute_uri)[-1]
#     # token_link = 'https://oauth.vk.com/access_token?client_id={0}'.format(APP_ID)
#     # get_token_and_id = requests.get(token_link, params={
#     #     'client_secret': APP_KEY, 'redirect_uri': 'http://127.0.0.1:8000/friendslist',
#     #     'code': code, 'v': API_VER})
#     # data = get_token_and_id.json()
#     # print(data)
#     # token = data['access_token']
#     # user_id = data['user_id']
#     token = re.split('access_token=|&expires_in=|user_id=|&', absolute_uri)[1]
#     user_id = re.split('access_token=|&expires_in=|user_id=|&', absolute_uri)[2]
#     return token, user_id


def get_friends(token, user_id):
    get_friends_link = 'https://api.vk.com/method/friends.get'
    get_friends_list = requests.get(get_friends_link, params={
                                              'access_token': token,
                                              'user_id': user_id,
                                              'v': API_VER,
                                              'order': 'random',
                                              'count': 5,
                                              'fields': 'city, domain',
                                          })
    vk_friends_list = get_friends_list.json()
    context = {'vk_list': vk_friends_list['response']['items']}
    return context
