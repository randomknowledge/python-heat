# coding=utf-8
import os


DATA_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'data'
    )
)

DIR_COLORSCHEMES = os.path.abspath(
    os.path.join(
        DATA_DIR,
        'color-schemes'
    )
)

DIR_DOTS = os.path.abspath(
    os.path.join(
        DATA_DIR,
        'dots'
    )
)

DOT_IMAGE_SIZE = 100
DOT_MIN_SIZE = 1
DOT_MAX_SIZE = 150
