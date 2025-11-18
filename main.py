from csv import reader
import sys
import time


class DataItem:
    def __init__(self, line):
        self.movieName = line[0]
        self.genre = line[1]
        self.releaseDate = line[2]
        self.director = line[3]
        self.revenue = line[4]
        self.rating = line[5]
        self.durationMins = line[6]
        self.productionCompany = line[7]
        self.quote = line[8]


class HashTable():
    def __init__(self, length: int):
        self.length = length
        self.table = [None] * length
        self.collisions = 0

    def store(self, value: DataItem):
        # TODO currently does not handle collisions
        key = self._hash(value.movieName)
        if self.table[key] != None:
            self.collisions += 1
        self.table[key] = value

    def retrieve(self, strKey: str) -> DataItem:
        pass

    def _hash(self, data):
        key = 0
        for c in data:
            key += ord(c)
            # key %= sys.maxsize # perhaps not necessary as python can handle numbers above sys.maxsize
        return key % self.length
    
    def get_empty_slots(self):
        return self.table.count(None)


def main():
    titletable = HashTable(15000)
    with open("MOCK_DATA.csv", encoding="UTF-8") as f:
        start = time.time_ns()
        for row in reader(f):
            titletable.store(DataItem(row))
    print("Time taken (s):", (time.time_ns() - start) / 10**9)
    print("Collisions:", titletable.collisions)
    print("Wasted slots:", titletable.get_empty_slots())
    # print([movie.movieName if movie else None for movie in titletable.table])


if __name__ == "__main__":
    main()