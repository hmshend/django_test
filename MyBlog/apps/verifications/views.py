# Create your views here.
import logging

from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django_redis import get_redis_connection

from . import constants
from utils.captcha.captcha import captcha
from users.models import User

logger = logging.getLogger('django')
class ImageCode(View):

    def get(self, request, image_code_id):
        text, image = captcha.generate_captcha()
        con_redis = get_redis_connection(alias='verify_codes')
        img_key = 'img_{}'.format(image_code_id)
        logger.info(img_key)
        con_redis.setex(img_key, constants.IMAGE_CODE_REDIS_EXPIRES, text)
        logger.info('Image Code: {}'.format(text))
        return HttpResponse(content=image, content_type="images/jpg")


class CheckUsernameView(View):

    # 1、创建一个类视图
    def get(self, request, username):
        # 2、校验参数
        # 3、查询数据
        # user = User.objects.filter(username=username)
        # 4、返回校验的结果
        # if not user:
        #     return HttpResponse('可以注册')
        # else:
        #     return HttpResponse('不能注册')
        count = User.objects.filter(username=username).count()
        data = {
            'username': username,
            'count': count
        }
        return JsonResponse(data=data)

