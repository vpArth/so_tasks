#!/usr/bin/env python
import PySimpleGUI as sg
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

def sin_data(start, stop, step, levels):
    lvl_step = 1/levels
    x = start
    while x < stop:
        y = np.sin(x)

        lvl = int(levels * y) / levels

        yield (x, lvl)
        x += step

def main():
    x_min = 0
    x_max = 350
    step = np.pi / 30
    levels = 6
    source = sin_data(x_min, x_max, step, levels)
    N = 650

    def show_plot():
        plt.xlabel('x')
        plt.ylabel('sin(x)')
        plt.title('Sin(x)')
        plt.grid(True)
        plt.show()


    data_buffer = deque(maxlen=N)
    i = 0
    for (x, y) in source:
        i += 1
        data_buffer.append((x, y))

        if i > 2*N/3:
            i = 0
            plt.plot([x for x, _ in data_buffer], [y for _, y in data_buffer],  color='purple')
            show_plot()
    plt.plot([x for x, _ in data_buffer], [y for _, y in data_buffer],  color='purple')
    show_plot()

if __name__ == '__main__':
    main()
