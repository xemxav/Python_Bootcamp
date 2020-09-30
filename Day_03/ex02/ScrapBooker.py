import numpy as np
from ex01.ImageProcessor import ImageProcessor
import sys


class ScrapBooker:

    def crop(self, array, dimensions, position=(0, 0)):
        if array.shape[0] < dimensions[0] or array.shape[1] < dimensions[1]:
            raise ValueError("Can not enlarge picture")
        if position[0] > dimensions[0] or position[0] > dimensions[0]:
            raise ValueError("Can not enlarge picture")
        if position[0] + dimensions[0] > array.shape[0]:
            raise ValueError("Can not enlarge picture")
        if position[1] + dimensions[1] > array.shape[1]:
            raise ValueError("Can not enlarge picture")
        new = array[position[0]:position[0] + dimensions[0],
              position[1]:position[1] + dimensions[1], :array.shape[2]].copy()
        return new

    def thin(self, array, n, axis):
        if axis:
            y = 0
        else:
            y = 1
        # for i in range(0, array.shape[y]):
        #     if (i + 1) % n == 0:
        #         array = np.delete(array, i, y)
        # return array
        return np.delete(array, [index for index in range(array.shape[y])
                             if (index + 1) % n == 0], y)

    def juxtapose(self, array, n, axis):
        new = array.copy()
        for i in range(0, n - 1):
            if axis:
                new = np.hstack((new, array))
            else:
                new = np.vstack((new, array))
        return new

    def mosaic(self, array, dimension):
        new = array.copy()
        new = self.juxtapose(new, dimension[0], 0)
        new = self.juxtapose(new, dimension[1], 1)
        return new


if __name__ == "__main__":
    if len(sys.argv) < 2:
        path = "../pictures/Lyon.jpg"
    else:
        path = sys.argv[1]

    s = ScrapBooker()
    print("test of thin() in simple arrays:")
    a = np.arange(5 * 10 * 3).reshape((5, 10, 3))
    a = np.arange(12).reshape(4, 1, 3)
    print("avant : ")
    print(a)
    print("apres : ")
    print(s.thin(a, 1, 0))
    a = np.arange(5 * 10 * 3).reshape((5, 10, 3))
    print("avant : ")
    print(a)
    print("apres : ")
    print(s.thin(a, 2, 1))
    ip = ImageProcessor()
    img = ip.load(path)
    c = s.crop(img, (img.shape[0], img.shape[1]), (0, 0))
    ip.display(c)
    img2 = s.juxtapose(img, 2, 0)
    ip.display(img2)
    img3 = s.juxtapose(img, 2, 1)
    ip.display(img3)
    img4 = s.mosaic(img, (4, 6))
    ip.display(img4)
