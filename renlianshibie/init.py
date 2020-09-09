from aip import AipFace
import base64
def init_baidu():
    APP_ID = '16391300'
    API_KEY = 'zHeIhOUgHMGwuGvijhlWKBn9'
    SECRET_KEY = 'VkAWkm3mqG4GIGMWIljV0Uyzf81C3cWM'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    return client
def image(img):
    with open(img, 'rb') as fo:
        image = fo.read()
    image = str(base64.b64encode(image), 'utf-8')
    return image
def option():
    options = {}
    options['face_field'] = "age,gender,beauty,glasses,race,emotion,face_shape"
    options['max_face_num'] = 10
    options["face_type"] = "LIVE"
    return options