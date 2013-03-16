# coding=utf-8
import Image
import os
import re
from heatmap import constants


re_scheme_filename = re.compile(r'^(?P<name>[a-z0-9_-]+)\.png$')
valid_schemes = {}
for filename in os.listdir(constants.DIR_COLORSCHEMES):
    match = re_scheme_filename.search(filename)
    if match:
        valid_schemes[match.group('name')] = os.path.abspath(
            os.path.join(
                constants.DIR_COLORSCHEMES,
                filename
            )
        )


class ColorScheme():
    def __init__(self, scheme='classic'):
        if not scheme in valid_schemes.keys():
            raise ValueError("scheme must be one out of {0}!".format(valid_schemes.keys()))
        self.name = scheme
        self.scheme = Image.open(valid_schemes.get(self.name))

    def get(self):
        return self.scheme.load()