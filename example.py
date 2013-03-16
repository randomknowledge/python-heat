# coding=utf-8
import random
from heatmap import get_heatmap_image


size = (600, 600)
points1 = []
points2 = []
points3 = []

for x in range(500):
    points1.append(
        (random.random() * 200 - 100, random.random() * 200 - 100)
    )
bounds = ((-100, -100), (100, 100))

for x in range(50):
    points2.append(
        (random.random() * 50 - 100, random.random() * 50 - 100)
    )

for x in range(50):
    points3.append(
        (random.random() * 50, random.random() * 50)
    )

get_heatmap_image(
    points1 + points2 + points3,
    data_bounds=bounds,
    size=size,
    scheme='classic',
    dotsize=30,
    pointgrid_size=1,
).save('example_1.png')

get_heatmap_image(
    points1 + points2 + points3,
    data_bounds=bounds,
    size=size,
    scheme='classic',
    dotsize=60,
    pointgrid_size=10,
).save('example_2.png')

get_heatmap_image(
    points1 + points2 + points3,
    data_bounds=bounds,
    size=size,
    scheme='classic',
    dotsize=100,
    pointgrid_size=70,
).save('example_3.png')

get_heatmap_image(
    points1[:200] + points2 + points3,
    data_bounds=bounds,
    size=size,
    scheme='fire',
    dotsize=120,
    pointgrid_size=20,
).save('example_4.png')

get_heatmap_image(
    points1 + points2 + points3,
    data_bounds=bounds,
    size=size,
    scheme='classic',
    dotsize=30,
    pointgrid_size=1,
    padding=100
).save('example_5.png')