import csv


class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0,
                 skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = list()
        self.hl = list()

    def __enter__(self):
        self.file = open(self.filename, 'r')
        lines = self.file.readlines()
        start = 0
        stop = len(lines) - self.skip_bottom
        ln = -1
        if self.header is True:
            start += 1
            self.hl = lines[0][:-1].split(self.sep)
            ln = len(self.hl)
        start += self.skip_top
        self.data = list()
        for i, line in enumerate(lines[start:], start):
            if i == stop:
                break
            line = line[:-1].split(self.sep)
            if i == start and ln == -1:
                ln = len(line)
            if i > start and ln != len(line):
                return None
            else:
                self.data.append(line)
        return self

    def __exit__(self, *args, **kwargs):
        self.file.close()

    def getdata(self):
        return self.data

    def getheader(self):
        if self.header:
            return self.hl
        else:
            return None


if __name__ == "__main__":
    with CsvReader('MOCK_DATA.csv', header=True, skip_top = 2,skip_bottom=990)\
            as file:
        if file == None:
            print("The file is corrupted")
            exit(1)
        data = file.getdata()
        header = file.getheader()
    print("header:", header)
    for d in data:
        print(d)
