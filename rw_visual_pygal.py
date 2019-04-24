import matplotlib.pyplot as plt
import matplotlib.axes as ax
from random_walk_pygal import RandomWalk
import pygal

# Make a random walk, and plot the points


rw = RandomWalk(500)
rw.fill_walk()

print(rw.x_values)
print(rw.y_values)

dictionary = dict(zip(rw.x_values, rw.y_values))

print(dictionary)

print(rw.tp_list)

xy_chart = pygal.XY(stroke=False)
xy_chart.title = "Pygal is not a very fun library"
xy_chart.add('Group A', rw.tp_list)
xy_chart.render_to_file('rw_visual_pygal_24_4.svg')

