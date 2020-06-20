import functools

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from NeuralPainter.utils import SingletonMeta


class TransferLearningNetwork(metaclass=SingletonMeta):
    output_image_size = 384
    style_image_size = 256

    def __init__(self):
        hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
        self.hub_module = hub.load(hub_handle)

    def transform(self, content_image_path, style_image_path):
        content_img_size = (self.output_image_size, self.output_image_size)
        style_img_size = (self.style_image_size, self.style_image_size)

        content_image = self.__load_image(content_image_path, content_img_size)
        style_image = self.__load_image(style_image_path, style_img_size)
        style_image = tf.nn.avg_pool(style_image, ksize=[3, 3], strides=[1, 1], padding='SAME')
        outputs = self.hub_module(tf.constant(content_image), tf.constant(style_image))
        return (outputs[0][0]).numpy()

    @staticmethod
    def __crop_center(image):
        shape = image.shape
        new_shape = min(shape[1], shape[2])
        offset_y = max(shape[1] - shape[2], 0) // 2
        offset_x = max(shape[2] - shape[1], 0) // 2
        image = tf.image.crop_to_bounding_box(
            image, offset_y, offset_x, new_shape, new_shape)
        return image

    @functools.lru_cache(maxsize=None)
    def __load_image(self, image_path, image_size=(256, 256), preserve_aspect_ratio=True):
        a = plt.imread(image_path)
        img = plt.imread(image_path).astype(np.float32)[np.newaxis, ...]
        if img.max() > 1.0:
            img = img / 255.
        if len(img.shape) == 3:
            img = tf.stack([img, img, img], axis=-1)
        img = self.__crop_center(img)
        img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
        return img
