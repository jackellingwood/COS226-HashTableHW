# Author: Jack Ellingwood
# Date: 11/18/25
# Assignment: COS226 HW 5: Hash Something Out 

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
        key = self._hash(value.movieName)
        if self.table[key] != None:
            self.collisions += 1
        
        originalKey = key
        while self.table[key]: # loops through filled slots
            key += 1
            if key == self.length:
                key = 0
            if key == originalKey:
                return "No more space, cannot store new value."

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
    titleTable = HashTable(15000)
    start = end = 0
    with open("MOCK_DATA.csv", encoding="UTF-8") as f:
        start = time.time_ns()
        for row in reader(f):
            titleTable.store(DataItem(row))
        end = time.time_ns() - start
    print([movie.movieName if movie else None for movie in titleTable.table])
    print()
    print("Time taken (s):", end / 10**9)
    print("Collisions:", titleTable.collisions)
    print("Wasted slots:", titleTable.get_empty_slots())


if __name__ == "__main__":
    main()