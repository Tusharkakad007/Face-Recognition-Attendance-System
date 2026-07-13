import os
import cv2
import numpy as np
import warnings
import time
from src.anti_spoof_predict import AntiSpoofPredict
from src.generate_patches import CropImage
from src.utility import parse_model_name

warnings.filterwarnings('ignore')


def check_image(image):
    height, width, channel = image.shape
    if width / height != 3 / 4:
        print("Image is not appropriate! Height/Width should be 4/3.")
        return False
    return True


def test(image, model_dir, device_id):
    model_test = AntiSpoofPredict(device_id)
    image_cropper = CropImage()

    image = cv2.resize(image, (int(image.shape[0] * 3 / 4), image.shape[0]))
    result = check_image(image)
    if result is False:
        return

    image_bbox = model_test.get_bbox(image)

    prediction = np.zeros((1, 3))
    test_speed = 0

    for model_name in os.listdir(model_dir):
        h_input, w_input, model_type, scale = parse_model_name(model_name)
        param = {
            "org_img": image,
            "bbox": image_bbox,
            "scale": scale,
            "out_w": w_input,
            "out_h": h_input,
            "crop": True,
        }
        if scale is None:
            param["crop"] = False
        img = image_cropper.crop(**param)
        start = time.time()
        prediction += model_test.predict(img, os.path.join(model_dir, model_name))
        test_speed += time.time() - start

    label = np.argmax(prediction)
    return label
