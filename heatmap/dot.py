# coding=utf-8
import Image
from heatmap import constants
import os
import re


re_dot_filename = re.compile(r'^dot_(?P<num>\d+)\.png$')
dot_images = {}
for filename in os.listdir(constants.DIR_DOTS):
    match = re_dot_filename.search(filename)
    if match:
        dot_images[int(match.group('num'))] = Image.open(
            os.path.abspath(
                os.path.join(
                    constants.DIR_DOTS,
                    filename
                )
            )
        )


class Dot():
    def __init__(self, size=50):
        if size < constants.DOT_MIN_SIZE or size > constants.DOT_MAX_SIZE:
            raise ValueError("size must be >= {0} and <= {1}!".format(constants.DOT_MIN_SIZE, constants.DOT_MAX_SIZE))
        self.size = size
        self.images = {}
        for key, img in dot_images.iteritems():
            self.images[key] = img.resize((size, size), Image.ANTIALIAS)

    def get_image(self, strength):
        if strength < 0 or strength > 100:
            raise ValueError("strength must be between 0 and 100. Got {0}".format(strength))
        return self.images.get(strength, self.images[min(self.images.keys(), key=lambda k: abs(k-strength))])