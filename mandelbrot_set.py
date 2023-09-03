import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    mandelbrot_grid = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            c = complex(x[i], y[j])
            mandelbrot_grid[i, j] = mandelbrot(c, max_iter)

    return mandelbrot_grid

def plot_mandelbrot(mandelbrot_grid):
    plt.imshow(mandelbrot_grid.T, extent=(-2, 2, -2, 2))
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.title("Mandelbrot Set")
    plt.colorbar()
    plt.show()

width, height = 1000, 1000
x_min, x_max = -2.0, 2.0
y_min, y_max = -2.0, 2.0
max_iter = 256

mandelbrot_grid = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
plot_mandelbrot(mandelbrot_grid)