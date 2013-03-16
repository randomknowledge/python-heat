# coding=utf-8
__version__ = '0.0.1'
from heatmap.generator import HeatMap


def get_heatmap_image(points, data_bounds=None, size=(256, 256),
                      scheme='classic', dotsize=50, pointgrid_size=1, padding=0):
    hm = HeatMap(size=size, scheme=scheme, dotsize=dotsize, pointgrid_size=pointgrid_size, padding=padding)
    hm.add_points(points=points, data_bounds=data_bounds)
    hm.generate()
    return hm.img


__all__ = [HeatMap]