import urllib
from collections import OrderedDict
from datetime import datetime
from geekshop import settings
from urllib.parse import urlunparse, urlencode
import urllib.request

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'vk-oauth2':
        api_url = urlunparse(('https',
                              'api.vk.com',
                              '/method/users.get',
                              None,
                              urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_200')),
                                                    access_token=response['access_token'],
                                                    v='5.126')),
                              None
                              ))
        resp = requests.get(api_url)
        if resp.status_code != 200:
            return

        data =resp.json()['response'][0]
        if data['sex']:
            user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

        if data['about']:
            user.shopuserprofile.aboutMe = data['about']

        if data['bdate']:
            bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
            print(bdate)
            age = timezone.now().date().year - bdate.year
            if age < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.vk.VKOAuth2')
            user.age = age

        if data['photo_200']:
            urllib.request.urlretrieve(data['photo_200'], f'{settings.MEDIA_ROOT}/users_avatar{user.pk}.jpg')
            user.avatar = f'users_avatar{user.pk}.jpg'
        user.save()
