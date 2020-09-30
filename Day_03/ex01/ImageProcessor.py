import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import sys


class ImageProcessor:
    def load(self, path):
        try:
            img = mpimg.imread(path)
        except FileNotFoundError:
            print("File not found")
            exit(1)
        if img.dtype == np.float32:
            img = (img * 255).astype(np.uint8)
        print("Loading image of dimensions %d x %d" % (
            img.shape[0], img.shape[1]))
        return img

    def display(self, array):
        plt.imshow(array)
        plt.show()


def main():
    if len(sys.argv) < 2:
        path = "../pictures/Lyon.jpg"
    else:
        path = sys.argv[1]
    ip = ImageProcessor()
    i = ip.load(path)
    print(i)
    ip.display(i)


if __name__ == "__main__":
    main()
