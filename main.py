from io import BytesIO

from PIL import Image
import numpy as np
import requests
import cv2

#CONSTANTS
API_ENDPOINT = 'https://shdu64vji0.execute-api.us-east-2.amazonaws.com/dev'
IMG_PATH = './catgivingflower.jpg'

def convertToGrayAPI(img):

    is_success, im_buf_arr = cv2.imencode(".png", img)
    byte_im = im_buf_arr.tobytes()

    r = requests.post(url=API_ENDPOINT, data=byte_im)

    img_ = Image.open(BytesIO(r.content))

    return np.asarray(img_)


def convertToGray(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return gray


if __name__ == "__main__":

    img = cv2.imread(IMG_PATH)

    img_gray = convertToGrayAPI(img)

    cv2.imwrite('./test_img_gray.png', img_gray)