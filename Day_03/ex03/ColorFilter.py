import sys
from ex01.ImageProcessor import ImageProcessor
import numpy as np


class ColorFilter:

    def invert(self, array):
        new = array.copy()
        for i in range(0, array.shape[0]):
            for j in range(0, array.shape[1]):
                r = 255 - array[i, j][0]
                v = 255 - array[i, j][1]
                b = 255 - array[i, j][2]
                new[i, j] = [r, v, b]
        return new

    def to_blue(self, array):
        new = np.zeros(array.shape, dtype="uint8")
        for i in range(0, array.shape[0]):
            for j in range(0, array.shape[1]):
                new[i, j][2] = array[i, j][2].copy()
        return new

    def to_green(self, array):
        new = array.copy()
        for i in range(0, array.shape[0]):
            for j in range(0, array.shape[1]):
                new[i, j][0] = array[i, j][0] * 0
                new[i, j][1] = array[i, j][1] * 1
                new[i, j][2] = array[i, j][2] * 0
        return new

    def to_red(self, array):
        blue = self.to_blue(array)
        green = self.to_green(array)
        red = array.copy()
        for i in range(0, array.shape[0]):
            for j in range(0, array.shape[1]):
                red[i, j][1] -= green[i, j][1]
                red[i, j][2] -= blue[i, j][2]
        return red

    def celluloid(self, array):
        pass

    def to_grayscale(self, array):
        pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        path = "../pictures/musk.jpg"
    else:
        path = sys.argv[1]

    ip = ImageProcessor()
    img = ip.load(path)
    cf = ColorFilter()
    img2 = cf.to_blue(img)
    ip.display(img2)
    img3 = cf.to_green(img)
    ip.display(img3)
    img4 = cf.to_red(img)
    ip.display(img4)
