# Create your views here.
from django.http import HttpResponse
from django.views import View
from utils.captcha.captcha import captcha
from django_redis import get_redis_connection
from . import constants
import logging


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