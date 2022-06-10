from pprint import pprint
import sys
import itertools

class rle:
    def __init__(self,data):
        self.comp_string = data
        

    def compress(self):
        for char, same in itertools.groupby(self.comp_string):
            count = sum(1 for _ in same)
            yield char + str(count)


if __name__ == '__main__':
    data = sys.argv
    new_dir = "".join(rle(data[1]).compress())
    pprint(new_dir)
