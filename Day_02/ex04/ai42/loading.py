from time import sleep, time
import sys


def ft_progress(lst):
    ln = len(lst)
    start = time()
    bar_wide = 25
    for i, elem in enumerate(lst):
        if i != 0:
            sys.stdout.write(u"\u001b[A")
        percent = int(elem / ln * 100)
        elapsed = time() - start
        eta = elapsed / (percent + 0.1) * 100 - elapsed
        bar = "ETA: {0:.2f} s".format(eta)
        bar += " [{0:02}%]".format(percent)
        width_bar = int(percent * bar_wide / 100)
        bar += "[{0: <25}]".format("=" * width_bar + ">")
        bar += "{elem}/{ln} | elapsed time {etime:.2f}s".format(elem=elem, ln=ln, etime=elapsed)
        bar += "\n..."
        sys.stdout.write(u"\u001b[%dD" % int(len(bar) + 1))
        sys.stdout.write(bar)
        sys.stdout.flush()
        yield elem


def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)


if __name__ == "__main__":
    main()
