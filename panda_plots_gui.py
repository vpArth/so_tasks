#!/usr/bin/env python
import PySimpleGUI as sg
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
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

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def main():
    x_min = 0
    x_max = 350
    step = np.pi / 30
    levels = 6
    source = sin_data(x_min, x_max, step, levels)

    layout = [
        [sg.Text('sin(x)', size=(40, 1), justification='center', font='Helvetica 20')],
        [sg.Canvas(size=(640, 480), key='-CANVAS-')],
    ]

    window = sg.Window('Sin(x)', layout, finalize=True)

    canvas_elem = window['-CANVAS-']
    canvas = canvas_elem.TKCanvas

    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
    fig_agg = draw_figure(canvas, fig)

    data_buffer = deque(maxlen=650)
    for (x, y) in source:
        data_buffer.append((x, y))

        event, values = window.read(timeout=10)
        if event in ('Exit', None):
            exit(69)

        ax.cla()
        ax.grid()
        ax.plot([x for x, _ in data_buffer], [y for _, y in data_buffer],  color='purple')

        fig_agg.draw()

    window.close()

if __name__ == '__main__':
    main()
