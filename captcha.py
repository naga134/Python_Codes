from captcha.image import ImageCaptcha
from PIL import Image
import random
import string

def generate_captcha_text(lenght=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=lenght))

def generate_captcha_image(captcha_text, image_width=300):
    image = ImageCaptcha(image_width)