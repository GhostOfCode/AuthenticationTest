from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import vk_api

API_VER = vk_api.API_VER
APP_ID = vk_api.APP_ID
APP_KEY = vk_api.APP_KEY
APP_SECRET = vk_api.APP_SECRET


def index(request):
    if 'auth_test' not in request.COOKIES:
        r = HttpResponse(request)
        r.set_cookie('auth_test', 'VK_auth', max_age=60 * 60 * 24 * 2)
        return render(request, 'homepage.html')
    else:
        return redirect('http://127.0.0.1:8000/friendslist')


def login(request):
    return vk_api.login(request)

    # cache1 = caches['my']


def list_friends(request):
    vk_api.login(request)
    context = vk_api.get_friends(*vk_api.get_token(request))
    return render(request, 'friendslist.html', context=context)
