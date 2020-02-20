import csv
from sys import argv


class GoogleTrendAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.table = []
        self.headers = []
        with open(filename, 'r') as f:
            self.title = f.readline().strip()
            f.readline() # read in a blank line and do nothing with it
            reader = csv.reader(f)
            self.headers = reader.__next__() # give me the first row of the column headers
            for row in reader:
                self.table.append(row)

    def most_popular(self):
        """
        Return the string of the column with the highest popularity.
        :return:
        """


if __name__ == '__main__':
    # argv is a list of the things that you send into the command when you run python
    # have to run in the second argument for it to run

    if len(argv) < 2:
        print("Usage is stats.py [filename]")
    print(argv)
    analyzer = GoogleTrendAnalyzer(argv[1])
    print(analyzer.most_popular())