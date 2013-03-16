# coding=utf-8
import random
from heatmap import get_heatmap_image


size = (600, 600)
points = []

for x in range(500):
    points.append(
        (random.random() * 200 - 100, random.random() * 200 - 100)
    )
bounds = ((-100, -100), (100, 100))

for x in range(100):
    points.append(
        (random.random() * 50 - 100, random.random() * 50 - 100)
    )

for x in range(600):
    points.append(
        (random.random() * 50, random.random() * 50)
    )

get_heatmap_image(
    points,
    data_bounds=bounds,
    size=size,
    scheme='classic',
    dotsize=30,
    pointgrid_size=1,
).save('example_1.png')

get_heatmap_image(
    points,
    data_bounds=bounds,
    size=size,
    scheme='classic',
    dotsize=60,
    pointgrid_size=10,
).save('example_2.png')

get_heatmap_image(
    points,
    data_bounds=bounds,
    size=size,
    scheme='classic',
    dotsize=80,
    pointgrid_size=50,
).save('example_3.png')

get_heatmap_image(
    points,
    data_bounds=bounds,
    size=size,
    scheme='fire',
    dotsize=100,
    pointgrid_size=6,
).save('example_4.png')