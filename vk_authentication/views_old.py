# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
# import requests
# from . import vk_api
#
# API_VER = vk_api.API_VER
# APP_ID = vk_api.APP_ID
# APP_KEY = vk_api.APP_KEY
# APP_SECRET = vk_api.APP_SECRET
#
#
# def index(request):
#     if 'auth_test' not in request.COOKIES:
#         return render(request, 'homepage.html')
#     else:
#         return redirect('http://127.0.0.1:8000/friendslist')
#
#
# def login(request):
#     try:
#         vk_api.login(request)
#         return redirect('http://127.0.0.1:8000/friendslist')
#     except requests.ConnectionError as error:
#         return HttpResponse(error)
#
#
# def list_friends(request):
#     token, user_id = vk_api.login(request)
#     friend_list = vk_api.get_friends(token, user_id)
#     return render(request, 'friendslist.html', context=friend_list)

# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# import requests
# import re
#
#
# API_VER = 5.122
# APP_ID = 7580883
# APP_KEY = 'UigEwK1kQwRnrcypb4Rd'
# APP_SECRET = '18b7745318b7745318b774533e18c4d880118b718b7745347fb5e7a01939f35035a1cb0'
#
#
# def index(request):
#     if 'auth_test' not in request.COOKIES:
#         return render(request, 'homepage.html')
#     else:
#         return HttpResponseRedirect('http://127.0.0.1:8000/friendslist')
#
#
# def login(request):
#     try:
#         response = requests.get('https://oauth.vk.com/authorize?client_id={0}'.format(APP_ID),
#                                 params={'scope': 2,
#                                         'redirect_uri': 'http://127.0.0.1:8000/friendslist', 'response_type': 'code',
#                                         'display': 'popup', 'v': API_VER})
#         return HttpResponseRedirect(response.url)
#     except requests.ConnectionError as error:
#         return HttpResponse(error)
#
#
# def get_token(request):
#     absolute_uri = request.build_absolute_uri()
#     code = re.split('code=', absolute_uri)[-1]
#     return_link = 'https://oauth.vk.com/access_token?client_id={0}'.format(APP_ID)
#     get_token_and_id = requests.get(return_link, params={
#         'client_secret': APP_KEY, 'redirect_uri': 'http://127.0.0.1:8000/friendslist',
#         'code': code, 'v': API_VER})
#     data = get_token_and_id.json()
#     print(data)
#     token = data['access_token']
#     user_id = data['user_id']
#     return code, token, user_id
#
#
# def get_friends(code, token, user_id):
#     get_friends_link = 'https://api.vk.com/method/friends.get'
#     get_friends_list = requests.get(get_friends_link, params={
#                                               'access_token': token,
#                                               'user_id': user_id,
#                                               'v': API_VER,
#                                               'order': 'random',
#                                               'count': 5,
#                                               'fields': 'city, domain',
#                                           })
#     vk_friends_list = get_friends_list.json()
#     context = {'vk_list': vk_friends_list['response']['items']}
#     return context
#
#
# def list_friends(request):
#     code, token, user_id = get_token(request)
#     context = get_friends(code, token, user_id)
#     if 'auth_test' not in request.COOKIES:
#         response_cookie = HttpResponse()
#         response_cookie.set_cookie('auth_test', 'VK_auth', max_age=60 * 60 * 24 * 2)
#         print(response_cookie.cookies)
#     return render(request, 'friendslist.html', context=context)

# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
# import requests
# from . import vk_api
#
# API_VER = vk_api.API_VER
# APP_ID = vk_api.APP_ID
# APP_KEY = vk_api.APP_KEY
# APP_SECRET = vk_api.APP_SECRET
#
#
# def index(request):
#     if 'auth_test' not in request.COOKIES:
#         return render(request, 'homepage.html')
#     else:
#         return redirect('http://127.0.0.1:8000/friendslist')
#
#
# def login(request):
#     try:
#         vk_api.login(request)
#         return redirect('http://127.0.0.1:8000/friendslist')
#     except requests.ConnectionError as error:
#         return HttpResponse(error)
#
#
# def list_friends(request):
#     token, user_id = vk_api.login(request)
#     friend_list = vk_api.get_friends(token, user_id)
#     return render(request, 'friendslist.html', context=friend_list)

# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# import requests
# import re
#
# API_VER = 5.122
# APP_ID = 7580883
# APP_KEY = 'UigEwK1kQwRnrcypb4Rd'
# APP_SECRET = '18b7745318b7745318b774533e18c4d880118b718b7745347fb5e7a01939f35035a1cb0'
#
#
# def index(request):
#     if not request.COOKIES.get('auth_test'):
#         return render(request, 'homepage.html')
#     else:
#         return HttpResponseRedirect('http://127.0.0.1:8000/friendslist')
#
#
# def login(request):
#     try:
#         response = requests.get('https://oauth.vk.com/authorize?client_id={0}'.format(APP_ID),
#                                 params={'scope': 2,
#                                         'redirect_uri': 'http://127.0.0.1:8000/friendslist', 'response_type': 'code',
#                                         'display': 'popup', 'v': API_VER})
#         return HttpResponseRedirect(response.url)
#     except requests.ConnectionError as error:
#         return HttpResponse(error)
#
#
# def get_token(request):
#     token = request.GET.get('access_token')
#     user_id = request.GET.get('user_id ')
#     absolute_uri = request.build_absolute_uri()
#     code = re.split('code=', absolute_uri)[-1]
#     return_link = 'https://oauth.vk.com/access_token?client_id={0}'.format(APP_ID)
#     get_token_and_id = requests.get(return_link, params={
#         'client_secret': APP_KEY, 'redirect_uri': 'http://127.0.0.1:8000/friendslist',
#         'code': code, 'v': API_VER})
#     data = get_token_and_id.json()
#     print(data)
#     token = data['access_token']
#     user_id = data['user_id']
#     return code, token, user_id
#
#
# def list_friends(request):
#     code, token, user_id = get_token(request)
#     get_friends_link = 'https://api.vk.com/method/friends.get'
#     get_friends_list = requests.get(get_friends_link, params={
#         'access_token': token,
#         'user_id': user_id,
#         'v': API_VER,
#         'order': 'random',
#         'count': 5,
#         'fields': 'city, domain',
#     })
#     vk_friends_list = get_friends_list.json()
#     context = {'vk_list': vk_friends_list['response']['items']}
#     if 'auth_test' not in request.COOKIES:
#         response = HttpResponse()
#         response.set_cookie('auth_test', 'VK_auth', max_age=60 * 60 * 2, secure=True)
#         print(request.COOKIES)
#     return render(request, 'friendslist.html', context=context)
